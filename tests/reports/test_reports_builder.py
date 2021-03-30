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

    def test_add_title(self):
        """
        it should add the given string to the contents dictionary parameter title
        """
        title = "Some Title"
        expected_item = "# {}".format(title)
        self.assertIsInstance(self.builder.add_title(title), ReportsBuilder)
        self.assertIsNotNone(self.builder.contents["title"])
        self.assertEqual(expected_item, self.builder.contents["title"])

    def test_add_description(self):
        """
        it should add the given string to the contents dictionary parameter description
        """
        description = "some text"
        self.assertIsInstance(self.builder.add_description(description), ReportsBuilder)
        self.assertIsNotNone(self.builder.contents["description"])
        self.assertEqual(description, self.builder.contents["description"])
