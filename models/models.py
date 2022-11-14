# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RepairOrder(models.Model):
    _inherit = 'repair.order'

    user_id = fields.Many2one('res.users', string='Instalador',required=True)
    patente = fields.Char('Patente',required=True)
    nro_boleta = fields.Char('Nro. Boleta',required=True)




    