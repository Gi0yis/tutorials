from odoo import models,fields

class estatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = "Descrition"

    price = fields.Float()
    status = fields.Selection(
        string='Status',
        selection=[
            ('accepted', 'Accepted'),
            ('refused', 'Refused')
        ],
        copy=False
    )
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)