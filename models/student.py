from openerp import models, api, fields, _


class student(models.Model):
    _inherit = "hr.employee"
    
    father_name = fields.Char("Father Name")
    nrc = fields.Char("NRC No")
    nation = fields.Many2one("nation" ,"Nationality", select=True)
    pob = fields.Char("Place of Birth")
    martial = fields.Selection([('single', 'Single'), ('married', 'Married')], "Martial Status")
    curyear = fields.Many2one("year", "Current Year", select=True)
    religion = fields.Selection([('buddhism', 'Buddhism'), ('christianity', 'Christianity'), ('hinduism', 'Hinduism'), ('islam', 'Islam')], "Religion")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], "Gender")
    major_id = fields.Many2one("major", "Major", select=True)
    
    high_school_id = fields.Char("High School ID")
    high_school_score = fields.Float("High School Score")
    
    student = fields.Boolean("Student", domain=[('student', '=', True)])
    
    attachment_ids = fields.Many2many("ir.attachment", string="Attachments")
    
class year(models.Model):
    _name = "year"
    
    year = fields.Char("Current Year", required=True, select=True)    

