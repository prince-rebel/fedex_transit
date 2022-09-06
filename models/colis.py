from email.mime import image
from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError



class fedex_transit_colis(models.Model):
    _name = 'fedex.colis'
    _inherit =['mail.thread','mail.activity.mixin']

    _description = 'fedex_colis'


    # add_date  = fields.Date(string="Date d'arrivée ", default=datetime.today())
    Lta_id  = fields.Many2one(string="Numero LTA",comodel_name='fedex.manifeste',required=True)
    NumColis = fields.Integer(string='Numbero Colis ',required=True)
    Poids  = fields.Integer(string='Poids du manifeste ',required=True)
    # Transporteur = fields.Many2one(string='Transporteur', comodel_name='fedex.transporteur')
    Destinateur  = fields.Many2one(string='Destinateur', comodel_name='res.partner',required=True)
    NbrColis  = fields.Float(string="Nombre de colis",  default='1',required=True)
    Description = fields.Text(string='Description',required=True)
    ValeurColis  = fields.Float(string='Valeur du colis')
    StatusColis= fields.Many2one(string=' Status', comodel_name='fedex.statut_colis')
    ModeSortie_id= fields.Many2one(string=' Mode de Sortie', comodel_name='fedex.modesortie')
    Ref = fields.Char(string='Reférence')
    Date_de_sortie = fields.Date(string="Date d'arrivée ", default=datetime.today())

    ImageColis  = fields.Binary("image du colis")

    # @api.constrains('NumLta')
    # def _check_lta(self):
    #     for record in self:
    #         if record.NumLta.values:
    #             raise ValidationError("Ce Numero LTA existe déja")

