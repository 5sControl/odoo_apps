from odoo import http

import json

from odoo.http import request

from .utils.utils import route, send


class MinMaxController(http.Controller):

    @route('/min_max/all_items')
    def get_products(self, **kwargs):
        """Sends a list of all products"""
        products = request.env['product.product'].sudo().search([])
        product_data = []
        for product in products:
            product_data.append({
                'id': product.id,
                'name': product.name,
            })

        return send({'data': product_data})

    @route('/min_max/ping')
    def ping(self):
        return send({'success': True})

    @route('/min_max/send_message', methods=['POST'])
    def send_message(self, **kwargs):
        """Sends a message to selected minmax users"""

        data = json.loads(request.httprequest.data.decode('utf-8'))
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
        print(message)
        return send({'success': True})
