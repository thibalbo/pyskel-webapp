import os
import configparser

cfg = configparser.ConfigParser()


def get_variable(variable, default=None):
    return os.getenv(variable, default)
