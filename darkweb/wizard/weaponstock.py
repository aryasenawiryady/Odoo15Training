from odoo import api, fields, models

class WeaponStock(models.TransientModel):
    _name = 'darkweb.weaponstock'

    weapon_id = fields.Many2one(comodel_name='darkweb.weapon', string='Weapon Name', required=True)
    total = fields.Integer(string='Add Stock', required=False)

    def button_weapon_stock(self):
        for line in self:
            self.env['darkweb.weapon'].search([('id', '=', line.weapon_id.id)]).write(
                {'stock': line.weapon_id.stock +  line.total}
            )