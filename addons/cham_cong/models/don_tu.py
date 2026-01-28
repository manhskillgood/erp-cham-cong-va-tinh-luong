from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class DonTu(models.Model):
    _name = 'don_tu'
    _description = 'Đơn từ'
    _rec_name = 'nhan_vien_id'

    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân viên", required=True)
    ngay_lam_don = fields.Date("Ngày làm đơn", required=True, default=fields.Date.today)
    ngay_ap_dung = fields.Date("Ngày áp dụng", required=True)
    ly_do = fields.Text("Lý do xin đơn")
    trang_thai_duyet = fields.Selection([
        ('cho_duyet', 'Chờ duyệt'),
        ('da_duyet', 'Đã duyệt'),
        ('tu_choi', 'Từ chối')
    ], string="Trạng thái phê duyệt", default='cho_duyet', required=True)

    loai_don = fields.Selection([
        ('nghi', 'Đơn xin nghỉ'),
        ('di_muon', 'Đơn xin đi muộn'),
        ('ve_som', 'Đơn xin về sớm')
    ], string="Loại đơn", required=True)

    # Thời gian xin đi muộn/về sớm (phút)
    thoi_gian_xin = fields.Float("Thời gian xin (phút)")

    @api.constrains('loai_don', 'thoi_gian_xin')
    def _check_thoi_gian_xin(self):
        for rec in self:
            if rec.loai_don in ('di_muon', 've_som') and rec.thoi_gian_xin <= 0:
                raise ValidationError("Vui lòng nhập 'Thời gian xin (phút)' > 0 cho đơn đi muộn/về sớm.")

    def action_submit(self):
        self.write({'trang_thai_duyet': 'cho_duyet'})

    def action_approve(self):
        self.write({'trang_thai_duyet': 'da_duyet'})
        self._sync_to_bang_cham_cong()

    def action_refuse(self):
        self.write({'trang_thai_duyet': 'tu_choi'})

    def action_reset_to_pending(self):
        self.write({'trang_thai_duyet': 'cho_duyet'})

    def _sync_to_bang_cham_cong(self):
        """Ensure the related attendance row exists and is linked to this request.

        This makes the approval instantly reflected in attendance status and payroll.
        """
        BangChamCong = self.env['bang_cham_cong']
        DangKy = self.env['dang_ky_ca_lam_theo_ngay']

        for rec in self:
            if not (rec.nhan_vien_id and rec.ngay_ap_dung):
                continue

            dk = DangKy.search([
                ('nhan_vien_id', '=', rec.nhan_vien_id.id),
                ('ngay_lam', '=', rec.ngay_ap_dung),
            ], limit=1)

            bcc = BangChamCong.search([
                ('nhan_vien_id', '=', rec.nhan_vien_id.id),
                ('ngay_cham_cong', '=', rec.ngay_ap_dung),
            ], limit=1)

            if bcc:
                bcc.write({
                    'don_tu_id': rec.id,
                    'dang_ky_ca_lam_id': dk.id if dk else bcc.dang_ky_ca_lam_id.id,
                })
            else:
                BangChamCong.create({
                    'nhan_vien_id': rec.nhan_vien_id.id,
                    'ngay_cham_cong': rec.ngay_ap_dung,
                    'don_tu_id': rec.id,
                    'dang_ky_ca_lam_id': dk.id if dk else False,
                })