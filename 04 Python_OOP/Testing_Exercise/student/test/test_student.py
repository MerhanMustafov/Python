import unittest

from project.student import Student


class StudentTests(unittest.TestCase):
    def setUp(self):
        self.s = Student("Harry", {})

    def test_init_without_second_param(self):
        s = Student("Harry")

        self.assertEqual(s.name, "Harry")
        self.assertEqual(s.courses, {})

    def test_init_with_second_param_none(self):
        s = Student("Harry", None)

        self.assertEqual(s.name, "Harry")
        self.assertEqual(s.courses, {})

    def test_init_with_second_param_dict(self):
        s = Student("Harry", {"Python": ["note1"]})

        self.assertEqual(s.name, "Harry")
        self.assertEqual(s.courses, {"Python": ["note1"]})

    def test_enroll_extend_notes(self):
        course_name = "Python"
        notes = ["note2"]
        add_course_notes = ""
        self.s.courses = {"Python": ["note1"]}

        res = self.s.enroll(course_name, notes, add_course_notes)
        self.assertEqual(res, "Course already added. Notes have been updated.")
        self.assertEqual(self.s.courses["Python"], ["note1", "note2"])

    def test_when_enrol_add_course_notes_is_Y(self):
        course_name = "Py"
        notes = ["note2"]
        add_course_notes = "Y"

        res = self.s.enroll(course_name, notes, add_course_notes)
        self.assertEqual(res, "Course and course notes have been added.")
        self.assertEqual(self.s.courses, {"Py": ["note2"]})

    def test_when_enrol_add_course_notes_is_empty(self):
        course_name = "Py"
        notes = ["note2"]
        add_course_notes = ""

        res = self.s.enroll(course_name, notes, add_course_notes)
        self.assertEqual(res, "Course and course notes have been added.")
        self.assertEqual(self.s.courses, {"Py": ["note2"]})

    def test_when_enrol_add_course_notes_is_no(self):
        course_name = "Py"
        notes = ["note2"]
        add_course_notes = "no"

        res = self.s.enroll(course_name, notes, add_course_notes)
        self.assertEqual(res, "Course has been added.")
        self.assertEqual(self.s.courses, {"Py": []})

    def test_add_notes(self):
        self.s.courses = {"Py": ["note1"]}
        course_name = "Py"
        notes = "note2"

        res = self.s.add_notes(course_name, notes)
        self.assertEqual(res, "Notes have been updated")
        self.assertEqual(self.s.courses, {"Py": ["note1", "note2"]})

    def test_add_notes_raise_exception(self):
        self.s.courses = {"Py": ["note1"]}
        course_name = "Python"
        notes = "note2"

        with self.assertRaises(Exception) as ex:
            self.s.add_notes(course_name, notes)
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course(self):
        self.s.courses = {"Py": ["note1"]}
        course_name = "Py"

        res = self.s.leave_course(course_name)
        self.assertEqual(res, "Course has been removed")
        self.assertEqual(self.s.courses, {})

    def test_leave_course_exception(self):
        self.s.courses = {"Py": ["note1"]}
        course_name = "Python"

        with self.assertRaises(Exception) as ex:
            self.s.leave_course(course_name)
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))



