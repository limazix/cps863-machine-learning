# -*- utf-8 -*-

from unittest import TestCase

from tools.reports.block_builder import BlockBuilder


class TestReportsBuilder(TestCase):
    def setUp(self):
        self.builder = BlockBuilder()

    def test_report_contents(self):
        """
        it should have a dictionary property contents to store the report contents
        """
        self.assertIsNotNone(self.builder.contents)
        self.assertIsInstance(self.builder.contents, dict)

    def test_check_empty_field(self):
        """
        it should check if a given field is empty or none and rases an AttributeError
        exception
        """
        error_message = "some error message"
        with self.assertRaises(AttributeError) as error:
            self.builder.check_empty_field(None, error_message)
            self.assertEqual(error_message, error)

    def test_add_title(self):
        """
        it should add the given string to the contents dictionary parameter title
        """
        title = "Some Title"
        expected_item = "# {}".format(title)
        self.assertIsInstance(self.builder.add_title(title), BlockBuilder)
        self.assertIsNotNone(self.builder.contents["title"])
        self.assertEqual(expected_item, self.builder.contents["title"])

    def test_add_empty_title(self):
        """
        it should raise an exception if no title is provided
        """
        with self.assertRaises(AttributeError):
            self.builder.add_title(title=None)
            self.builder.add_title(title="")
            self.builder.add_title()

    def test_add_description(self):
        """
        it should add the given string to the contents dictionary parameter description
        """
        description = "some text"
        self.assertIsInstance(self.builder.add_description(description), BlockBuilder)
        self.assertIsNotNone(self.builder.contents["description"])
        self.assertEqual(description, self.builder.contents["description"])

    def test_add_empty_description(self):
        """
        it should raise an exception if no description is provided
        """
        with self.assertRaises(AttributeError):
            self.builder.add_description(text=None)
            self.builder.add_description(text="")
            self.builder.add_description()
