# -*- coding: utf-8 -*-
{
    'name': "Fedex_Transit",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Neurones Technologie",
    'website': "https://www.neuronestechnologie.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    # 'category': 'Transit',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/etatSoumission.xml',
        'views/modeSortie.xml',
        'views/regime.xml',
        'views/statusColis.xml',
        'views/statusTransit.xml',
        'views/transporteur.xml',
        'views/typeSoumission.xml',
        'views/manifeste.xml',
        'views/eclatement.xml',
        'views/articles.xml',
        'views/retourClient.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
