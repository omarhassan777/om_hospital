from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'  # hosiptal.patients
    _description = 'high Department'
    _rec_name = 'gender'

    first_name = fields.Char(string="first_name")
    last_name = fields.Char(string="last_name")
    active = fields.Boolean(default=True)
    gender = fields.Selection(
        selection=[
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ],
        string="Gender"
    )
    image = fields.Binary(string="image")

    price_outzero = fields.Float(string="price_outzero", digits=(16, 2))

    def name_get(self):
        res = []
        for rec in self:
            name = f'{rec.first_name}-{rec.gender}'
            res.append((rec.id, name))

        return res

    @api.onchange('price_outzero')
    def _onchange_price_outzero(self):
        # تحويل الرقم إلى نص
        number_str = str(self.price_outzero)

        # إذا كانت هناك الفارزة العشرية
        if '.' in number_str:
            # إزالة الأصفار الزائدة بعد الفارزة العشرية
            stripped_number = number_str.rstrip('0').rstrip('.')
            # تحديث قيمة الحقل بالقيمة المعالجة
            self.price_outzero = float(
                stripped_number) if stripped_number else 0.0
        else:
            # إذا كانت القيمة صحيحة بدون فارزة عشرية، يتم تحديثها مباشرة
            self.price_outzero = int(number_str)
