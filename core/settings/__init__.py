from configparser import ConfigParser

from .settings import GameSetup

import os


file = os.path.join(
    os.path.dirname(os.path.abspath('__file__')),
    f'core{os.sep}settings{os.sep}config.ini'
)

config = ConfigParser()

config.read(file)

configurator = GameSetup(config)
