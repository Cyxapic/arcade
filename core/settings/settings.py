import os

from configparser import ConfigParser


class GameSetup:

    file = os.path.join(
        os.path.dirname(os.path.abspath('__file__')),
        f'core{os.sep}settings{os.sep}config.ini'
    )
    config = ConfigParser()

    def __init__(self):
        self.config.read(self.file)

    def get_screen(self):
        return (
            int(self.config['video']['width']),
            int(self.config['video']['height'])
        )

    def get_lvl(self):
        number = self.get_lvl_number
        level_file = f'resourses/levels/level_{number}.lvl'
        with open(level_file) as _file:
            level = _file.readlines()
        return level

    @property
    def get_lvl_number(self):
        return int(self.config['level']['number'])

    @property
    def block_size(self):
        return int(self.config['level']['block'])

    @property
    def db_name(self):
        return self.config['db']['name']

    def set_lvl(self, number):
        self.config.set("level", "number", str(number))
        with open(self.file, 'w') as fp:
            self.config.write(fp)
