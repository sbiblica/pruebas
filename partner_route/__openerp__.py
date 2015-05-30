# -*- coding: utf-8 -*-
######################################################################
#
#  Note: Program metadata is available in /__init__.py
#
######################################################################


{
    "name" : "Rutas Visitador",
    "version" : "1.0",
    "author" : '',
    "summary": "Permite ver las Rutas y Cartera de clientes",
    "description" : """
Lista toda la cartera de clientes por Rutas y el cliente que tiene Cuenta por Cobrar.
""",
    'maintainer': 'Miguel Chuga',
    'website': 'odoo.com',
    "category": 'Accounting & Finance',
    "images" : [],
    "depends" : ["base","account_accountant"],
    "data" : [
              'partner_ruta_customer.xml',
              'catalogos_view.xml',
              'partner_view.xml',
              'security/ir.model.access.csv',
    ],
    "test" : [
    ],
    "auto_install": False,
    "application": False,
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

