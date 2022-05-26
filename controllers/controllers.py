# -*- coding: utf-8 -*-
# from odoo import http


# class SecLab(http.Controller):
#     @http.route('/sec_lab/sec_lab', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sec_lab/sec_lab/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sec_lab.listing', {
#             'root': '/sec_lab/sec_lab',
#             'objects': http.request.env['sec_lab.sec_lab'].search([]),
#         })

#     @http.route('/sec_lab/sec_lab/objects/<model("sec_lab.sec_lab"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sec_lab.object', {
#             'object': obj
#         })
