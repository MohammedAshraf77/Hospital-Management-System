from odoo import fields, models, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Master'

    name = fields.Char(
        string="Name",
        required=True,
        tracking=True
    )
    ref = fields.Char(
        default='New',
        readonly=True
    )


    date_of_birth = fields.Date(
        string='DOB',
        tracking=True
    )
    # assign_to_id = fields.Many2one('res.partner')

    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')],
        string="Gender",
        tracking=True
    )
    state = fields.Selection([
        ('draft','Draft'),('pending','Pending'),('closed','Closed')
    ],default='draft')

    tag_ids = fields.Many2many(
        'patient.tag', 'patient_tag_rel', 'patient_id', 'tag_id', string="Tags"
    )

    tag_dummy_ids = fields.Many2one(
        'patient.tag', string="Tags"
    )
    # product_ids = fields.Many2one(
    #     'product.product', string="Products"
    # )
    #


    @api.model
    def create(self,vals):
        res = (super(HospitalPatient,self).create(vals))
        if res.ref == 'New':
           res.ref= self.env['ir.sequence'].next_by_code('patient_seq')
           return res