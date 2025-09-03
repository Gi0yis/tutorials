{
    'name': 'estate',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Gioyis',
    'website': 'http://www.gioyis.pro',
    'category': 'Estate',
    'description': '''
    My first odoo module.
    ''',
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menus.xml'
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3'
}