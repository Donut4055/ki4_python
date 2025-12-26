from odoo import models, fields


class HotelRoomType(models.Model):
    _name = 'hotel.room.type'
    _description = 'Loại phòng khách sạn'

    name = fields.Char(string='Tên loại phòng', required=True)
    code = fields.Char(string='Mã loại')
