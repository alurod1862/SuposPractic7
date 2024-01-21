# -*- coding: utf-8 -*-
# from odoo import http


# class EscuelaVela(http.Controller):
#     @http.route('/escuela_vela/escuela_vela', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/escuela_vela/escuela_vela/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('escuela_vela.listing', {
#             'root': '/escuela_vela/escuela_vela',
#             'objects': http.request.env['escuela_vela.escuela_vela'].search([]),
#         })

#     @http.route('/escuela_vela/escuela_vela/objects/<model("escuela_vela.escuela_vela"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('escuela_vela.object', {
#             'object': obj
#         })
