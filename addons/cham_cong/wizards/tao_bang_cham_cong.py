from datetime import timedelta

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class TaoBangChamCongWizard(models.TransientModel):
    _name = 'cham_cong.tao_bang_cham_cong_wizard'
    _description = 'Tạo nhanh bảng chấm công'

    nhan_vien_id = fields.Many2one('nhan_vien', string='Nhân viên', required=True)
    tu_ngay = fields.Date(string='Từ ngày', required=True, default=fields.Date.context_today)
    den_ngay = fields.Date(string='Đến ngày', required=True, default=fields.Date.context_today)
    chi_tao_thieu = fields.Boolean(string='Chỉ tạo ngày chưa có', default=True)

    @api.constrains('tu_ngay', 'den_ngay')
    def _check_dates(self):
        for rec in self:
            if rec.tu_ngay and rec.den_ngay and rec.tu_ngay > rec.den_ngay:
                raise ValidationError("'Từ ngày' phải nhỏ hơn hoặc bằng 'Đến ngày'.")

    def action_tao(self):
        self.ensure_one()

        BangChamCong = self.env['bang_cham_cong']
        DangKy = self.env['dang_ky_ca_lam_theo_ngay']

        created = self.env['bang_cham_cong'].browse([])

        current = self.tu_ngay
        while current <= self.den_ngay:
            existing = BangChamCong.search([
                ('nhan_vien_id', '=', self.nhan_vien_id.id),
                ('ngay_cham_cong', '=', current),
            ], limit=1)

            if existing and self.chi_tao_thieu:
                current = current + timedelta(days=1)
                continue

            dk = DangKy.search([
                ('nhan_vien_id', '=', self.nhan_vien_id.id),
                ('ngay_lam', '=', current),
            ], limit=1)

            vals = {
                'nhan_vien_id': self.nhan_vien_id.id,
                'ngay_cham_cong': current,
                'dang_ky_ca_lam_id': dk.id if dk else False,
            }

            if existing:
                existing.write(vals)
                created |= existing
            else:
                created |= BangChamCong.create(vals)

            current = current + timedelta(days=1)

        return {
            'type': 'ir.actions.act_window',
            'name': 'Bảng chấm công',
            'res_model': 'bang_cham_cong',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', created.ids)] if created else [('nhan_vien_id', '=', self.nhan_vien_id.id)],
            'context': {'default_nhan_vien_id': self.nhan_vien_id.id},
        }
