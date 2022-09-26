# -*- coding: utf-8 -*-

import string
from odoo import models, fields, api
from datetime import datetime

class fedex_sortie_colie(models.Model):
    _inherit="fedex.colis"
    _name="fedex.sortie"
    _inherit =['mail.thread','mail.activity.mixin']
    _description = 'Demande  de sortie'

    name_test = fields.Char(string='teste')


# class fedex_validations(models.Model):
#     _name = 'fedex.validations'
#     _inherit =['mail.thread','mail.activity.mixin']
#     _description = 'Demande de validations de sortie'


#     Lta_id  = fields.Many2one(string="Numero LTA",comodel_name='fedex.manifeste',required=True)
#     articles_ids  = fields.One2many(related='Lta_id.Colis_ids',readonly=False,
#     ondelete='cascade'
#     )
#     Date_Eclatement= fields.Date(string="Date ", default=datetime.today())
#     nbrTotal = fields.Integer(string="Nombre total d'article",compute='_totalArticle',required=True)
#     Poids_manifest = fields.Float(string='poids du manifeste',store=True,
#         compute='_onchangeLta' )
    
    
    # manifest_article =fields.Char(compute='_custom_method')

    
    @api.onchange('articles_ids')
    def _totalArticle(self):
        for record in self:
            record.nbrTotal = len(record.articles_ids)

    @api.depends('Lta_id')
    def _onchangeLta(self):
        for r in self:
            r.Poids_manifest=r.Lta_id.Poids


    # @api.onchange('Lta_id')
    # def _Ltaidonchange(self):
    #     domain={'articles_ids':[('Lta_id',)]}
    # def _custom_method(self):

    #     self.manifest_article = self.env.get('Lta_id').id
    #     print ("...context..",self.env.context.get('active_id'))
    #     print ("...context..", self.env.context)
    





#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
