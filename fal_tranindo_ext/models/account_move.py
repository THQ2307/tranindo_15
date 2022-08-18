from odoo import _, exceptions, fields, models, api
from datetime import date
from dateutil.relativedelta import relativedelta, MO, SU
from odoo.exceptions import UserError, ValidationError
from num2words import num2words


class AccountInvoice(models.Model):
    _inherit = "account.move"


    fal_stock_picking_id = fields.Many2one("stock.picking", string="Delivery", compute='_fal_get_stock_picking')
    date_invoice = fields.Date(string='Date Invoices')
    payment_voucher_bool = fields.Boolean(string="Payment Voucher")
    is_delivery_address = fields.Boolean(string="Delivery Address")
    credit_note = fields.Boolean(string="Credit Note")

    customer_npwp = fields.Char(string="NPWP")
    customer_pkp = fields.Boolean(string="Customer PKP")
    invoice_salesperson = fields.Many2one(string="Salesperson", related="fal_stock_picking_id.sale_id.user_id")
    
    def get_amount_to_text(self, total_amount):
        return num2words(total_amount, lang="id")

    html_word = fields.Char(string="HTML Word", compute="_html_to_word")

    @api.depends("narration")
    def _html_to_word(self):
        for record in self:
            if record.narration:
                record.html_word = str(record.narration)[3:-4]


    # @api.depends("partner_id")
    # def _get_customer_npwp(self):
    #     for record in self:
    #         record.customer_npwp = ""
    #         if record.partner_id.l10n_id_pkp:
    #             record.customer_npwp = record.partner_id.vat


    
    @api.depends('invoice_line_ids')
    def _fal_get_stock_picking(self):
        for invoice in self:
            sale_order_ids = invoice.invoice_line_ids.mapped('sale_line_ids').mapped('order_id')
            if sale_order_ids:
                invoice.fal_stock_picking_id = sale_order_ids[0].fal_stock_picking_id.id if sale_order_ids[0].fal_stock_picking_id else False
            else:
                invoice.fal_stock_picking_id = ''

    fal_paid_date = fields.Date(string='Paid Date')
    fal_payment_method = fields.Many2one('account.journal', string='Payment Method')
    

