# -*- utf-8 -*-

from unittest import TestCase

from tools.reports.reports_builder import ReportsBuilder


class TestReportsBuilder(TestCase):
    def setUp(self):
        self.builder = ReportsBuilder()

    def test_report_contents(self):
        """
        it should have a string property contents to store the report contents
        """
        self.assertIsNotNone(self.builder.contents)
        self.assertIsInstance(self.builder.contents, str)
