import os
import configparser

cfg = configparser.ConfigParser()
cfg.read('config.ini')
env = os.getenv('ENV', 'local')


def get_variable(variable, default=None):
    return os.getenv(variable, cfg[env].get(variable, default))
