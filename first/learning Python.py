


def sandwich(func):
    def wrapper(*args, **kwargs):
        up = '---- Верхний ломтик хлеба ----'
        down = '---- Нижний ломтик хлеба ----'
        print(up)
        return func(*args, **kwargs)
        print(down)
        return
    return wrapper


@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))

add_ingredients(['томат', 'салат', 'сыр', 'бекон'])


@sandwich
def beegeek():
    return 'beegeek'


print(beegeek())