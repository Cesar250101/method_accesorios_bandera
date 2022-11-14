# -*- coding: utf-8 -*-
from odoo import http

# class MethodAccesoriosBandera(http.Controller):
#     @http.route('/method_accesorios_bandera/method_accesorios_bandera/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_accesorios_bandera/method_accesorios_bandera/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_accesorios_bandera.listing', {
#             'root': '/method_accesorios_bandera/method_accesorios_bandera',
#             'objects': http.request.env['method_accesorios_bandera.method_accesorios_bandera'].search([]),
#         })

#     @http.route('/method_accesorios_bandera/method_accesorios_bandera/objects/<model("method_accesorios_bandera.method_accesorios_bandera"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_accesorios_bandera.object', {
#             'object': obj
#         })