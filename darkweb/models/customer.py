from odoo import models, fields, api

class Customer(models.Model):
    _inherit = 'res.partner'
    _description = 'Contact'

    point = fields.Integer(string='Point')
    level = fields.Char(string='Level')