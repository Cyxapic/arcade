class TileTypes:
    """ Create an object which keep types of Blocks dict
        types -- dict; {tile_name_str: img_name_str} -> {'M': 'image.png'}
    """
    def __init__(self, types: dict):
        self._tile_type = types

    @property
    def get_types(self)-> tuple:
        """ Return tuple of types"""
        return tuple(self._tile_type.keys())

    @property
    def get_types_img(self):
        return self._tile_type


if __name__ == '__main__':
    tile_types = TileTypes({'a': '1', 's': '2'})
    assert tile_types.get_types == ('a', 's')
    assert tile_types.get_types_img == {'a': '1', 's': '2'}
