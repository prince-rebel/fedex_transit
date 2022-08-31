# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fedex_transit(models.Model):
    _name = 'fedex.transit'
    _description = 'fedex_transit'

    name = fields.Char()
    value = fields.Integer()
    description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
