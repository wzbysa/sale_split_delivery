from odoo import models, fields, exceptions, api, _
from odoo.exceptions import UserError

class SaleDeliveryAddress(models.Model):
    _name = 'sale.delivery.address'
    _description="Sale delivery address"

    partner_id = fields.Many2one('res.partner')
    reference = fields.Char(related='partner_id.ref')
    product_id = fields.Many2one(
        'product.product',
        string='Product',
        check_company=True,
    )
    quantity = fields.Integer('Qty.')
    order_id = fields.Many2one('sale.order')
    company_id = fields.Many2one('res.company', 'Company')