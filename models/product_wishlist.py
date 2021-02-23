# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import api, fields, models
from odoo.http import request

class Customers(models.Model):
    _inherit = 'res.partner'

    wishlist_ids = fields.One2many('product.wishlist', 'partner_id', string='Wishlist Products')

class ProductWishlist(models.Model):
    _inherit = 'product.wishlist'

    quantity = fields.Integer(string="Quantity", default=1)