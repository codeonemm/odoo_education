from openerp import models, api, fields, _

class nation(models.Model):
    
    _name = "nation"
    
    name = fields.Char("Nation Name", required=True, select=True)    
