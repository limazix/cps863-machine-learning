# -*- utf-8 -*-

import os

from unittest import TestCase
from unittest.mock import patch

from tools.reports.block_builder import BlockBuilder


class TestReportsBuilder(TestCase):
    def setUp(self):
        self.builder = BlockBuilder()

    def test_contents(self):
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

    @patch.object(BlockBuilder, "check_empty_field")
    def test_add_empty_paragraph(self, mock_check_empty_field):
        """
        it should raise an exception if no paragraph value is provided
        """
        self.builder.add_paragraph(paragraph=None)
        mock_check_empty_field.assert_called_with(
            None, "Paragraph cannot be empty or null"
        )

        self.builder.add_paragraph(paragraph="")
        mock_check_empty_field.assert_called_with(
            "", "Paragraph cannot be empty or null"
        )

    def test_add_block_paragraph(self):
        """
        it should add the given BlockBuilder instance to the contents dictionary
        parameter body list
        """
        sub_block = BlockBuilder()
        sub_block.add_title("sub title")
        sub_block.add_description("sub description")
        paragraph = sub_block

        self.assertIsInstance(self.builder.add_paragraph(paragraph), BlockBuilder)
        self.assertIsNotNone(self.builder.contents["body"])
        self.assertIn(str(paragraph), self.builder.contents["body"])

    def test_add_paragraph(self):
        """
        it should add the givin string to the contents dictionary parameter body list
        """
        paragraph = "some paragraph"
        self.assertIsInstance(self.builder.add_paragraph(paragraph), BlockBuilder)
        self.assertIsNotNone(self.builder.contents["body"])
        self.assertIn(paragraph, self.builder.contents["body"])

    def test_to_string(self):
        """
        it should transform the block into a markdown string
        """
        title = "Some Title"
        description = "Block description"

        expected_result = "# {}\n\n{}".format(title, description)

        self.builder.add_title(title)
        self.builder.add_description(description)

        self.assertEqual(expected_result, str(self.builder))

    @patch.object(BlockBuilder, "add_paragraph")
    def test_add_image(self, mock_add_paragraph):
        """
        it should add a image path to the document
        """
        image_path = "../../image.png"
        expected_item = "[image]({})".format(image_path)

        self.assertIsInstance(self.builder.add_image(image_path), BlockBuilder)
        mock_add_paragraph.assert_called_with(expected_item)

    def test_to_string_with_sub_block(self):
        """
        it should transform the block with sub blocks into a markdown string
        """
        title = "Some Title"
        description = "Block description"

        sub_block = BlockBuilder()
        sub_block.add_title("sub title")
        sub_block.add_description("sub description")

        sub_block2 = BlockBuilder()
        sub_block2.add_title("sub title 2")
        sub_block2.add_description("sub description 2")

        expected_result = "# {}\n\n{}\n\n{}\n\n{}".format(
            title, description, str(sub_block), str(sub_block2)
        )

        self.builder.add_title(title).add_description(description).add_paragraph(
            sub_block
        ).add_paragraph(sub_block2)

        self.assertEqual(expected_result, str(self.builder))

    def test_export(self):
        """
        it should create a markdown file to a given output path
        """
        output_path = "../"
        file_name = "report-test.md"

        title = "Some Title"
        description = "Block description"

        sub_block = BlockBuilder()
        sub_block.add_title("sub title")
        sub_block.add_description("sub description")

        sub_block2 = BlockBuilder()
        sub_block2.add_title("sub title 2")
        sub_block2.add_description("sub description 2")

        self.builder.add_title(title).add_description(description).add_paragraph(
            sub_block
        ).add_paragraph(sub_block2).export(file_name=file_name, output_path=output_path)

        path = os.path.abspath(os.path.join(output_path, file_name))
        self.assertTrue(os.path.exists(path))
        self.assertTrue(os.path.isfile(path))
