# -*- coding: utf-8 -*-
{
    'name': "room_booking",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Agisna Ihatec",
    'website': "http://www.ihatec.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': "LGPL-3",
    'application': True,
    'installable': True,
    'sequence': 10,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu_item.xml',
        'views/templates.xml',
        'views/room_list.xml',
        'views/room_status.xml',
        'views/room_book.xml',
        'views/room_hours.xml',
        'views/book_hours.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
