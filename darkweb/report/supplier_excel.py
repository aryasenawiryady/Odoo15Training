from odoo import models, fields

class SupplierExcel(models.AbstractModel):
    _name= 'report.darkweb.report_supplier_xlsx'
    _inherit= 'report.report_xlsx.abstract'
    report_date= fields.Date.today() 

    def generate_xlsx_report(self, workbook, data, supplier):
        sheet = workbook.add_worksheet('Supplier List')
        sheet.write(0, 0, str(self.report_date))

        bold = workbook.add_format({'bold': True})
        sheet.write(1, 0, 'Company Name', bold)
        sheet.write(1, 1, 'Address', bold)
        sheet.write(1, 2, 'Phone', bold)
        sheet.write(1, 3, 'Items', bold)

        row = 2
        col = 0
        for obj in supplier:
            col = 0

            sheet.write(row, col, obj.name)
            sheet.write(row, col + 1, obj.address)
            sheet.write(row, col + 2, obj.phone)
            sheet.set_column(row, col, 20)
            for item in obj.weapon_id:
                sheet.write(row, col + 3, item.name)
                sheet.set_column(row, col, 20)
                row += 1
            