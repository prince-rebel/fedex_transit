# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fedex_articles(models.Model):
    _name = 'fedex.articles'
    _inherit =['mail.thread','mail.activity.mixin']
    _description = 'Articles des lots'

    Lta_id  = fields.Many2one(string="Numero LTA",comodel_name='fedex.manifeste')
    NumLignle= fields.Integer(string="N°Ligne",  default='1')
    name = fields.Char(string='Nature')
    Awb  = fields.Char(string ='AWB ' ,help='057-001-004')
    Destinateur  = fields.Many2one(string='Destinateur', comodel_name='res.partner')
    Poids  = fields.Integer(string='Poids (Kg)')
    eclatement_ids = fields.Many2one( comodel_name='fedex.eclatement')
    # Lta_id  = fields.Char(string="Numero LTA" ,related='eclatement_ids.Lta_id')
    Nbr  = fields.Integer(string="Nombre",  default='1')
    ImageArticles  = fields.Binary("image Article")








#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
