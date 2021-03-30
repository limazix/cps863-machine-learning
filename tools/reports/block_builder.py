# -*- utf-8 -*-


class BlockBuilder:
    """
    Class designed on the builder pattern to create reports interactively

    :param dict contents: it stores the report contents
    """

    def __init__(self):
        self.contents = dict()

    def add_title(self, title):
        """
        Method used to define the block's title by add the given string to the
        dictionary.

        :param str title: Block's title

        :return: the instance of the class
        """
        if title is None or len(title) <= 0:
            raise AttributeError("Title cannot be empty or null")

        self.contents["title"] = "# {}".format(title)
        return self

    def add_description(self, text):
        """
        Method used to define the block's description by add the given string to the
        dictionary.

        :param str title: Block's description

        :return: the instance of the class
        """
        self.contents["description"] = text
        return self
