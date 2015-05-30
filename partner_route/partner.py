# -*- encoding: utf-8 -*-

from openerp.osv import osv, fields
import datetime
import time

class res_partner(osv.osv):
    _inherit = 'res.partner'

    def _departamento(self, cr, uid, ids, field_name, arg, context):
        result = {}

        for cliente in self.pool.get('res.partner').browse(cr, uid, ids):

            if cliente.municipio_id:
                result[cliente.id] = cliente.municipio_id.departamento_id.id

        return result

    _columns = {
        'municipio_id': fields.many2one('mc.municipios', 'Municipio'),
        'departamento_id': fields.function(_departamento, type='many2one', obj="mc.departamentos", method=True, string='Departamento'),
    }


res_partner()
