# -*- coding: utf-8 -*-
from openerp import models, fields, api 


class stock_picking(models.Model):
    _inherit = 'stock.picking'

    new_location_id = fields.Many2one(
        'stock.location', 'Source Location',
        readonly=True,
        states={
            'draft': [('readonly', False)],
            'waiting': [('readonly', False)],
            'confirmed': [('readonly', False)],
            },  
        help="Sets a location if you produce at a fixed location. This can be a partner location if you subcontract the manufacturing operations. This will be the default of the asociated stock moves.")
    new_location_dest_id = fields.Many2one(
        'stock.location', 'Destination Location',
        readonly=True,
        states={
            'draft': [('readonly', False)],
            'waiting': [('readonly', False)],
            'confirmed': [('readonly', False)],
            },  
        help="Location where the system will stock the finished products. This will be the default of the asociated stock moves.")

    @api.one
    def update_locations(self):
        vals = { 
            'location_id': self.new_location_id.id,
            'location_dest_id': self.new_location_dest_id.id
            }   
        self.move_lines.write(vals)


#from openerp import models, fields
#
#class stock_picking(models.Model):
#    _inherit = "stock.picking"
#
#    header_location_id = fields.Many2one('stock.location')
#    header_location_dest_id = fields.Many2one('stock.location')
#
#stock_picking()
#
#class stock_move(models.Model):
#    _inherit = "stock.move"
#
#    def on_change_location_id(self, cr, uid, location_id, parent_location_id, context):
#        if not parent_location_id:
#            return {'value': {'location_id': context}}
#        else:
#            return {'value': {}}
#
#    def on_change_location_dest_id(self, cr, uid, location_dest_id, parent_location_dest_id, context):
#        if not parent_location_dest_id:
#            return {'value': {'location_dest_id': context}}
#        else:
#            return {'value': {}}
#
#    def onchange_move_type(self, cr, uid, ids, type, context=None):
#        """ On change of move type gives sorce and destination location.
#        @param type: Move Type
#        @return: Dictionary of values
#        """
#        if type == 'internal':
#            return {'value':{}}
#        else:
#            return super(stock_move, self).onchange_move_type(cr, uid, ids, type, context)
#
#def _default_location_destination(self, cr, uid, context=None):
#        """ Gets default address of partner for destination location
#        @return: Address id or False
#        """
#
#        if context.get('picking_type') != 'internal':
#            return super(stock_move, self)._default_location_destination(cr, uid, context)
#
#        return False
#
#
#    def _default_location_source(self, cr, uid, context=None):
#        """ Gets default address of partner for source location
#        @return: Address id or False
#        """
#
#        if context.get('picking_type') != 'internal':
#            return super(stock_move, self)._default_location_source(cr, uid, context)
#
#        return False
#
#    _defaults = {
#        'location_id': _default_location_source,
#        'location_dest_id': _default_location_destination,
#    }
#
#stock_move()
