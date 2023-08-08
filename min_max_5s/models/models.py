# -*- coding: utf-8 -*-
from odoo import models, fields


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