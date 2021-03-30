# -*- utf-8 -*-


class ReportsBuilder:
    """
    Class designed on the builder pattern to create reports interactively

    :param dict contents: it stores the report contents
    """

    def __init__(self):
        self.contents = dict()

    def add_report_title(self, title):
        """
        Method used to define the report's title by add the given string to the
        dictionary.

        :param str title: Report Title

        :return: the instance of the class
        """
        self.contents["title"] = "# {}".format(title)
        return self

    def add_report_overview(self, text):
        """
        Method used to define the report's overview by add the given string to the
        dictionary.

        :param str title: Report Overview

        :return: the instance of the class
        """
        self.contents["overview"] = text
        return self
