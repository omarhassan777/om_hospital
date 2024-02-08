from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class HospitalSurgeryDepartment(models.Model):
    _name = 'hospital.surgery.department'  # hosiptal.patients
    _description = 'high Department '
    # _rec_name='capacity'

    name = fields.Char()
    capacity = fields.Integer()
    is_open = fields.Boolean()

    patients = fields.Char()
    patient_id = fields.One2many('hospital.surgery.patients', 'department_id')
    
    
    # Define a related field to get the patient test result from the patient records
    patient_test_result = fields.Char(
        string='Patient Test Result',
        related='patient_id.test',
        store=False  # Set store to False to make it a virtual field
    )

    # blood_types_depart = fields.Many2many(
    #     'hospital.surgery.patients',  # Model to reference
    #     'department_blood_type_rel',  # Table name for the relationship
    #     'department_id',  # Field in this model
    #     'blood_type',  # Field in the referenced model
    #     string="Blood Types",
    #     compute="_compute_blood_types",
    #     store=True
    # )

    # @api.depends('patient_id.blood_type')
    # def _compute_blood_types(self):
    #     for department in self:
    #         blood_types = department.patient_id.mapped('blood_type')
    #         department.blood_types_depart = blood_types


# before create one2many should creat field many2one becaus you need his data to creat one2many
