from datetime import datetime

from odoo import api, fields, models


class TaoPhieuLuongWizard(models.TransientModel):
    _name = 'tinh_luong.tao_phieu_luong_wizard'
    _description = 'Tạo nhanh phiếu lương'

    nhan_vien_id = fields.Many2one('nhan_vien', string='Nhân viên', required=True)
    thang = fields.Selection([
        ('1', 'T1'), ('2', 'T2'), ('3', 'T3'), ('4', 'T4'), ('5', 'T5'), ('6', 'T6'),
        ('7', 'T7'), ('8', 'T8'), ('9', 'T9'), ('10', 'T10'), ('11', 'T11'), ('12', 'T12')
    ], string="Tháng", required=True, default=lambda self: str(datetime.now().month))
    nam = fields.Integer(string="Năm", required=True, default=lambda self: datetime.now().year)
    chi_tao_thieu = fields.Boolean(string='Chỉ tạo nếu chưa có', default=True)

    def action_tao(self):
        self.ensure_one()
        PhieuLuong = self.env['hr_phieu_luong']

        existing = PhieuLuong.search([
            ('nhan_vien_id', '=', self.nhan_vien_id.id),
            ('thang', '=', self.thang),
            ('nam', '=', self.nam),
        ], limit=1)

        if existing and self.chi_tao_thieu:
            rec = existing
        elif existing:
            # If user wants to force-create, just open the existing one (avoid duplicates).
            rec = existing
        else:
            rec = PhieuLuong.create({
                'nhan_vien_id': self.nhan_vien_id.id,
                'thang': self.thang,
                'nam': self.nam,
            })

        return {
            'type': 'ir.actions.act_window',
            'name': 'Phiếu lương',
            'res_model': 'hr_phieu_luong',
            'view_mode': 'form',
            'res_id': rec.id,
            'context': {'default_nhan_vien_id': self.nhan_vien_id.id},
        }
