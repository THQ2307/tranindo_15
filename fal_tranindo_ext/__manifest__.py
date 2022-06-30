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
        'sale_stock',
        'account',
    ],
    'data': [
        'views/sale_views.xml',
        'views/account_move_views.xml',
        'report/c5_report.xml',
    ],
    'css': [],
    'js': [],
    'installable': True,
    'active': False,
    'application': False,
}
