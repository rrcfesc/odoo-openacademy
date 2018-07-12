# -*- coding: utf-8 -*-
#import pdb;

from odoo import models, fields, api, exceptions

class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required = True)
    start_date =  fields.Date(default= fields.Date.today)
    datetime_test =fields.Datetime(default = fields.Datetime.now)
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(string="Number of seats");
    instructor_id = fields.Many2one("res.partner", string="Instructor", domain=["|", ('instructor', '=', True), ('category_id.name', 'ilike', 'Teacher')])
    course_id = fields.Many2one('openacademy.course', ondelete="cascade", string="Course", required = True)
    attendee_ids =  fields.Many2many("res.partner", string= "Atendee")
    taken_seats     = fields.Float(compute="_taken_seats")
    active          = fields.Boolean(default=True)

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for record in self.filtered(lambda r: r.seats != 0):
            record.taken_seats = 100.0 *len(record.attendee_ids) /record.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0 :
            self.active = False
            return {
                'warning' : {
                    'title' : 'Incorrect seats Value',
                    'message' : 'Incorrect of seats may not be negative '
                }
            }
        if self.seats < len(self.attendee_ids) :
            self.active = False
            return {
                'warning' : {
                    'title': 'To many attendees',
                    'message': 'Increment seats or remove attendees '
                }
            }
        self.active = True
    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for record in self.filtered('instructor_id'):
            if record.instructor_id in record.attendee_ids:
                raise exceptions.ValidationError("Asession instructor cant be an attendee");