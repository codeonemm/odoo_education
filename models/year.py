from openerp import models, api, fields, _

class student_year(models.Model):
    
    _name = "student.year"
    
    name = fields.Char("Current Year", required=True, select=True)
