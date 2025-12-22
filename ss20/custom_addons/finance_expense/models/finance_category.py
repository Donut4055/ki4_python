# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FinanceCategory(models.Model):
    _name = 'finance.category'
    _description = 'Finance Category'
    _order = 'name'

    name = fields.Char(
        string='Tên danh mục',
        required=True,
        help='Tên danh mục chi tiêu (VD: Văn phòng phẩm, Du lịch công tác). Bắt buộc.'
    )
    
    code = fields.Char(
        string='Mã danh mục',
        required=True,
        help='Mã danh mục chi tiêu (VD: VP, DL). Bắt buộc và duy nhất.'
    )
    
    description = fields.Text(
        string='Mô tả',
        help='Mô tả chi tiết về danh mục chi tiêu.'
    )
    
    active = fields.Boolean(
        string='Hoạt động',
        default=True,
        help='Đánh dấu danh mục có đang hoạt động hay không.'
    )
    
    expense_ids = fields.One2many(
        comodel_name='finance.expense',
        inverse_name='category_id',
        string='Các khoản chi tiêu',
        help='Danh sách các khoản chi tiêu thuộc danh mục này.'
    )
    
    expense_count = fields.Integer(
        string='Số lượng chi tiêu',
        compute='_compute_expense_count',
        help='Tổng số khoản chi tiêu trong danh mục này.'
    )
    
    total_amount = fields.Float(
        string='Tổng số tiền',
        compute='_compute_total_amount',
        help='Tổng số tiền của tất cả chi tiêu trong danh mục.'
    )
    
    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'Mã danh mục phải là duy nhất!')
    ]
    
    @api.depends('expense_ids')
    def _compute_expense_count(self):
        for record in self:
            record.expense_count = len(record.expense_ids)
    
    @api.depends('expense_ids.amount')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = sum(record.expense_ids.mapped('amount'))
