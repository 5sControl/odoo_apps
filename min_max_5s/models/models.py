import requests
import logging

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

    def fetch_data_from_external_service(self):
        url = "https://40da-134-17-26-206.ngrok-free.app/api/inventory/items/"
        response = requests.get(url)
        data = response.json()
        print(data)
        for item_data in data:
            self.create({
                'name': item_data.get('name'),
                'object_type': item_data.get('object_type'),
                'status': item_data.get('status'),
                'current_stock_level': item_data.get('current_stock_level')
            })

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        # Вызываем метод fetch_data_from_external_service перед чтением записей
        self.fetch_data_from_external_service()
        return super(Items, self).search(args, offset=offset, limit=limit, order=order, count=count)

