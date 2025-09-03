from odoo import models, fields

class estatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Description'

    name = fields.Char(required=True)