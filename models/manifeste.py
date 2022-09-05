# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class fedex_manifeste(models.Model):
    _name = 'fedex.manifeste'
    _inherit =['mail.thread','mail.activity.mixin']
    _description = 'Enregistrement des manifestes'

    add_date  = fields.Date(string="Date d'arrivée ", default=datetime.today())
    name  = fields.Char(string ='LTA ' ,help='057-001-004')
    Poids  = fields.Integer(string='Poids du manifeste ')
    Transporteur = fields.Many2one(string='Transporteur', comodel_name='fedex.transporteur')
    Colis_ids = fields.One2many('fedex.colis', 'Lta_id',string="colis")



#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
