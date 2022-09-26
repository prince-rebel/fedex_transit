from email.mime import image
from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError



class fedex_statut_colis(models.Model):
    _name = 'fedex.statut_colis'
    _inherit =['mail.thread','mail.activity.mixin']

    _description = 'statut des colis'

    name  = fields.Char(string ='Status Colis ',required=True)

class fedex_mode_sortie(models.Model):
    _name = 'fedex.modesortie'
    _inherit =['mail.thread','mail.activity.mixin']

    _description = 'Les modes de sorties'

    name = fields.Char(string="Mode de Sortie",required=True)


class fedex_statut_transit(models.Model):
    _name = 'fedex.statut_transit'
    _inherit =['mail.thread','mail.activity.mixin']

    _description = 'statut des transit'

    name  = fields.Char(string ='libellé ',required=True)
     

class fedex_transit_transporteur(models.Model):
    _name = 'fedex.transporteur'
    _inherit =['mail.thread','mail.activity.mixin']

    _description = 'fedex_transporteur'

    name = fields.Char(string='Transporteur',required=True)



class fedex_regime(models.Model):
    _name = 'fedex.regime'
    _inherit =['mail.thread','mail.activity.mixin']

    _description = 'Liste des regimes'

    name  = fields.Char(string ='Libellé',required=True)

class fedex_etatSoumission(models.Model):
    _name = 'fedex.etat_soumission'
    _inherit =['mail.thread','mail.activity.mixin']

    _description = 'Liste des Etats de soumission'

    name  = fields.Char(string ='Libellé',required=True)

class fedex_typeSoumission(models.Model):
    _name = 'fedex.type_soumission'
    _inherit =['mail.thread','mail.activity.mixin']

    _description = 'Liste des Types de soumission'

    name  = fields.Char(string ='Libellé')

class fedex_retourClient(models.Model):
    _name = 'fedex.retourclient'
    _inherit =['mail.thread','mail.activity.mixin']

    _description = 'Liste des Types de retour Client'

    name  = fields.Char(string ='Libellé',required=True)


  
