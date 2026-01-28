from odoo import models, fields, api


class NhanVienChamCong(models.Model):
    _inherit = 'nhan_vien'

    bang_cham_cong_ids = fields.One2many('bang_cham_cong', 'nhan_vien_id', string='Bảng chấm công')
    don_tu_ids = fields.One2many('don_tu', 'nhan_vien_id', string='Đơn từ')
    dang_ky_ca_lam_ids = fields.One2many('dang_ky_ca_lam_theo_ngay', 'nhan_vien_id', string='Đăng ký ca làm')

    bang_cham_cong_count = fields.Integer(compute='_compute_cham_cong_counts')
    don_tu_count = fields.Integer(compute='_compute_cham_cong_counts')
    dang_ky_ca_lam_count = fields.Integer(compute='_compute_cham_cong_counts')

    @api.depends('bang_cham_cong_ids', 'don_tu_ids', 'dang_ky_ca_lam_ids')
    def _compute_cham_cong_counts(self):
        for rec in self:
            rec.bang_cham_cong_count = len(rec.bang_cham_cong_ids)
            rec.don_tu_count = len(rec.don_tu_ids)
            rec.dang_ky_ca_lam_count = len(rec.dang_ky_ca_lam_ids)

    @api.model_create_multi
    def create(self, vals_list):
        employees = super().create(vals_list)
        # Auto-add new employees to currently open registration periods to avoid manual syncing.
        open_dots = self.env['dot_dang_ky'].search([
            ('trang_thai_dang_ky', '=', 'Đang mở'),
        ])
        if open_dots:
            for emp in employees:
                open_dots.write({'nhan_vien_ids': [(4, emp.id)]})
        return employees

    def action_open_bang_cham_cong(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Bảng chấm công',
            'res_model': 'bang_cham_cong',
            'view_mode': 'tree,form',
            'domain': [('nhan_vien_id', '=', self.id)],
            'context': {'default_nhan_vien_id': self.id},
        }

    def action_open_don_tu(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Đơn từ',
            'res_model': 'don_tu',
            'view_mode': 'tree,form',
            'domain': [('nhan_vien_id', '=', self.id)],
            'context': {'default_nhan_vien_id': self.id},
        }

    def action_open_dang_ky_ca_lam(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Đăng ký ca làm theo ngày',
            'res_model': 'dang_ky_ca_lam_theo_ngay',
            'view_mode': 'tree,form',
            'domain': [('nhan_vien_id', '=', self.id)],
            'context': {'default_nhan_vien_id': self.id},
        }
