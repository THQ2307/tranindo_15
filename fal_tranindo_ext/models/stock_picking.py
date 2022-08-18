from odoo import fields, models, api
from odoo import _
from odoo.exceptions import UserError, ValidationError
import logging
import odoo.addons.decimal_precision as dp
_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    no_po_do = fields.Char(string="Customer Reference", compute="_get_customer_reference")
    sticker_delivery = fields.Integer(string="Sticker Delivery")

    @api.depends("sale_id")
    def _get_customer_reference(self):
        for record in self:
            record.no_po_do = ""
            if record.sale_id.client_order_ref:
                record.no_po_do = record.sale_id.client_order_ref

    def _get_product_bom_report(self):
        data = []
        for record in self.move_ids_without_package:
            # for x in record.sale_line_id.product_id:
            data.append([record, record.sale_line_id.product_id, record.sale_line_id])
        
        res = {}
        for table, sale_product, sale_id in data:
            if sale_id in res:
                res[sale_id]['product'] = sale_id.product_id
                res[sale_id]['table'] = table
            else:
                res[sale_id] = {'product': sale_id.product_id, 'table':table,}

        data_new = []
        for record in res:
            data_new.append(res[record])

        return data_new

