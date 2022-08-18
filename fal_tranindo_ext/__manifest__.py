# -*- coding: utf-8 -*-
# Part of Odoo Falinwa Edition. See LICENSE file for full copyright and licensing details.
{
    'name': 'Falinwa Tranindo Extention',
    'version': '15.0.1.0.0',
    'author': 'Falinwa Limited',
    'summary': 'Module to handle tranindo extention from falinwa',
    'category': 'Falinwa Tranindo Extention',
    'website': "https://falinwa.com",
    'description':
    '''
        Module to handle tranindo extention from falinwa
    ''',
    'depends': [
        'base',
        'sale',
        'sale_stock',
        'sales_team',
        'account',
        'stock',
        'purchase',
        # 'report',
    ],
    'data': [
        # Form File
        'views/account_move_views.xml',
        'views/sale_order_views.xml',
        'views/res_company_views.xml',
        'views/stock_picking_views.xml',
        'views/purchase_order_view.xml',
        # Report File
        'report/tranindo_report_sj_transfer_header_footer.xml',
        'report/tranindo_report_sj_letter_header_footer.xml',
        'report/tranindo_voucher_a4_header_footer.xml',
        'report/tranindo_voucher_c5_header_footer.xml',
        'report/tranindo_invoice_letter_header_footer.xml',
        'report/tranindo_invoice_letter_c5_header_footer.xml',
        'report/tranindo_vendor_bill_c5_header_footer.xml',
        'report/tranindo_vendor_bill_a4_header_footer.xml',
        'report/tranindo_rpj_c5_header_footer.xml',
        'report/layouts.xml',
        'report/invoice_letter.xml',
        'report/invoice_letter_c5.xml',
        'report/sj_transfers_c5.xml',
        'report/sj_letters_c5.xml',
        'report/voucher_c5.xml',
        'report/voucher_a4.xml',
        'report/rpj_c5.xml',
        'report/vendor_bill_c5.xml',
        'report/vendor_bill_a4.xml',
        'report/tranindo_report_forecasted.xml',
        # Security
        'security/ir_server_action.xml',
    ],
    'css': [],
    'js': [],
    'installable': True,
    'active': False,
    'application': False,
}
