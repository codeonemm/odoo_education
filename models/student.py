from openerp import models, api, fields, _


class student(models.Model):
    _name = "student.student"
    
    name = fields.Char("Name", required=True, select=True)
    date_of_birth = fields.Date("Date Of Birth", required=True)
    father_name = fields.Char("Father Name", required=True)
    nrc = fields.Char("NRC No", required=True)
    phone = fields.Char("Phone No", required=True)
    address = fields.Char("Address", required=True)
    nation = fields.Many2one("nation" ,"Nationality", required=True, select=True)
    race = fields.Selection([('kachin', 'Kachin'), ('kayah', 'Kayah'), ('kayin', 'Kayin'), ('chin', 'Chin'), ('mon', 'Mon'), ('rakhine', 'Rakhine'), ('shan', 'Shan'), ('yangon', 'Yangon'), ('mandalay', 'Mandalay'), ('ayeyarwady', 'Ayeyarwady'), ('sagaing', 'Sagaing'), ('magway', 'Magway'), ('bago', 'Bago'), ('tanintharyi', 'Tanintharyi')], "Race", required=True)
    pob = fields.Char("Place of Birth", required=True)
    martial = fields.Selection([('single', 'Single'), ('married', 'Married')], "Martial Status", required=True)
    curyear = fields.Char("Current Year", required=True)
    religion = fields.Selection([('buddhism', 'Buddhism'), ('christianity', 'Christianity'), ('hinduism', 'Hinduism'), ('islam', 'Islam')], "Religion", required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], "Gender", required=True)
    email = fields.Char("Email", required=True)
    fees = fields.Float("Fees", required=True)
    major_id = fields.Many2one("major", "Major", required=True, select=True)
    state = fields.Selection([("draft", "Draft"), ("confirm", "Confirm"), 
				("pay", "Pay"), ("book_receive", "Book Receive"), ("done", "Done")], "State", readonly=True)
    
    high_school_id = fields.Char("High School ID")
    high_school_score = fields.Float("High School Score")
    
    attachment_ids = fields.Many2many("ir.attachment", string="Attachments")
    
    
    _defaults = {
	'state': 'draft'
    }
