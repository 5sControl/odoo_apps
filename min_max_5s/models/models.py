import requests

from odoo.exceptions import ValidationError

from datetime import datetime

from odoo import models, fields, api


class ExternalServiceConnection(models.Model):
    _name = 'min_max.connection'
    _description = 'Connection'

    name = fields.Char(string='Name', required=True)
    url = fields.Char(string='URL', required=True)
    username = fields.Char(string='Username', required=True)
    password = fields.Char(string='Password', required=True)
    access_token = fields.Char(string='Access Token', readonly=True)
    is_connected = fields.Boolean(string='Is Connected', compute='_compute_is_connected', store=True)

    @api.depends('access_token')
    def _compute_is_connected(self):
        for record in self:
            record.is_connected = bool(record.access_token)

    @api.model
    def create(self, vals):
        auth_data = {
            "username": vals["username"],
            "password": vals["password"]
        }
        response = requests.post(f"{vals['url']}/auth/jwt/create/", json=auth_data)

        if response.status_code != 200:
            raise ValidationError("Record not created, invalid data entered.")

        token_data = response.json()
        connection = super(ExternalServiceConnection, self).create(vals)
        connection.access_token = token_data.get("access")
        connection.is_connected = True

        return connection


class Items(models.Model):
    _name = 'min_max.items'
    _description = 'Items'

    id = fields.Integer(string='Id item')
    name = fields.Char(string='Name')
    number = fields.Integer(string='Number')
    object_type = fields.Char(string='Object Type')
    status = fields.Char(string='Status')
    current_stock_level = fields.Integer(string='Current Stock Level')
    date_updated = fields.Char(string='Date last updated')

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
                    'number': item_data.get('id'),
                    'name': item_data.get('name'),
                    'object_type': item_data.get('object_type'),
                    'status': item_data.get('status'),
                    'current_stock_level': item_data.get('current_stock_level'),
                    'date_updated': str(item_data.get('date_updated'))
                })
                records += new_record

            return records
        else:
            return super(Items, self).search(args, offset=offset, limit=limit, order=order, count=count)

    @api.model
    def action_item_graph(self, args, offset=0, limit=None, order=None, count=False):
        connection_record = self.env['min_max.connection'].search([], limit=1)
        graph_data = []
        if connection_record:
            id = 0
            item_record = self.env['min_max.items'].browse(args[0])
            if item_record:
                id += item_record.number
            url = f'{connection_record.url}/api/inventory/history/2023-08-09/00:00:00/23:59:00/{id}/'
            headers = {
                'Authorization': f'Bearer {connection_record.access_token}'
            }
            response = requests.get(url, headers=headers)
            data = response.json()
            for report_data in data:
                date_updated = datetime.strptime(report_data.get('start_tracking'), '%Y-%m-%d %H:%M:%S.%f').isoformat()
                if 'extra' in report_data:
                    for extra_data in report_data['extra']:
                        if extra_data.get('itemId') == id:
                            status = extra_data.get('status')
                            graph_data.append({'date_updated': date_updated, 'status': status})
        view_id = self.env.ref('min_max_5s.view_items_graph').id
        action = {
            'name': 'Item Graph',
            'type': 'ir.actions.act_window',
            'view_mode': 'graph',
            'view_id': view_id,
            'context': {'graph_data': graph_data},
        }
        return action


class Reports(models.Model):
    _name = 'min_max.reports'
    _description = 'Reports'

    name = fields.Char(string='Name items')
    count = fields.Integer(string='Count items')
    date_created = fields.Datetime(string='Date create')

    @api.model
    def get_graph_data(self, args, offset=0, limit=None, order=None, count=False):

        connection_record = self.env['min_max.connection'].search([], limit=1)
        if connection_record:
            url = f'{connection_record.url}/api/inventory/history/2023-08-09/00:00:00/23:59:00/'

            headers = {
                'Authorization': f'Bearer {connection_record.access_token}'
            }

            response = requests.get(url, headers=headers)
            data = response.json()
            print(data)

            records = self.env['min_max.reports']
            for report_data in data:
                new_record = self.env['min_max.reports'].create({
                    'name': report_data.get('id'),
                    'count': report_data.get('name'),
                    'date_created': str(report_data.get('start_tracking'))
                })
                records += new_record

            return records
        else:
            return super(Reports, self).search(args, offset=offset, limit=limit, order=order, count=count)
