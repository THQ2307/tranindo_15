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
        'sale',
        'sale_stock',
        'account',
        'stock',
    ],
    'data': [
        'views/account_move_views.xml',
        'views/sale_order_views.xml',
        'report/c5_report.xml',
        'e_faktur/e_faktur_account_move_view.xml',
        'e_faktur/e_faktur_res_partner_view.xml',
    ],
    'css': [],
    'js': [],
    'installable': True,
    'active': False,
    'application': False,
}
