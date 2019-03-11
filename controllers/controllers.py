# -*- coding: utf-8 -*-
from odoo import http

# class Colegios(http.Controller):
#     @http.route('/colegios/colegios/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/colegios/colegios/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('colegios.listing', {
#             'root': '/colegios/colegios',
#             'objects': http.request.env['colegios.colegios'].search([]),
#         })

#     @http.route('/colegios/colegios/objects/<model("colegios.colegios"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('colegios.object', {
#             'object': obj
#         })