from odoo import models, fields, api


class SafetyControl(models.Model):
    _name = 'safety_control.safety_control'
    _description = 'Safety Control'
    _rec_name = 'device'

    device = fields.Char(string="Device")

    time = fields.Char(string="Time of Report")
    lastTime = fields.Char(string="Time of Report: ")
    image = fields.Binary(
        string="Image",
        store=True,
        attachment=False
    )

    recognitionType = fields.Text()

    personWithoutHelmet = fields.Boolean(string="Person Without Helmet", default=False)
    personWithoutHeadphones = fields.Boolean(string="Person Without Headphones", default=False)
    personWithoutJacket = fields.Boolean(string="Person Without Jacket", default=False)
    personWithoutGloves = fields.Boolean(string="Person Without Gloves", default=False)
    personWithoutMask = fields.Boolean(string="Person Without Mask", default=False)

    @api.model
    def create(self, vals):

        vals['image'] = vals['image'].split(',')[-1]
        vals['device'] = vals['device']['name']

        return super(SafetyControl, self).create(vals)
