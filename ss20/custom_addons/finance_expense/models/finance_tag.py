# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FinanceTag(models.Model):
    _name = 'finance.tag'
    _description = 'Finance Tag'
    _order = 'name'

    name = fields.Char(
        string='Tên thẻ',
        required=True,
        help='Tên của thẻ/nhãn (VD: Khẩn cấp, Định kỳ, Dự án A)'
    )
    
    color = fields.Integer(
        string='Màu sắc',
        help='Màu sắc hiển thị của thẻ trong giao diện'
    )
    
    description = fields.Text(
        string='Mô tả',
        help='Mô tả chi tiết về thẻ này'
    )
    
    active = fields.Boolean(
        string='Hoạt động',
        default=True,
        help='Đánh dấu thẻ có đang hoạt động hay không'
    )
    
    # Mối quan hệ Many2many: Nhiều thẻ có thể gắn cho nhiều khoản chi tiêu
    expense_ids = fields.Many2many(
        comodel_name='finance.expense',
        relation='finance_expense_tag_rel',
        column1='tag_id',
        column2='expense_id',
        string='Các khoản chi tiêu',
        help='Danh sách các khoản chi tiêu có gắn thẻ này'
    )
    
    # Trường tính toán: Số lượng khoản chi tiêu có thẻ này
    expense_count = fields.Integer(
        string='Số lượng chi tiêu',
        compute='_compute_expense_count',
        help='Tổng số khoản chi tiêu được gắn thẻ này'
    )
    
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Tên thẻ phải là duy nhất!')
    ]
    
    @api.depends('expense_ids')
    def _compute_expense_count(self):
        """Tính số lượng khoản chi tiêu có thẻ này"""
        for record in self:
            record.expense_count = len(record.expense_ids)
