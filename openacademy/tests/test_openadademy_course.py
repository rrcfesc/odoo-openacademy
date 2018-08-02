# -*- coding: utf-8 -*-
from psycopg2 import IntegrityError
from odoo.tests import common
from odoo.tools import mute_logger

# To mute sql constraints error use:
# "with mute_loger('odoo.sql_db'), ..." or
# "@mute_logger('odoo.sql_db')" before function

class GlobalTestOpenAcademyCourse(common.TransactionCase):
    # Global test for openacademy module,
    # Test course

    # Pseudo-constructor method of test setUp
    def setUp(self):

        # Define global variables to test methods
        super(GlobalTestOpenAcademyCourse, self).setUp()
        self.course = self.env['openacademy.course']

    # Class methods (Isn't a test)

    # Create course function
    def create_course(self, course_name, course_description, course_responsible_id):
        course_id = self.course.create({
            'name': course_name,
            'description': course_description,
            'responsible_id': course_responsible_id,
            })
        return course_id

    # Tests methods (start with: 'test_')

    @mute_logger('odoo.sql_db')
    def test_10_course_same_name_description(self):

        # Test: Create a course with the same name and description.
        # Constraint of different name than description.
        with self.assertRaisesRegexp(IntegrityError,
            'new row for relation "openacademy_course" violates check'
            ' constraint "openacademy_course_name_description_check"'):
            self.create_course('test','test', None)

    @mute_logger('odoo.sql_db')
    def test_20_courses_same_name(self):

        # Test: Create a course with ixisting name
        # Constraint of unique name
        with self.assertRaisesRegexp(IntegrityError,
            'duplicate key value violates unique constraint "openacademy_course_name_unique"'):
            self.create_course('Test Name', 'Test Description', None)
            self.create_course('Test Name', 'Test Description', None)

    def test_15_duplicate_course(self):

        # Test: Duplicate course and pass constraint name
        course = self.env.ref('openacademy.course0')
        course_id = course.copy()
        self.assertEqual(
            course_id.name,
            'Course 0otro')
