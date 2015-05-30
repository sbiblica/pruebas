# -*- encoding: utf-8 -*-

from openerp.osv import osv, fields
import datetime
  
 

class mc_departamentos(osv.osv):
    _name = 'mc.departamentos'
    _description = 'Departamentos'
    _rec_name = 'nombre'
    _columns = {
        'codigo': fields.char('Codigo', size=5, required=True),
        'nombre': fields.char('Departamento', size=40, required=True),
    }
    _order = 'codigo'
mc_departamentos()

class mc_municipios(osv.osv):
    _name = 'mc.municipios'
    _description = 'Municipios'
    _rec_name = 'nombre'
    _columns = {
        'departamento_id': fields.many2one('mc.departamentos', 'Departamento', required=True),
        'codigo': fields.char('Codigo', size=5, required=True),
        'nombre': fields.char('Municipio', size=40, required=True),
    }
    _order = 'codigo'
mc_municipios()
