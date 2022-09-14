from email.policy import default
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class transaction(models.Model):
    _name = 'darkweb.transaction'
    _description = 'Transaction'

    no_bill = fields.Char(string='No.')
    customer_name = fields.Many2one(comodel_name='res.partner',
                                string='Customer Name')
    payment_date = fields.Datetime(
        string='Payment Date',
        default=fields.Datetime.now()
    )
    payment_total = fields.Integer(
        string='Total Payment',
        compute='_compute_totalpayment'
    )
    transactiondetails_ids = fields.One2many(
        comodel_name='darkweb.transactiondetails',
        inverse_name='transaction_id',
        string='Transaction Details'
    )

    state = fields.Selection(string = 'Status', 
            selection=[('draft','Draft'),('confirm','Confirm'),('done','Done'),('cancelled','Cancelled')],
            required=True, readonly=True, default='draft')

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancelled(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})

    @api.depends('transactiondetails_ids')
    def _compute_totalpayment(self):
        for line in self:
            result = sum(self.env['darkweb.transactiondetails'].search(
                [('transaction_id', '=', line.id)]).mapped('subtotal'))
            line.payment_total = result

    def unlink(self):
        if self.transactiondetails_ids:
            sale = []
            for line in self:
                sale = self.env['darkweb.transactiondetails'].search(
                    [('transaction_id', '=', line.id)])

            for ob in sale:
                print(ob.weapon_id.name + ' ' + str(ob.quantity))
                ob.weapon_id.stock += ob.quantity

        line = super(transaction, self).unlink()
        return line
    
    def write(self,vals):
        for rec in self:
            a = self.env['darkweb.transactiondetails'].search([('transaction_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.weapon_id.name)+' '+str(data.quantity)+' '+str(data.weapon_id.stock))
                data.weapon_id.stock += data.quantity
        record = super(transaction,self).write(vals)

        for rec in self:
            b = self.env['darkweb.transactiondetails'].search([('transaction_id','=',rec.id)])
            print(a)
            print(b)
            
            for newdata in b:
                if newdata in a:
                    print(str(newdata.weapon_id.name)+' '+str(newdata.quantity)+' '+str(newdata.weapon_id.stock))
                    newdata.weapon_id.stock -= newdata.quantity
                else:
                    pass    
        return record
    
    _sql_constraints = [
        ('no_bill_unique', 'unique (no_bill)', 'Transaction Number cannot be duplicated.')
    ]

class transactiondetails(models.Model):
    _name = 'darkweb.transactiondetails'
    _description = 'Transaction Details'

    name = fields.Char(string='Name')
    transaction_id = fields.Many2one(
        comodel_name='darkweb.transaction',
        string='Transaction Details'
    )
    weapon_id = fields.Many2one(
        comodel_name='darkweb.weapon',
        string='Weapon List'
    )
    quantity_price = fields.Integer(
        string='Quantity Price',
        onchange='_onchange_weapon_id'
    )
    quantity = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal',string='Subtotal')

    @api.depends('quantity_price', 'quantity')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.quantity_price

    @api.onchange('weapon_id')
    def _onchange_weapon_id(self):
        if self.weapon_id.selling_price:
            self.quantity_price = self.weapon_id.selling_price

    @api.model
    def create(self, vals):
        line = super(transactiondetails, self).create(vals)
        if line.quantity:
            self.env['darkweb.weapon'].search(
                [('id', '=', line.weapon_id.id)]
            ).write({'stock': line.weapon_id.stock - line.quantity})
        return line
    
    @api.constrains('quantity')
    def check_quantity(self):
        for line in self:
            if line.quantity < 1:
                raise ValidationError('The minimum Quantity of Purchase is 1.')
            elif line.weapon_id.stock < line.quantity:
                raise ValidationError('Sorry but the Stock for the Item is not Enough.')

    