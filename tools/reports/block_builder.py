# -*- utf-8 -*-


class BlockBuilder:
    """
    Class designed on the builder pattern to create reports interactively

    :param dict contents: it stores the report contents
    """

    def __init__(self):
        self.contents = dict()

    def check_empty_field(self, field, error_message):
        """
        Method used to check if a given field is empty or none

        :param field: Field to check
        :param error_message: Message to raises if the given field is empty or none

        :raises: AttributeError
        """
        if field is None or len(field) <= 0:
            raise AttributeError(error_message)

    def add_title(self, title):
        """
        Method used to define the block's title by add the given string to the
        dictionary.

        :param str title: Block's title

        :return: the instance of the class
        """
        self.check_empty_field(title, "Title cannot be empty or null")
        self.contents["title"] = "# {}".format(title)
        return self

    def add_description(self, text):
        """
        Method used to define the block's description by add the given string to the
        dictionary.

        :param str text: Block's description

        :return: the instance of the class
        """
        self.check_empty_field(text, "Description cannot be empty or null")
        self.contents["description"] = text
        return self
