import json
from odoo import http, models, fields
from odoo.http import request

class Darkweb(http.Controller):
    @http.route('/darkweb/getWeapon', auth='public', method=['GET'])
    def getWeapon(self, **kw):
        items = request.env['darkweb.weapon'].search([])
        a = []

        for b in items:
            a.append({
                'weapon_name': b.name,
                'selling_price': b.selling_price,
                'stock': b.stock
            })
        return json.dumps(a)

    