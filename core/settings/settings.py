class GameSetup:
    def __init__(self, config):
        self.config = config

    def get_screen(self):
        return (
            int(self.config['video']['width']),
            int(self.config['video']['height'])
        )

    def get_lvl(self):
        number = self.config['level']['number']
        level_file = f'resourses/levels/level_{number}.lvl'
        with open(level_file) as _file:
            level = _file.readlines()
        return level

    @property
    def block_size(self):
        return int(self.config['level']['block'])

    def write_lvl(self, lvl):
        pass
