# -*- coding: utf-8 -*-

from asyncio.log import logger
from pprint import pprint
from re import template
from odoo import models, fields, api
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)


class fedex_manifeste(models.Model):
    _name = 'fedex.manifeste'
    _inherit =['mail.thread','mail.activity.mixin']
    _description = 'Enregistrement des manifestes'

    add_date  = fields.Date(string="Date d'arrivée ", default=datetime.today())
    name  = fields.Char(string ='LTA ' ,help='057-001-004',required=True)
    Poids  = fields.Integer(string='Poids du manifeste ',required=True)
    Transporteur = fields.Many2one(string='Transporteur', comodel_name='fedex.transporteur',required=True,tracking=True)
    Colis_ids = fields.One2many('fedex.colis', 'Lta_id',string="colis" ,store=True,ondelete='cascade',tracking=True)
    # Colis_ids = fields.Many2many(
    # comodel_name='fedex.colis',relation='manifeste_colis_relation',
    # column1="name",
    # column2="NumColis"
    # )
    createur  = fields.Many2one('res.users','Utilisateur ', default=lambda self: self.env.user)
    state = fields.Selection(selection=[
           ('draft', 'Draft'),
           ('in_progress', 'In Progress'),
           ('cancel', 'Cancelled'),
           ('done', 'Done'),
       ], string='Status', required=True, readonly=True, copy=False,
       tracking=True, default='draft')

   



    def button_get_in_eclatement(self):
        x=self.id
        return _logger.info("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",x)
    #    self.write({
    #        'state': "in_progress"
    #    })

       
      

    # def send_mail(self):
    #     self.ensure_one()

    #     template_id=self.env.ref('fedex__transit.email_template_relance').id
    #     ctx={
    #         'default_model':'fedex.manifeste',
    #         'default_res_id':self.id,
    #         'default_use_template':bool(template_id),
    #         'default_template_id':template_id,
    #         'default_composition_mode':'comment',
    #         'email_to':self.Colis_ids.courrier,
    #     }
    #     return{
    #         'type': 'ir.actions.act_window',
    #         'view_type':'form',
    #         'view_mode':'form',
    #         'res_model':'mail.compose.message',
    #         'target':'new',
    #         'context':ctx,
    #     }



#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
