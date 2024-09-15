{
    'name': 'hospital app',
    'author': 'Mohamed Ashraf Omran',
    'category': 'Healthcare',
    'version': '17.0',
    'depends': ['base', 'sale','mail','product'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/appointment_views.xml',
        'views/appointment_line_views.xml',
        'views/patient_tag_views.xml',
        'views/patient_views.xml',
        'views/base_menus.xml',
        'views/sales_order.xml',



    ],
    'application': True,
    'license': 'LGPL-3',
}
