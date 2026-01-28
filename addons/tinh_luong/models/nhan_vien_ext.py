from odoo import models, fields, api


class NhanVienTinhLuong(models.Model):
    _inherit = 'nhan_vien'

    phieu_luong_ids = fields.One2many('hr_phieu_luong', 'nhan_vien_id', string='Phiếu lương')
    phieu_luong_count = fields.Integer(compute='_compute_phieu_luong_count')

    @api.depends('phieu_luong_ids')
    def _compute_phieu_luong_count(self):
        for rec in self:
            rec.phieu_luong_count = len(rec.phieu_luong_ids)

    def action_open_phieu_luong(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Phiếu lương',
            'res_model': 'hr_phieu_luong',
            'view_mode': 'tree,form',
            'domain': [('nhan_vien_id', '=', self.id)],
            'context': {'default_nhan_vien_id': self.id},
        }
