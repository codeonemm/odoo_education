from openerp import models, api, fields, _


class student_enroll(models.Model):
    
    _name = "student.enroll"
    
    name = fields.Char("Name")
    student_id = fields.Many2one('hr.employee', string="Student", domain=[('student', '=', True)], required=True)
    teacher_id = fields.Many2one('hr.employee', string="Responsible Person", domain=[('teacher', '=', True)], required=True)
    fees = fields.Float("Fees", required=True)
    state = fields.Selection([("draft", "Draft"), ("confirm", "Confirm"),
				("pay", "Pay"), ("book_receive", "Book Receive"), ("done", "Done")], "State", readonly=True)

    _defaults = {
	'state': 'draft'
    }
    
    def confirm(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state': 'confirm'})
        return True
	
    def pay(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state': 'pay'})
        return True
	
    def book_receive(self, cr, uid, ids, context=None):
	self.write(cr, uid, ids, {'state': 'book_receive'})
	return True
	
    def done(self, cr, uid, ids, context=None):
	self.write(cr, uid, ids, {'state': 'done'})
	return True		
	
    @api.model
    def create(self, vals):
	if self.name == False:
            name = self.pool.get('ir.sequence').get(self.env.cr, self.env.uid,
                                                       'student.enroll', context=self._context) or "/"
	    vals["name"] = name
	return super(student_enroll, self).create(vals)
