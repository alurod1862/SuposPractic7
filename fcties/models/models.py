# -*- coding: utf-8 -*-

from odoo import models, fields, api

class fcties_alumno(models.Model):
    _name = 'fcties.alumno'
    _description = 'Modelo de Alumno'

    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento", required=True)
    curso_academico = fields.Char(string="Curso Académico", required=True)
    email = fields.Char(string="Correo Electrónico")
    telefono = fields.Char(string="Teléfono")
    ciclo_formativo = fields.Selection([("DAM", "DAM"), ("DAW", "DAW"), ("ASIX", "ASIX")],
                                      string="Ciclo Formativo", required=True)
    periodo_practica = fields.Selection([("abril", "Abril"), ("septiembre", "Septiembre")],
                                        string="Periodo de Práctica", required=True)
    nota_media = fields.Float(string="Nota Media", required=True)
    nota_media_texto = fields.Char(string="Nota Media en Texto", compute="_compute_nota_media_texto", store=True)
    
    empresa_id = fields.Many2one("fcties.empresa", string="Empresa")

    @api.depends('nota_media')
    def _compute_nota_media_texto(self):
        for alumno in self:
            if alumno.nota_media >= 9:
                alumno.nota_media_texto = 'Sobresaliente'
            elif alumno.nota_media >= 7:
                alumno.nota_media_texto = 'Notable'
            elif alumno.nota_media >= 5:
                alumno.nota_media_texto = 'Aprobado'
            else:
                alumno.nota_media_texto = 'Suspenso'
                

class fcties_empresa(models.Model):
    _name = 'fcties.empresa'
    _description = 'Modelo de Empresa'

    name = fields.Char(string="Nombre", required=True)
    persona_contacto = fields.Char(string="Persona de Contacto", required=True)
    telefono_contacto = fields.Char(string="Teléfono de Contacto", required=True)
    email = fields.Char(string="Correo Electrónico", required=True)
    direccion = fields.Text(string="Dirección", required=True)

    # Campos de relación
    alumnos_ids = fields.One2many("fcties.alumno", "empresa_id", string="Alumnos")