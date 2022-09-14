from odoo import models, fields, api

class darkweb(models.Model):
    _name = 'darkweb.itemstype'
    _description = 'items type'

    name = fields.Selection([
        ('primary weapons', 'Primary Weapons'),
        ('secondary weapons', 'Secondary Weapons'),
        ('melee weapons', 'Melee Weapons'),
        ('explosive','Explosive')
        ], string='Items Type')
    
    item_type = fields.Char(string='Items ID')

    @api.onchange('name')
    def _onchange_items_type(self):
        if self.name == 'primary weapons':
            self.item_type = 'G1'
        elif self.name == 'secondary weapons':
            self.item_type = 'G2'
        elif self.name == 'melee weapons':
            self.item_type = 'M1'
        elif self.name == 'explosive':
            self.item_type = 'E1'

    weapon_ids = fields.One2many(comodel_name='darkweb.weapon',
                                inverse_name='items_type_id',
                                string='Weapon List')
    
    total_items = fields.Char(compute='_compute_total_items', 
                            string='Total Items')

    @api.depends('weapon_ids')
    def _compute_total_items(self):
        for record in self:
            a = self.env['darkweb.weapon'].search([('items_type_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.total_items = b
            record.list = a
    
    list = fields.Char(string='Items List')

    _sql_constraints = [
        ('item_type_unique', 'unique (item_type)', 'Items ID cannot be duplicated.')
    ]
