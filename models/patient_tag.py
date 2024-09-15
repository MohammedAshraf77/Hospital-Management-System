from odoo import fields, models, api

class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'
    _order = 'sequence,id'


    name = fields.Char(
        string="Name",
        required=True,
    )
    ref = fields.Char(
        default='New',
        readonly=True
    )


    date_of_birth = fields.Date(
        string='DOB',
    )
    sequence = fields.Integer(default=10)
    # assign_to_id = fields.Many2one('res.partner')

    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')],
        string="Gender",
    )
    # state = fields.Selection([
    #     ('draft','Draft'),('pending','Pending'),('closed','Closed')
    # ],default='draft')


