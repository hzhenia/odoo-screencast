# -*- coding: utf-8 -*-
{
    'name': "holidays",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check <odoo>/addons/base/module/module_data.xml of the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["base", "website", "web", "sale", "website_sale"],
    'data': [
        "security/ir.model.access.csv",

        "data/menu.xml",
        "views/holiday.xml",

        "views/website.xml",
        "views/snippets.xml",
    ],

    'demo': ["data/holidays_demo.xml"],

    'tests': [
    ],
}
