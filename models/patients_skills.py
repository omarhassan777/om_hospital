from odoo import models, fields


class patientskills(models.Model):
    _name = 'patient.skills'  # hosiptal.patients

    name = fields.Char()
