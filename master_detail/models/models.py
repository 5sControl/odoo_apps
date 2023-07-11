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

    REPAIR_WORKS_SELECTION = [
        ('1', 'Trūkimo vietos užtaisymas, kai gylis iki 2,0 m., plieninio vamzdžio skersmuo'),
        ('2', 'Trūkimo vietos užtaisymas, kai gylis iki 2,5 m., plieninio vamzdžio skersmuo'),
        ('3', 'Trūkimo vietos užtaisymas, kai gylis iki 3,0 m., plieninio vamzdžio skersmuo'),
        ('4', 'Trūkimo vietos užtaisymas, kai gylis iki 4,0 m., plieninio vamzdžio skersmuo'),
        ('5', 'Trūkimo vietos užtaisymas, kai gylis iki 5,0 m., plieninio vamzdžio skersmuo'),
        ('6', 'Trūkimo vietos užtaisymas, kai gylis iki 6,0 m., plieninio vamzdžio skersmuo'),
        ('7', 'Vamzdžio movos sandarinimas, kai gylis iki 2,0 m., ketinio vamdžio skersmuo, mm'),
        ('8', 'Vamzdžio movos sandarinimas, kai gylis iki 2,5 m., ketinio vamdžio skersmuo, mm')
    ]

    diameter_selection = [
        ('80', '80'),
        ('100', '100'),
        ('125', '125'),
        ('150', '150'),
        ('200', '200'),
        ('250', '250'),
        ('300', '300'),
        ('350', '350'),
        ('400', '400'),
        ('500', '500'),
        ('600', '600'),
        ('700', '700'),
        ('800', '800'),
    ]

    name = fields.Char(string='Act Number')
    description = fields.Text(string='Description')
    contract_id = fields.Many2one('contract.contract', string='Contract')
    photos = fields.Many2many('ir.attachment', string='Photos')
    address = fields.Char(string='Address')
    master_id = fields.Many2one('hr.employee', string='Master')
    quantity = fields.Float(string='Quantity')
    unit = fields.Char(string='Unit of measurement')
    unit_price = fields.Float(string='Unit Price')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    date_receipt_work = fields.Date(string='Date of receipt of work')
    coverage_type = fields.Char(string='Coverage Type')
    preliminary_dismantling = fields.Integer(string='Ardomas preliminarus dangų plotas')
    employers_ids = fields.Many2many('hr.employee', string='Employees', relation='act_employers_rel')
    phone_number = fields.Text(string='Phone Number')
    precipitation_date = fields.Date(string='Precipitation Date')
    description_precipitation = fields.Text(string='Description of precipitation')
    permission_excavate = fields.Selection(selection=PERMISSION_SELECTION, string='Permission to excavate')
    diameter = fields.Selection(selection=diameter_selection, string='Pipe Diameter ⌀')
    repair_works = fields.Selection(selection=REPAIR_WORKS_SELECTION, string='Repair Works')

