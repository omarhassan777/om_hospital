
{
    "name": "Hospital Manager",
    "summary": "patients record 2",
    "website": "odoo.com",
    "depends": ["mail"],
    "data": [
        "secuirty/ir.model.access.csv",

        "data/sequence.xml",
        "views/menu.xml",
        "views/patients.xml",
        "views/patients_surgery.xml",
        "views/patient_surg_department.xml",
        "views/hospital_doctors.xml",
        "reports/report.xml",
        "reports/patient_card.xml",
        "reports/sale_report_inherit.xml"


    ]


}
