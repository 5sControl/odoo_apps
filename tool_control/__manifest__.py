{
    'name': "Tools control",
    'summary': """
        Tool Control app and Tool Control ERP is a system that helps to keep the workplace, documentation and team relationships in order. 
    """,
    'description': """
        Everything is in its place 
        An employee used a tool but forgot to return or damaged it? No more lost inventory, no more lost profits!  
        Tool Control ERP is a convenient repository for reports created in ToolControl mobile application. 
        
        The ToolControl app takes a photo of a worker at the moment when she/he takes a tool. 
        Images are sent to Tool Control ERP, where you can always check who took this or that tool last and contact that person directly.  
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
        'views/templates.xml',
        'views/tools_control_menu.xml',
    ],
    'application': True,
    'license': 'LGPL-3'
}
