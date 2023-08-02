# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TitlePost(models.Model):
    _name = 'connector_operations.title'
    _rec_name = 'link'

    link = fields.Char(string='Link')
    description = fields.Char(string='Description')

