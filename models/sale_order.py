# Copyright 2013-2015 Camptocamp SA - Nicolas Bessi
# Copyright 2018 Camptocamp SA - Julien Coux
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, models,fields
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare


class SaleOrder(models.Model):
    """Adds picking split without done state."""

    _inherit = "sale.order"

    delivery_address_line_ids = fields.One2many(
        comodel_name='sale.delivery.address',
        inverse_name='order_id',
        string="Delivery Lines"
    )

