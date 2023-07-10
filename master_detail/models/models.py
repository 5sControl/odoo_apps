from odoo import models, fields, api


class Contract(models.Model):
    _name = 'contract.contract'
    _description = 'Contracts'

    name = fields.Char(string='Contract Number')
    description = fields.Text(string='Description')
    create_date = fields.Datetime(string='Create Date', readonly=True, default=lambda self: fields.Datetime.now())
    write_date = fields.Datetime(string='Write Date', readonly=True)
    client = fields.Many2one('res.partner', string='Client', domain="[('is_company', '=', True)]")
    subcontractor = fields.Many2one('res.partner', string='Subcontractor', domain="[('is_company', '=', True)]")
    acts_ids = fields.One2many('contract.act', 'contract_id', string='Acts')

    def write(self, values):
        values['write_date'] = fields.Datetime.now()
        return super(Contract, self).write(values)


class Act(models.Model):
    _name = 'contract.act'
    _description = 'Acts'

    PERMISSION_SELECTION = [
        ('permission', 'Have permission'),
        ('no_permission', 'No permission'),
        ('no_record', 'Missing entry')
    ]

    name = fields.Char(string='Act Number')
    description = fields.Text(string='Description')
    contract_id = fields.Many2one('contract.contract', string='Contract')
    photos = fields.Many2many('ir.attachment', string='Photos')
    address = fields.Char(string='Address')
    quantity = fields.Float(string='Quantity')
    unit = fields.Char(string='Unit of measurement')
    unit_price = fields.Float(string='Unit Price')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    coverage_type = fields.Char(string='Coverage Type')
    preliminary_dismantling = fields.Integer(string='Ardomas preliminarus dangų plotas')
    master_ids = fields.Many2many('hr.employee', string='Employees')
    phone_number = fields.Text(string='Phone Number')
    precipitation_date = fields.Date(string='Precipitation Date')
    description_precipitation = fields.Text(string='Description of precipitation')
    permission_excavate = fields.Selection(selection=PERMISSION_SELECTION, string='Permission to excavate')
