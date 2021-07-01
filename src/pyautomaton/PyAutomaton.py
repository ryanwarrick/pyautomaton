from pathlib import Path
import typing
import configparser


class PyAutomaton(object):

    def __init__(self, config_parser: configparser.ConfigParser):
        """[summary]

        :param config_parser: [description]
        :type config_parser: configparser.ConfigParser
        """
        self.config_parser = config_parser
