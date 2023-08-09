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
    def search(self, args, offset=0, limit=None, order=None, count=False):
        connection_record = self.env['min_max.connection'].search([], limit=1)

        if connection_record:
            url = f'{connection_record.url}/api/inventory/items/'
            response = requests.get(url)
            data = response.json()

            records = self.env['min_max.items']
            for item_data in data:
                new_record = self.env['min_max.items'].create({
                    'name': item_data.get('name'),
                    'object_type': item_data.get('object_type'),
                    'status': item_data.get('status'),
                    'current_stock_level': item_data.get('current_stock_level')
                })
                records += new_record

            return records
        else:
            return super(Items, self).search(args, offset=offset, limit=limit, order=order, count=count)

