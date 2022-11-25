


class CardDeck:
    def __init__(self):
        self.suit = ['пики', 'трефы', 'бубны', 'червы']
        self.nom = ['двойка', 'тройка', 'четверка', 'пятерка', 'шестерка', 'семерка',
                    'восьмерка', 'девятка', 'десятка', 'валет', 'дама', 'король', 'туз']
        self.data = [((n, s) for n in self.nom) for s in self.suit]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        return self.data[self.index]


cards = CardDeck()

print(next(cards))
print(next(cards))
