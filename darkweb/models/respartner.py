from odoo import models, fields, api

class respartner(models.Model):
    _inherit = 'res.partner'
    _description = 'ResPartner'

    is_customer = fields.Boolean(string='Is Customer')
    point = fields.Integer(string='Point')
    level = fields.Char(string='Level')