# -*- coding: utf-8 -*-
{
    'name': "darkweb",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/itemstype_view.xml',
        'views/weapon_view.xml',
        'views/staff_view.xml',
        'views/cashier_view.xml',
        'views/cleaningservice_view.xml',
        'views/security_view.xml',
        'views/customer_view.xml',
        'views/supplier_view.xml',
        'views/transaction_view.xml',
        'report/report.xml',
        'report/pdf_print.xml',
        'wizard/weaponstock_view.xml'
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
