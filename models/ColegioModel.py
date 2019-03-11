from odoo import models, fields, api

class Colegio(models.Model):
    _name = 'colegios.colegio'
    _description = "colegios Colegio"
    nombre = fields.Char(string="Colegio", required=True)
    descripcion = fields.Text()

    responsable_id = fields.Many2one('res.users',
ondelete='set null', string="Responsable", index=True)

    asignatura_ids = fields.One2many(
'colegios.asignatura', 'colegio_id', string="Asignaturas del colegio")