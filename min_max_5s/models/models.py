# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class min_max_5s(models.Model):
#     _name = 'min_max_5s.min_max_5s'
#     _description = 'min_max_5s.min_max_5s'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
