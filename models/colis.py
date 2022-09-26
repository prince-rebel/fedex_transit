import email
from email.mime import image
from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError



class fedex_transit_colis(models.Model):
    _name = 'fedex.colis'
    _inherit =['mail.thread','mail.activity.mixin']
    _description = 'fedex_colis'


    # add_date  = fields.Date(string="Date d'arrivée ", default=datetime.today())
    Lta_id  = fields.Many2one(string="Numero LTA",comodel_name='fedex.manifeste',
    ondelete='set null'
    )
    # Lta_id = fields.Char(related='fedex_manifeste.name',store=True)
    NumColis = fields.Integer(string='AWB ',required=True,tracking=True)
    NumLigne = fields.Integer(string='Ligne ',default='1')
    Poids  = fields.Integer(string='Poids du colis ',required=True,tracking=True)
    # Transporteur = fields.Many2one(string='Transporteur', comodel_name='fedex.transporteur')
    Destinateur  = fields.Many2one(string='Destinateur', comodel_name='res.partner',required=True,tracking=True)
    NbrColis  = fields.Float(string="Nombre de colis",  default='1',required=True)
    Description = fields.Text(string='Description',required=True,tracking=True)
    ValeurColis  = fields.Float(string='Valeur du colis')
    # StatusColis= fields.Many2one(string=' Status', comodel_name='fedex.statut_colis')
    state_colis = fields.Selection(selection=[('magasin', 'En magasin'),
                                                         ('pret','Pret à la livraison'),('sortie_confirme','Autorisation confirmée'),('livre','livré')],default='magasin',string="status du colis",tracking=True)
    ModeSortie_id= fields.Many2one(string=' Mode de Sortie', comodel_name='fedex.modesortie',tracking=True)
    Ref = fields.Char(string='Reférence')
    Date_de_sortie = fields.Date(string="Date d'arrivée ", default=datetime.today())
    courrier = fields.Char(string="client Email",compute='_mail_user')
    ImageColis  = fields.Binary("image du colis")
    doc = fields.Binary(string="Document",tracking=True)    
    doc_name = fields.Char(string='File name')
    Transitaire = fields.Many2one('fedex.retourclient',string='Transitaire')

    # @api.constrains('NumLta')
    # def _check_lta(self):
    #     for record in self:
    #         if record.NumLta.values:
    #             raise ValidationError("Ce Numero LTA existe déja")
    @api.onchange('Destinateur')
    def _mail_user(self):
        for record in self:
            record.courrier= record.Destinateur.email


    def Envoyer_demande_sortie(self):
        self.state_colis ="pret"

    def valider_sortie(self):
        self.state_colis ="sortie_confirme"

    def Marquer_livre(self):
        self.state_colis ="livre"

    def send_mail(self):
        self.ensure_one()
       
        template_id=self.env.ref('fedex__transit.email_template_avisclient').id
        ctx={
            'default_model':'fedex.colis',
            'default_res_id':self.id,
            'default_use_template':bool(template_id),
            'default_template_id':template_id,
            'default_composition_mode':'comment',
            'email_to':self.Destinateur.email,
        }
        return{
            'type': 'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'mail.compose.message',
            'target':'new',
            'context':ctx,
        }



