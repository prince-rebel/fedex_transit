# -*- coding: utf-8 -*-

import string
from odoo import models, fields, api
from datetime import datetime


class fedex_eclatement(models.Model):
    _name = 'fedex.eclatement'
    _inherit =['mail.thread','mail.activity.mixin']
    _description = 'Faire des éclatements'


    Lta_id  = fields.Many2one(string="Numero LTA",comodel_name='fedex.manifeste',required=True)
    articles_ids  = fields.One2many('fedex.articles','eclatement_ids',string="articles")
    Date_Eclatement= fields.Date(string="Date ", default=datetime.today())
    nbrTotal = fields.Integer(string="Nombre total d'article",compute='_totalArticle',required=True)

    @api.onchange('articles_ids')
    def _totalArticle(self):
        for record in self:
            record.nbrTotal = len(record.articles_ids)








#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
