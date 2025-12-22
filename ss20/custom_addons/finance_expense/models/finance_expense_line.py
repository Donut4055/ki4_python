# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FinanceExpenseLine(models.Model):
    _name = 'finance.expense.line'
    _description = 'Finance Expense Line'
    _order = 'sequence, id'

    expense_id = fields.Many2one(
        comodel_name='finance.expense',
        string='Khoản chi tiêu',
        required=True,
        ondelete='cascade',
        help='Khoản chi tiêu mà chi tiết này thuộc về'
    )
    
    sequence = fields.Integer(
        string='Thứ tự',
        default=10,
        help='Thứ tự hiển thị của dòng chi tiết'
    )
    
    name = fields.Char(
        string='Mô tả chi tiết',
        required=True,
        help='Mô tả chi tiết của khoản chi (VD: Vé máy bay, Khách sạn, Ăn trưa)'
    )
    
    quantity = fields.Float(
        string='Số lượng',
        default=1.0,
        help='Số lượng đơn vị'
    )
    
    unit_price = fields.Float(
        string='Đơn giá',
        help='Đơn giá cho mỗi đơn vị'
    )
    
    subtotal = fields.Float(
        string='Thành tiền',
        compute='_compute_subtotal',
        store=True,
        help='Thành tiền = Số lượng × Đơn giá'
    )
    
    note = fields.Text(
        string='Ghi chú',
        help='Ghi chú bổ sung cho chi tiết này'
    )
    
    @api.depends('quantity', 'unit_price')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.quantity * record.unit_price
