from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class Hospitalpatients(models.Model):
    _name = 'hospital.patients'  # hosiptal.patients
    _description = 'high services '
    _inherit = "mail.thread"

    name = fields.Char(string="Name", required=True,
                       tracking=True)  # tracking to log history
    age = fields.Integer(string="age", tracking=True)
    is_child = fields.Boolean(string="Is Chaild", tracking=True)
    image = fields.Binary(string="Image")
    width = fields.Integer(string="width", tracking=True)
    phone = fields.Char(string="phone", tracking=True)

    hight = fields.Integer(
        string="hight", compute="_compute_hight", store=True, tracking=True)
    notes = fields.Text(string="Notes")
    ref = fields.Char(string="Reference", default=lambda self: _('New'))
    capitalize_name = fields.Char(
        string="capitalize Name", compute="_compute_capitalize_name", store=True)

    # surgery_id = fields.Many2many(
    #     'hospital.surgery.patients', string="surgery")
    gender = fields.Selection(
        selection=[
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ],
        string="Gender"
    )
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    tag_ids = fields.Many2many(
        'res.partner.category', 'hospital_patient_tag_rel', "patient_id", 'tag_id', string="Tags")

    def action_share_whatsapp(self):
        if not self.phone:
            raise ValidationError(_("missing phone number!"))
        message = 'Hi %s ' % self.name
        whats_link_api = "https://api.whatsapp.com/send?phone=%s&text=%s" % (
            self.phone, message)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': whats_link_api
        }

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code(
                "hospital.patients")
        return super(Hospitalpatients, self).create(vals_list)

    @api.depends('width')
    def _compute_hight(self):
        for rec in self:
            if rec.width:
                rec.hight = rec.width*2.0
            else:
                rec.hight = ''

    @api.constrains('is_child', 'age')   # to connect to feild
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(_("Age has to be recorded"))
            else:
                rec.capitalize_name = ''

    @api.depends('name')
    def _compute_capitalize_name(self):
        for rec in self:
            if rec.name:
                rec.capitalize_name = rec.name.upper()
            else:
                rec.capitalize_name = ''

    @api.onchange('age')
    def _onchange_age(self):
        if (self.age) <= 15:
            self.is_child = True
        else:
            self.is_child = False

    # @api.onchange('width')
    # def _onchange_width(self):
    #     if (self.width) <= 20:
    #         self.hight = 40

    #     else:
    #         self.hight = 70
