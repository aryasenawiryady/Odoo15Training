from dataclasses import field
from odoo import models, fields, api

class Weapon(models.Model):
    _name = 'darkweb.weapon'
    _description = 'Weapons'

    name = fields.Char(string='Weapons Name')
    purchase_price = fields.Integer(string='Purchase Price', required=True)
    selling_price = fields.Integer(string='Selling Price', required=True)

    items_type_id = fields.Many2one('darkweb.itemstype',
                                    string='Items Type',
                                    ondelete='cascade')

    supplier_id = fields.Many2many(comodel_name='darkweb.supplier', 
                                    string='Supplier')
            
    stock = fields.Integer(string='Stock')
    image = fields.Image(string='-------->')