# -*- utf-8 -*-

"""
.. module:: reports_builder
    :synopsis: Module created to handle report building tasks
    :platform: OpenSuse 15.2 on WSL2 (Windows 10)
.. moduleauthor:: Bruno Lima <blcardoso@cos.ufrj.br>
"""


class ReportsBuilder:
    """
    Class designed on the builder pattern to create reports interactively

    :param contents: it stores the report contents
    """

    def __init__(self):
        self.contents = ""
