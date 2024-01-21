# -*- coding: utf-8 -*-

from odoo import models, fields, api

class escuelavela_alumno(models.Model):
    _name = 'escuelavela.alumno'
    _description = 'Alumno de Vela'

    name = fields.Char(string="Nombre", required=True)
    contact = fields.Text(string="Datos de Contacto")
    matricula_number = fields.Char(string="Número de Matrícula", required=True)
    escuela = fields.Many2one("escuelavela.escuela", string="Escuela")

    @api.model
    def create(self, vals):
        if vals.get('matricula_number', 'New') == 'New':
            escuela = self.env['escuelavela.escuela'].browse(vals['escuela'])
            vals['matricula_number'] = escuela.matricula_sequence.next_by_id() or '/'
        return super(escuelavela_alumno, self).create(vals)



class escuelavela_monitor(models.Model):
    _name = 'escuelavela.monitor'
    _description = 'Monitor de Vela'

    name = fields.Char(string="Nombre", required=True)
    contact = fields.Text(string="Datos de Contacto")
    unique_id = fields.Char(string="Código de Identificación Único", required=True)
    escuelas_colaboradoras = fields.Many2many("escuelavela.escuela", string="Escuelas Colaboradoras")
    

    
class escuelavela_curso(models.Model):
    _name = 'escuelavela.curso'
    _description = 'Curso de Vela'
    
    title = fields.Char(string="Título", required=True)
    duration_days = fields.Integer(string="Duración(días)")
    duration_hours = fields.Float(string="Duración(horas)")
    price = fields.Float(string="Precio")
    
    escuela = fields.Many2one("escuelavela.escuela", string="Escuela", inverse_name="cursos")

class escuelavela_escuela(models.Model):
    _name = 'escuelavela.escuela'
    _description = 'Escuela de Vela'

    denominacion = fields.Char(string="Denominación", required=True, help="Introduce la denominacion de la escuela")
    logo = fields.Binary(string="Logotipo")
    contact = fields.Text(string="Datos de Contacto")
    matricula_sequence = fields.Many2one("ir.sequence", string="Secuencia de Matrícula", compute="_compute_matricula_sequence", store=True)
    cursos = fields.One2many("escuelavela.curso", string="Cursos", inverse_name="escuela")
    monitores = fields.Many2many("escuelavela.monitor", string="Monitores")
    alumnos = fields.One2many("escuelavela.alumno", string="Alumnos", inverse_name="escuela")

    @api.depends('denominacion')
    def _compute_matricula_sequence(self):
        for escuela in self:
            code = f"escuelavela.alumno.seq.{escuela.denominacion.replace(' ', '_').lower()}"
            sequence = self.env['ir.sequence'].search([('code', '=', code)])
            if not sequence:
                sequence = self.env['ir.sequence'].create({
                    'name': f"Alumno Sequence - {escuela.denominacion}",
                    'code': code,
                    'prefix': f"ALUMNO-{escuela.denominacion.replace(' ', '_').upper()}",
                    'padding': 5,
                })
            escuela.matricula_sequence = sequence.id



    
