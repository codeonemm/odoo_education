from openerp import models, api, fields, _


class teacher(models.Model):

    _inherit = "hr.employee"
    
    teacher = fields.Boolean("Teacher", domain=[('teacher', '=', True)])
