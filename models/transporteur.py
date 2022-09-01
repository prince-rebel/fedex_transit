from odoo import models, fields, api


class fedex_transit_transporteur(models.Model):
    _name = 'fedex.transporteur'
    _description = 'fedex_transporteur'

    name = fields.Char(help='Transporteur')