from odoo import http

import json

from odoo.http import request, Controller


class MinMaxController(http.Controller):

    @http.route('/min_max/all_items', type='http', auth='public', methods=['GET'])
    def get_products(self, **kwargs):
        products = request.env['product.product'].sudo().search([])
        product_data = []
        for product in products:
            product_data.append({
                'id': product.id,
                'name': product.name,
            })
        return json.dumps(product_data)

    @http.route('/min_max/ping', type='http', auth='public')
    def ping(self):
        return json.dumps({'success': True})
