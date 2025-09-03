from odoo import models,fields

class estatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Description'

    name = fields.Char(required=True)