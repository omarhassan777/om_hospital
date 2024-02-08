
from odoo import fields, models, api
from odoo.exceptions import UserError


class HospitalSurgeryPatients(models.Model):
    _name = 'hospital.surgery.patients'
    _description = 'Surgery Patients'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", readonly=True)
    is_child = fields.Boolean(string="Is Child")
    Birth_data = fields.Date(string="Birth_data")
    history = fields.Html()
    cr_ratio = fields.Float(string="CR Ratio")
    notes = fields.Text(string="Notes")
    # blood_type = fields.Many2one(string="blood type")
    pcr = fields.Boolean(string="PCR")
    image = fields.Binary()
    adress = fields.Text(string="address")
    email = fields.Char(string="email")
    blood_type = fields.Selection(
        [('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')],
        string="Blood Type"
    )
   
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        string="Gender"
    )

    login_time = fields.Datetime()
    department_id = fields.Many2one("hospital.surgery.department")
    department_capacity = fields.Integer(related="department_id.capacity")
    doctor_id = fields.Many2many('hospital.doctor')
    test = fields.Char(string=" get type")
   

    @api.onchange('blood_type')
    def _onchange_age(self):
        if self.blood_type:
            self.test = self.blood_type
        else:
            self.test = "1"

    @api.model
    def create(self, vals):
        if 'name' in vals:
            search_employee = self.search(
                [('name', '=', vals['name'])], limit=5)
            if search_employee:
                raise UserError("Employee with the same name already exists.")
        return super().create(vals)

    # @api.model
    # def create(self, vals):
    #     print(f"Before modification - vals: {vals}")
    #     name_split = vals['name'].split()
    #     vals["email"] = f"{name_split[0][0]}{name_split[0]}@gmail.com"
    #     result = super().create(vals)
    #     print(f"After modification - result: {result}")
    #     return result

    def write(self, vals):
        # By checking if 'name' is present in the vals dictionary before modifying it, you ensure that the write method works as expected.
        if 'name' in vals:
            name_split = vals['name'].split()
            vals['email'] = f"{name_split[0][0]}{name_split[1]}@gmail.com"

        # Call the superclass write method and return its result
        return super(HospitalSurgeryPatients, self).write(vals)


# class Hospitalpatients(Hospitalpatients):
