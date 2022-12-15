from odoo import http
from odoo.http import request


class ToolsControl(http.Controller):
    @http.route('/tools/get_all_alerts', auth='user', type='json')
    def all_alerts(self, **kw):
        # session_id = http.request.env['ir.http'].sudo().search([])
        # print(session_id)
        alert_rec = http.request.env['tools_control.tools_control'].sudo().search([])
        alerts = []
        for rec in alert_rec:
            alerts.append({
                'action': rec.action,
                'date': rec.date,
                'area': rec.area,
                'photo': rec.photo,
            })
        print()
        return alerts

    @http.route('/tools/create_alert', auth='user', type='json')
    def create(self, **rec):
        if http.request.render:
            if rec['action']:
                vals = {
                    'action': rec['action'],
                    'date': rec['date'],
                    'area': rec['area'],
                    'photo': rec['photo'],
                }
                new_alert = request.env['tools_control.tools_control'].sudo().create(vals)
                args = {'success': True, 'message': 'Success', 'ID': new_alert.id}
        return args

    @http.route('/tools/ping', type='json', auth='public')
    def ping(self):
        return {'success': True}
