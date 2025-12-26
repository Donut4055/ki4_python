from odoo import models, fields


class HotelCustomer(models.Model):
    _name = 'hotel.customer'
    _description = 'Khách hàng'

    name = fields.Char(string='Tên khách hàng', required=True)
    identity_card = fields.Char(string='Số CMND/CCCD')
    phone = fields.Char(string='Số điện thoại')

    _sql_constraints = [
        ('identity_card_unique', 'UNIQUE(identity_card)', 'Số CMND/CCCD đã tồn tại!')
    ]
