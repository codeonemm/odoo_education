from openerp import models, api, fields, _


class subject(models.Model):
    _name = "subject"
    
    major_id = fields.Many2one("major", required=True, ondelete='cascade')
    name = fields.Char("Subject Name", required=True, select=True)
    description = fields.Text("Description")

class major(models.Model):
    _name = "major"
    
    name = fields.Char("Major Name", required=True, select=True)
    subject_ids = fields.One2many("subject", "major_id", "Subjects")
