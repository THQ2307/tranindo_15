from odoo import _, exceptions, fields, models, api
from datetime import date
from dateutil.relativedelta import relativedelta, MO, SU
from odoo.exceptions import UserError, ValidationError

class AccountPayment(models.Model):
    _inherit = "account.payment"

    def action_validate_invoice_payment(self):
        invoice_obj = self.env['account.move']
        # get context
        context = dict(self._context)
        active_ids = context.get('active_ids')
        for account in invoice_obj.browse(active_ids):
            for record in self:
                account.update({
                    'fal_paid_date': record.payment_date,
                    'fal_payment_method': record.journal_id.id,
                })

        if any(len(record.invoice_ids) != 1 for record in self):
            # For multiple invoices, there is account.register.payments wizard
            raise UserError(_("This method should only be called to process a single invoice's payment."))
        return self.post()
