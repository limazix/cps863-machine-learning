# -*- utf-8 -*-

from unittest import TestCase

from tools.reports.reports_builder import ReportsBuilder


class TestReportsBuilder(TestCase):
    def setUp(self):
        self.builder = ReportsBuilder()

    def test_report_contents(self):
        """
        it should have a dictionary property contents to store the report contents
        """
        self.assertIsNotNone(self.builder.contents)
        self.assertIsInstance(self.builder.contents, dict)

    def test_add_report_title(self):
        """
        it should add the given string to a markdown title inside the variable contents
        at first position
        """
        title = "Some Title"
        expected_item = "# {}".format(title)
        self.assertIsInstance(self.builder.add_report_title(title), ReportsBuilder)
        self.assertIsNotNone(self.builder.contents["title"])
        self.assertEqual(expected_item, self.builder.contents["title"])
