# -*- coding: utf-8 -*-

# from odoo import models, fields, api


from email.policy import default
from odoo import models,fields,api
from rsa import PrivateKey



class Package(models.Model):

    _name = 'iti.package'
    _description = 'Call Package'

    name = fields.Char()
    price = fields.Float()
    type = fields.Selection(selection=[
        ('unit','Unit'),
        ('flex','Flex')
    ],default='unit')


class CallLog(models.Model):
    _name = 'iti.call.log'
    _description = 'sec_lab.sec_lab'
    _rec_name = 'timestamp'




    customer = fields.Char()
    timestamp = fields.Datetime()
    from_number = fields.Char(string='From')
    to_number = fields.Char(string='To')
    duration = fields.Integer()
    price = fields.Float(compute='_compute_price')
    notes = fields.Text()
    package_id = fields.Many2one(comodel_name='iti.package')


    @api.depends('duration','package_id.price')
    def _compute_price(self):
        for rec in self :
            rec.price = (rec.duration / 60) * rec.package_id.price


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100