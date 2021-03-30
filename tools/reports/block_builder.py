# -*- utf-8 -*-


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
        if field is None or len(field) <= 0:
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

    def __str__(self):
        """
        Method used to transform the block content into a string
        """
        output = list()
        output.append(self.contents["title"])

        if self.contents["description"]:
            output.append(self.contents["description"])

        return "\n".join(output)
