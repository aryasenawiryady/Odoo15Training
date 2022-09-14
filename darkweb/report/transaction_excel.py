from odoo import models, fields
from datetime import timedelta

class TransactionExcel(models.AbstractModel):
    _name= 'report.darkweb.report_transaction_xlsx'
    _inherit= 'report.report_xlsx.abstract'
    report_date= fields.Date.today() 

    def generate_xlsx_report(self, workbook, data, transaction):
        sheet = workbook.add_worksheet('Transaction List')
        sheet.write(0, 0, str(self.report_date))

        bold = workbook.add_format({'bold': True})
        sheet.write(1, 0, 'No.', bold)
        sheet.write(1, 1, 'Customer Name', bold)
        sheet.write(1, 2, 'Payment Date', bold)
        sheet.write(1, 3, 'Items', bold)
        sheet.write(1, 4, 'Price', bold)
        sheet.write(1, 5, 'Quantity', bold)
        sheet.write(1, 6, 'Subtotal', bold)
        sheet.write(1, 7, 'Total Price', bold)

        row = 2
        col = 0
        for obj in transaction:
            col = 0

            sheet.set_column(row, col, 20)
            sheet.write(row, col, obj.no_bill)
            sheet.write(row, col + 1, obj.customer_name.name)
            sheet.write(row, col + 2, (obj.payment_date+ timedelta(hours=7)).strftime("%d/%m/%Y, %H:%M:%S"))
            sheet.write(row, col + 7, obj.payment_total)
            
            for item in obj.transactiondetails_ids:
                sheet.set_column(row, col, 20)
                sheet.write(row, col+3, item.weapon_id.name)
                sheet.write(row, col+4, item.quantity_price)
                sheet.write(row, col+5, item.quantity)
                sheet.write(row, col+6, item.subtotal)
                row += 1
            