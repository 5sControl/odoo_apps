from odoo import http

import json

from odoo.http import request


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
        return json.dumps(product_data, content_type="application/json")

    @http.route('/min_max/ping', type='http', auth='public', csrf=False)
    def ping(self):
        return json.dumps({'success': True}, content_type="application/json")

    @http.route('/min_max/send_message', type='http', auth='public', methods=['POST'], csrf=False)
    def send_message(self):
        body = request.httprequest.data
        data = json.loads(body)
        message = data.get('message', '')
        print(message)
        user_5controlS = request.env['res.users'].sudo().search([('login', '=', '5controlS')], limit=1)
        admin_user = request.env['res.users'].sudo().search([('login', '=', 'admin')], limit=1)

        if user_5controlS and admin_user:
            channel = request.env['mail.channel'].sudo().search([
                ('channel_partner_ids', 'in', [user_5controlS.partner_id.id, admin_user.partner_id.id]),
                ('channel_type', '=', 'chat')
            ], limit=1)
            if not channel:
                channel = request.env['mail.channel'].sudo().create({
                    'channel_partner_ids': [(6, 0, [user_5controlS.partner_id.id, admin_user.partner_id.id])],
                    'public': 'private',
                    'channel_type': 'chat',
                })
            channel.sudo().message_post(body=message, author_id=user_5controlS.partner_id.id, message_type="comment")
            return json.dumps({'success': True}, content_type="application/json")
        return json.dumps({'success': False}, content_type="application/json")




