from xlsxwriter.contenttypes import defaults

from odoo import models, fields, api, _

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'

    name = fields.Char(string='Appointment Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string="Patient")
    date_appointment = fields.Date(string="Date")
    note = fields.Text(string="Note")
    state = fields.Selection([
        ('draft', 'Draft'), ('confirmed', 'Confirmed'), ('ongoing', 'Ongoing'), ('done', 'Done'),
        ('cancel', 'Cancelled'),

    ], default='draft', tracking=True)

    appointment_line_ids = fields.One2many(
        'hospital.appointment.line','appointment_id', string="lines"
    )

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('appointment_seq') or _('New')
        return super(HospitalAppointment, self).create(vals)


    def action_confirm(self):
        for rec in self:
            print("button is clicked",)
            rec.state = 'confirmed'

    # def action_draft(self):
    #     for rec in self:
    #         print("button is clicked",)
    #         rec.state = 'draft'

    def action_ongoing(self):
        for rec in self:
            print("button is clicked", )
            rec.state = 'ongoing'

    def action_done(self):
        for rec in self:
            print("button is clicked", )
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            print("button is clicked", )
            rec.state = 'cancel'



class HospitalAppointmentLine(models.Model):
    _name = 'hospital.appointment.line'
    _description = 'Hospital Appointment Line'

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
    product_id = fields.Many2one('product.product', string="Product")
    qty = fields.Float(string="Quantity")
