# -*- utf-8 -*-

from unittest import TestCase
from unittest.mock import patch

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

    @patch.object(BlockBuilder, "check_empty_field")
    def test_add_empty_title(self, mock_check_empty_field):
        """
        it should raise an exception if no title is provided
        """
        self.builder.add_title(title=None)
        mock_check_empty_field.assert_called_with(None, "Title cannot be empty or null")

        self.builder.add_title(title="")
        mock_check_empty_field.assert_called_with("", "Title cannot be empty or null")

    def test_add_title_tag(self):
        """
        it should add a markdown 'tag' instead of the default '#'
        """
        title = "some title"
        tag = "##"
        expected_item = "{} {}".format(tag, title)
        self.builder.add_title(title=title, tag=tag)
        self.assertEqual(expected_item, self.builder.contents["title"])

    def test_add_description(self):
        """
        it should add the given string to the contents dictionary parameter description
        """
        description = "some text"
        self.assertIsInstance(self.builder.add_description(description), BlockBuilder)
        self.assertIsNotNone(self.builder.contents["description"])
        self.assertEqual(description, self.builder.contents["description"])

    @patch.object(BlockBuilder, "check_empty_field")
    def test_add_empty_description(self, mock_check_empty_field):
        """
        it should raise an exception if no description is provided
        """
        self.builder.add_description(text=None)
        mock_check_empty_field.assert_called_with(
            None, "Description cannot be empty or null"
        )

        self.builder.add_description(text="")
        mock_check_empty_field.assert_called_with(
            "", "Description cannot be empty or null"
        )
