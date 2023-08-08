import requests

from odoo import models, fields, api


class ExternalServiceConnection(models.Model):
    _name = 'min_max.connection'
    _description = 'Connection'

    name = fields.Char(string='Name', required=True)
    url = fields.Char(string='URL', required=True)
    username = fields.Char(string='Username', required=True)
    password = fields.Char(string='Password', required=True)


class Items(models.Model):
    _name = 'min_max.items'
    _description = 'Items'

    name = fields.Char(string='Name')
    object_type = fields.Char(string='Object Type')
    status = fields.Char(string='Status')
    current_stock_level = fields.Integer(string='Current Stock Level')

    @api.model
    def update_items_from_api(self):
        url = "https://40da-134-17-26-206.ngrok-free.app/api/inventory/items/"
        response = requests.get(url)

        if response.status_code == 200:
            items_data = response.json()

            for item_data in items_data:
                self.create({
                    'name': item_data.get('name'),
                    'object_type': item_data.get('object_type'),
                    'status': item_data.get('status'),
                    'current_stock_level': item_data.get('current_stock_level')
                })
