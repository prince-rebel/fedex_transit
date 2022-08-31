# -*- coding: utf-8 -*-
# from odoo import http


# class FedexTransit(http.Controller):
#     @http.route('/fedex__transit/fedex__transit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fedex__transit/fedex__transit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fedex__transit.listing', {
#             'root': '/fedex__transit/fedex__transit',
#             'objects': http.request.env['fedex__transit.fedex__transit'].search([]),
#         })

#     @http.route('/fedex__transit/fedex__transit/objects/<model("fedex__transit.fedex__transit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fedex__transit.object', {
#             'object': obj
#         })
