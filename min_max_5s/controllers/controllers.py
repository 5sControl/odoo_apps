# -*- coding: utf-8 -*-
# from odoo import http


# class MinMax5s(http.Controller):
#     @http.route('/min_max_5s/min_max_5s', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/min_max_5s/min_max_5s/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('min_max_5s.listing', {
#             'root': '/min_max_5s/min_max_5s',
#             'objects': http.request.env['min_max_5s.min_max_5s'].search([]),
#         })

#     @http.route('/min_max_5s/min_max_5s/objects/<model("min_max_5s.min_max_5s"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('min_max_5s.object', {
#             'object': obj
#         })
