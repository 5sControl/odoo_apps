from odoo import http
import json


class ItemsController(http.Controller):

    @http.route('/get_items_data', type='json', auth='user')
    def get_items_data(self):
        # Здесь получите данные из внешнего сервиса (например, с помощью библиотеки requests)
        external_data = [...]

        return {
            'data': external_data,
            'view_id': self.env.ref('your_module.view_items_tree').id,
        }


class ReportsController(http.Controller):

    def get_reports_data(self):
        # Ваш код для получения данных по внешнему запросу
        data = [...]  # Полученные данные
        return {'data': data}
