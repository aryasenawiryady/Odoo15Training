from odoo import models, fields, api

class Supp(models.Model):
    _name = 'darkweb.supplier'
    _description = 'Supplier'

    name = fields.Char(string='Company Name')
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    weapon_id = fields.Many2many(comodel_name='darkweb.weapon', string='Weapons')
    image = fields.Image(string='-------->')