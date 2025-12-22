# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FinanceExpense(models.Model):
    _name = 'finance.expense'
    _description = 'Finance Expense'

    name = fields.Char(
        string='Tên Field',
        required=True,
        help='Nội dung chi tiêu (VD: Tiếp khách A). Bắt buộc.'
    )
    
    expense_type = fields.Selection(
        selection=[
            ('travel', 'Đi chuyển'),
            ('food', 'Ăn uống'),
            ('other', 'Khác')
        ],
        string='Kiểu dữ liệu',
        default='travel',
        help='Mặc định là travel.'
    )
    
    amount = fields.Float(
        string='Yêu cầu',
        help='Số tiền yêu cầu.'
    )
    
    expense_date = fields.Date(
        string='Ngày chi tiêu.',
        help='Ngày chi tiêu.'
    )
    
    is_paid = fields.Boolean(
        string='Đã thanh toán chưa?',
        default=False,
        help='Đã thanh toán chưa? (Mặc định False).'
    )
    
    approval_note = fields.Text(
        string='Ghi chú duyệt chi',
        help='Ghi chú duyệt chi (Trường bảo mật).',
        groups='finance_expense.group_finance_manager'
    )
