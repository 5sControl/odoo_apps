# -*- coding: utf-8 -*-
{
    "name": "Operation View",
    "summary": """
    A tool to improve production efficiency in both qualitative and quantitative terms. Allows the enterprise manager to:

    """,
    "description": """    
    """,
    'author': "5sControl",
    "website": "https://5controls.com/",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": [
        "base",
        "mrp",
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/data.xml',
    ],
    'images': ['static/description/banner.gif'],
    "application": True,
    'auto_install': False,
    "development_status": "Beta",
    "license": "LGPL-3",
}
