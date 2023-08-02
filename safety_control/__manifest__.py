# -*- coding: utf-8 -*-
{
    'name': "Safety Control",
    'summary': """Repository for reports created in Safety Control mobile application""",
    'description': """
        Safety Control is a mobile app that detects use of personal protective equipment by staff before they start working with equipment. It also informs in case of presence in a dangerous zone.  

Safety Control product is based on artificial intelligence technology for analyzing data from video. This helps to detect people and objects at the production site.

When a worker approaches the machine, AI technology detects whether this person is wearing personal protective equipment or not. If not, Safety Control app sends a warning requiring you to wear a protective helmet.

At the same time, Safety Control app takes a photo of the person who neglects safety protocols. The image is saved in Safety Control Odoo, where managers can observe those who violate safety rules and contact them directly.
    """,
    'author': "5sControl",
    'website': "https://eigsoft.com/5scontrol",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/safety_control_menu.xml'
    ],
    'images': ['static/description/images/image1.png'],
    'application': True,
    'license': 'LGPL-3'
}