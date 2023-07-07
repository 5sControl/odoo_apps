from odoo import models, fields


class ProductScanner(models.Model):
    _name = 'product_scanner.product_scanner'

    barcode = fields.Char(string='Barcode', related='product_product.barcode', readonly=True)
    product_template_id = fields.Many2one('product.template', string='Product Template')
