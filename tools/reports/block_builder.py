# -*- utf-8 -*-

import os


class BlockBuilder:
    """
    Class designed on the builder pattern to create reports interactively

    :param contents: it stores the report contents
    :type contents: list.
    """

    def __init__(self):
        self.contents = dict()

    def check_empty_field(self, field, error_message):
        """
        Method used to check if a given field is empty or none

        :param field: Field to check
        :type field: obj.
        :param error_message: Message to raises if the given field is empty or none
        :type error_message: str.

        :raises: AttributeError

        """
        if field is None:
            raise AttributeError(error_message)
        elif isinstance(field, str) and len(field) <= 0:
            raise AttributeError(error_message)

    def add_title(self, title, tag="#"):
        """
        Method used to define the block's title by add the given string to the
        dictionary.

        :param title: Block's title
        :type title: str.

        :return: the instance of the class

        """
        self.check_empty_field(title, "Title cannot be empty or null")
        self.contents["title"] = "{tag} {text}".format(tag=tag, text=title)
        return self

    def add_description(self, text):
        """
        Method used to define the block's description by add the given string to the
        dictionary.

        :param text: Block's description
        :type text: str.

        :return: the instance of the class

        """
        self.check_empty_field(text, "Description cannot be empty or null")
        self.contents["description"] = text
        return self

    def add_paragraph(self, paragraph):
        """
        Method used to insert a paragraph into the block

        :param paragraph: Paragraph to be inserted
        :type paragraph: str

        :return: the instance of the class

        """
        self.check_empty_field(paragraph, "Paragraph cannot be empty or null")
        if "body" not in self.contents.keys():
            self.contents["body"] = list()

        self.contents["body"].append(
            paragraph if isinstance(paragraph, str) else str(paragraph)
        )
        return self

    def add_image(self, image_path):
        """
        Method used to inject an image into the block as a paragraph

        :param image_path: Image path
        :type image_path: str

        :return: the instance of the class

        """
        md_image = "[image]({})".format(image_path)
        self.add_paragraph(md_image)
        return self

    def export(self, file_name, output_path):
        """
        Method used to export the report to a file

        :param file_name: Output file name
        :type file_name: str
        :param output_path: Output folder to store the final file
        :type output_path: str

        :return: the instance of the class

        """
        abs_path = os.path.abspath(os.path.join(output_path, file_name))
        with open(abs_path, "+w") as file:
            file.write(str(self))
        return self

    def __str__(self):
        """
        Method used to transform the block content into a string
        """
        output = list()
        output.append(self.contents["title"])

        if self.contents["description"]:
            output.append(self.contents["description"])

        if "body" in self.contents.keys():
            output.extend(self.contents["body"])

        return "\n\n".join(output)
