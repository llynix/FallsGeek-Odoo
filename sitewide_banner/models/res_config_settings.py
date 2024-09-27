# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# See LICENSE file for full copyright and licensing details.
# License URL : <https://store.webkul.com/license.html/>
##############################################################################


from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    show_sitewide_banner = fields.Boolean(
        string="Sitewide Banner",
        config_parameter='sitewide_banner.show_sitewide_banner')
    sitewide_banner_background = fields.Char(string="Background Color", related="website_id.sitewide_banner_background", readonly=False)
    sitewide_banner_text = fields.Html(
        string='Sitewide Banner Text',
        related='website_id.sitewide_banner_text',
        readonly=False)

    @api.onchange('show_sitewide_banner')
    def onchange_show_sitewide_banner(self):
        if not self.show_sitewide_banner:
            self.sitewide_banner_text = False
