class Fruit:
    def __init__(self, price, colour, taste):
        self.price = price
        self.colour = colour
        self.taste = taste

    def ripe(self):
        print('This fruit is ripe.')

    def spoiled(self):
        print('This fruit is already spoiled.')

apple = Fruit(5, 'red', 'Sweet')
lemon = Fruit(6, 'yellow', 'sour')

print('Apple Price: RM ' + str(apple.price))
print('Apple Colour: ' + str(apple.colour))
print('Apple Taste: RM ' + str(apple.taste))

apple.ripe()
lemon.spoiled()
