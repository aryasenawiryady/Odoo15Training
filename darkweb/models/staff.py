from odoo import models, fields, api

class Staff(models.Model):
    _name = 'darkweb.staff'
    _description = 'Staff'

    name = fields.Char(string='Name')
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')
    birthday = fields.Date(string='Birthday')
    gender = fields.Selection([
            ('male','Male'),('female','Female')], string='Gender')

class Cashier(models.Model):
    _name = 'darkweb.cashier'
    _inherit = 'darkweb.staff'
    _description = 'Cashier'

    cashier_id = fields.Char(string='Cashier ID')

class CleaningService(models.Model):
    _name = 'darkweb.cleaningservice'
    _inherit = 'darkweb.staff'
    _description = 'Cleaning Service'

    cleaningservice_id = fields.Char(string='Cleaning Service ID')

class Security(models.Model):
    _name = 'darkweb.security'
    _inherit = 'darkweb.staff'
    _description = 'Security'

    security_id = fields.Char(string='Security ID')

