url_mapping = {
    'characters.move': {
        'url_pattern': '/my/[name]/action/move',
        'params': {'name', },
    },
    'characters.fight': {
        'url_pattern': '/my/[name]/action/fight',
        'params': {'name', },
    },
    'characters.list': {
        'url_pattern': '/my/characters',
        'params': set(),
    }
}
