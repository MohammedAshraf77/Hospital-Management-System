from odoo import fields, models

class CuSalesOrder(models.Model):

    # _name = 'hospital app'
    # _description = 'Hospital Management'

    _inherit = 'sale.order'  # وراثة نموذج sale.order بدون إنشاء نموذج جديد



    test01 = fields.Char(string="Test 01")
    test02 = fields.Char(string="Test 2")
