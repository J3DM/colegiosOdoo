from odoo import models, fields, api
from datetime import timedelta

class Asignatura(models.Model):
    _name = 'colegios.asignatura'
    _description = "Asignaturas"
    titulo = fields.Char(required=True)
    fecha_inicio = fields.Date(default=fields.Date.today)
    duracion = fields.Float(digits=(6, 2), help="Duracion en días")
    plazas = fields.Integer(string="Numero de plazas disponibles")

    profesor_id = fields.Many2one('res.partner', string="Profesor")

    colegio_id = fields.Many2one('colegios.colegio',
ondelete='cascade', string="Colegio", required=True)