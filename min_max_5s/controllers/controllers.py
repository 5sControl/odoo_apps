from odoo import http

import json

from odoo.http import request


class MinMaxController(http.Controller):

    @http.route('/min_max/all_items', type='json', auth='public', methods=['GET'])
    def get_products(self, **kwargs):
        products = request.env['product.product'].sudo().search([])
        product_data = []
        for product in products:
            product_data.append({
                'id': product.id,
                'name': product.name,
            })
        return json.dumps(product_data)

    @http.route('/min_max/ping', type='json', auth='public', csrf=False)
    def ping(self):
        return json.dumps({'success': True})

    @http.route('/min_max/send_message', type='json', auth='public', methods=['POST'], csrf=False)
    def send_message(self):
        body = request.httprequest.data
        data = json.loads(body)
        message = data.get('message', '')
        last_connection = request.env['min_max.connection'].sudo().search([], order='id desc', limit=1)

        for user in last_connection.notification_users:
            if user.partner_id:
                bot_user = request.env.ref('base.user_root')
                channel_name = f"OdooBot, {user.name}"

                if user and bot_user:
                    channel = request.env['mail.channel'].sudo().search([
                        ('name', '=', channel_name),
                        ('channel_type', '=', 'chat')
                    ], limit=1)

                    channel.sudo().message_post(body=message, author_id=bot_user.partner_id.id, message_type="comment")

        return json.dumps({'success': True})
