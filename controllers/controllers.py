# -*- coding: utf-8 -*-
# from pprint import pprint
# from unicodedata import name
# from urllib import request
# from odoo import http


# class FedexTransit(http.Controller):
#     @http.route('/fedex__transit/fedex__transit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

    # @http.route('/fedex__transit/fedex__transit/objects', auth='public')
    # def list(self, **kw):
    #     return http.request.render('fedex__transit.listing', {
    #         'root': '/fedex__transit/fedex__transit',
    #         'objects': http.request.env['fedex__transit.fedex__transit'].search([]),
    #     })

    # @http.route('/fedex__transit/mani', auth='public' ,type='http')
    # def object(self, **kw):

    #     x=http.request.env['fedex.manifeste']
    #     y=x.search([])
    #     pprint(y)
    #     for r in y:
    #         print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$',r[name])
