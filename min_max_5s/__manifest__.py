# -*- coding: utf-8 -*-
{
    'name': "MinMax5s",

    'summary': """
        The module allows you to connect to the 5S inventory control system""",

    'description': """
        The module allows you to connect to the 5S inventory control system
    """,

    'author': "5sControl",
    "website": "https://5controls.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        # 'views/report_dashboard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/banner.gif'],
    "application": True,
    'auto_install': False,
    "development_status": "Beta",
    "license": "LGPL-3",
}
