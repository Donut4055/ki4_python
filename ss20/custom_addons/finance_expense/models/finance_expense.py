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
    
    category_id = fields.Many2one(
        comodel_name='finance.category',
        string='Danh mục chi tiêu',
        ondelete='restrict',
        help='Danh mục chi tiêu của khoản chi này.'
    )
    
    expense_line_ids = fields.One2many(
        comodel_name='finance.expense.line',
        inverse_name='expense_id',
        string='Chi tiết khoản chi',
        help='Danh sách các dòng chi tiết của khoản chi tiêu này'
    )
    
    total_line_amount = fields.Float(
        string='Tổng tiền chi tiết',
        compute='_compute_total_line_amount',
        store=True,
        help='Tổng tiền tính từ các dòng chi tiết'
    )
    
    # Mối quan hệ Many2many: Một khoản chi tiêu có thể có nhiều thẻ
    tag_ids = fields.Many2many(
        comodel_name='finance.tag',
        relation='finance_expense_tag_rel',
        column1='expense_id',
        column2='tag_id',
        string='Thẻ/Nhãn',
        help='Các thẻ/nhãn gắn cho khoản chi tiêu này'
    )
    
    @api.depends('expense_line_ids.subtotal')
    def _compute_total_line_amount(self):
        """Tính tổng tiền từ tất cả các dòng chi tiết"""
        for record in self:
            record.total_line_amount = sum(record.expense_line_ids.mapped('subtotal'))

