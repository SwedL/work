
from collections import ChainMap


def deep_update(chainmap, key, value):
    if key in sorted(chainmap.parents.keys()):
        for i in chainmap.maps[1:]:
            i[key] = value
    else:
        chainmap[key] = value




chainmap = ChainMap({})

print(deep_update(chainmap, 'city', 'Moscow'))


