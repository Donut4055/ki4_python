from odoo import models, fields


class HotelService(models.Model):
    _name = 'hotel.service'
    _description = 'Dịch vụ đi kèm'

    name = fields.Char(string='Tên dịch vụ', required=True)
    price = fields.Integer(string='Giá dịch vụ')

    _sql_constraints = [
        ('price_positive', 'CHECK(price > 0)', 'Giá dịch vụ phải lớn hơn 0!')
    ]
