from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from datetime import timedelta


class HotelBooking(models.Model):
    _name = 'hotel.booking'
    _description = 'Phiếu đặt phòng'

    code = fields.Char(string='Mã booking')
    check_in = fields.Date(string='Ngày nhận phòng', required=True, default=fields.Date.today)
    check_out = fields.Date(string='Ngày trả phòng')
    duration = fields.Integer(string='Số đêm', compute='_compute_duration', store=True)
    total_amount = fields.Integer(string='Tổng tiền', compute='_compute_total_amount', store=True)
    state = fields.Selection([
        ('draft', 'Nháp'),
        ('confirmed', 'Đã xác nhận'),
        ('done', 'Hoàn thành')
    ], string='Trạng thái', default='draft')
    
    customer_id = fields.Many2one('hotel.customer', string='Khách hàng', required=True)
    room_id = fields.Many2one('hotel.room', string='Phòng', required=True)
    service_ids = fields.Many2many('hotel.service', string='Dịch vụ')

    @api.depends('check_in', 'check_out')
    def _compute_duration(self):
        for record in self:
            if record.check_in and record.check_out:
                delta = record.check_out - record.check_in
                record.duration = delta.days
            else:
                record.duration = 0

    @api.depends('duration', 'room_id', 'service_ids')
    def _compute_total_amount(self):
        for record in self:
            room_price = 0
            if record.room_id and record.duration:
                room_price = record.room_id.price_per_night * record.duration
            
            service_price = sum(record.service_ids.mapped('price'))
            record.total_amount = room_price + service_price

    @api.onchange('check_in')
    def _onchange_check_in(self):
        if self.check_in:
            self.check_out = self.check_in + timedelta(days=1)

    @api.onchange('room_id')
    def _onchange_room_id(self):
        if self.room_id and self.room_id.status == 'maintenance':
            return {
                'warning': {
                    'title': 'Cảnh báo',
                    'message': 'Phòng này đang bảo trì, vui lòng chọn phòng khác!'
                }
            }

    @api.constrains('check_in', 'check_out')
    def _check_dates(self):
        for record in self:
            if record.check_out and record.check_in and record.check_out <= record.check_in:
                raise ValidationError('Ngày trả phòng không hợp lệ!')

    @api.constrains('room_id')
    def _check_room_available(self):
        for record in self:
            if record.room_id and record.room_id.status == 'occupied':
                raise ValidationError('Phòng này đang có khách ở!')
