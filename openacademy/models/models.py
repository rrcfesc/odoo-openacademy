# -*- coding: utf-8 -*-
#import pdb;

from odoo import models, fields, api, exceptions
import time
class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', string="Responsible", Index= True, ondelete = "set null", default = lambda self, *a: self.env.uid)
    session_ids = fields.One2many('openacademy.session', 'course_id')

    _sql_constraints = [
        ('name_description_check', 'CHECK(name!= description)', "The title of the coyrse not be description"),
        ('name_unique', 'UNIQUE(name)', 'The course title must be unique')
    ]

    def copy(self, default= None):
        if default is None:
            default = {}
        default['name'] = self.name + 'otro'
        return super(Course, self).copy(default)



