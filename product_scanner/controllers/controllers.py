# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from werkzeug.wrappers import Response
import json


class ScanerControl(http.Controller):
    @http.route('/scaner/products', type='http', auth='public', methods=['GET'])
    def get_products(self, **kwargs):
        products = request.env['product.product'].sudo().search([])
        product_data = []
        for product in products:
            product_data.append({
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.list_price,
                'default_code': product.default_code,
                'barcode': product.barcode,
                'responsible': product.responsible_id.name if product.responsible_id else None,
            })
        return json.dumps(product_data)

    @http.route('/scaner/ping', type='json', auth='public')
    def ping(self):
        return {'success': True}

    @http.route('/scanner/scan', type='http', auth='public', methods=['POST'], csrf=False)
    def scan_product(self, **post):
        body = request.httprequest.data
        data = json.loads(body)
        barcode = data.get('barcode')

        product = request.env['product.product'].sudo().search([('barcode', '=', barcode)], limit=1)

        if product:
            response_data = {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.list_price,
                'default_code': product.default_code,
                'barcode': product.barcode,
                'responsible': product.responsible_id.name if product.responsible_id else None,
            }
            return Response(json.dumps(response_data), status=200, mimetype='application/json')
        else:
            return Response(json.dumps({'success': False}), status=200, mimetype='application/json')
