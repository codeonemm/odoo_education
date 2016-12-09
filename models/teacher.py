from openerp import models, api, fields, _


class teacher(models.Model):

    _inherit = "hr.employee"
    
    email = fields.Char("Email")
    phone = fields.Char("Phone")
    teacher = fields.Boolean("Teacher", domain=[('teacher', '=', True)])
