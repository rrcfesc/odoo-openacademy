# -*- coding: utf-8 -*-

from psycopg2 import IntegrityError
from odoo.tests import common
from odoo.exceptions import ValidationError
from odoo.tools import mute_logger  # noqa

class GlobalTestOpenAcademySession(common.TransactionCase):
    # Global test for openacademy module,
    # Test session

    # Pseudo-constructor method of test setUp
    def setUp(self):
        # Define global variables to test methods
        super(GlobalTestOpenAcademySession, self).setUp()
        self.session = self.env['openacademy.session']
        self.course = self.env.ref('openacademy.course0')
        self.partner = self.env.ref('base.res_partner_1')
        self.attendee = self.env.ref('base.res_partner_2')

    # Class methods (Isn't a test)

    # Create session function
    def create_session(self, session_name, session_seats,
        session_instructor_id, session_attendee_ids, session_course_id):
        session_id = self.session.create({
            'name': session_name,
            'seats': session_seats,
            'instructor_id': session_instructor_id,
            'attendee_ids': session_attendee_ids,
            'course_id': session_course_id,
        })
        return session_id

        # Test methods
        # Mute SQL error
        @mute_logger('odoo.sql_db')
        def test_04_instructor_is_attendee(self):
            """
            Check that raise of 'A session's instructor can't be an attendee
            """
            test_04_instructor_is_attendee_correct = False
            try:
                partner_vauxoo = self.env.ref('base.res_partner_2')
                course = self.env.ref('openacademy.course0')
                self.create_session(
                    name='Session test 1',
                    seats=1,
                    instructor=partner_vauxoo,
                    course=course,
                    attendees=[partner_vauxoo.id]
                )
            except ValidationError as vaidation_error:
                test_04_instructor_is_attendee_correct = True
                self.assertEquals(
                    vaidation_error.name, (
                        "A session's instructor can't be an attendee"
                    )
                )

            self.assertTrue(test_04_instructor_is_attendee_correct)
    # Mute SQL error
    @mute_logger('odoo.sql_db')
    def test_20_session_without_course(self):
        # Test: Create a session without course
        # Python constraint for session without course

        with self.assertRaisesRegexp(IntegrityError, 'null value in column "course_id"'
            ' violates not-null constraint'):

            self.create_session('Session Test Name', 2, self.partner.id,
            [(6,0,[self.partner.id])], None)

    # Mute SQL error
    @mute_logger('odoo.sql_db')
    def test_30_create_valid_session(self):
        # Test: Create a session with valid parameters

        session = self.create_session('Session Test Name', 2, self.partner.id,
        [(6,0,[self.attendee.id])], self.course.id)

        self.assertTrue(self.session.search([('id','=', "{}".format(session.id))]).id)
