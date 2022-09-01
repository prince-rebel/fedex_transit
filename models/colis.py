from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError



class fedex_transit_colis(models.Model):
    _name = 'fedex.colis'
    _description = 'fedex_colis'

    add_date  = fields.Date(string="Date d'arrivée ", default=datetime.today())
    NumLta  = fields.Char(string ='Numéra LTA ')
    Poids  = fields.Integer(string='Poids ')
    Transporteur = fields.Many2one(string='Transporteur', comodel_name='fedex.transporteur')
    coli_ids = fields.Many2many(
    comodel_name='fedex.colis'
    )

    # @api.constrains('NumLta')
    # def _check_lta(self):
    #     for record in self:
    #         if record.NumLta.values:
    #             raise ValidationError("Ce Numero LTA existe déja")

