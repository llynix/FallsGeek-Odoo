# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# See LICENSE file for full copyright and licensing details.
# License URL : <https://store.webkul.com/license.html/>
##############################################################################


from odoo import fields, models


class Website(models.Model):
    _inherit = 'website'

    sitewide_banner_text = fields.Html('Text for Sitewide Banner')
    sitewide_banner_background = fields.Char(string="Background Color", default="#FFFFFF")
