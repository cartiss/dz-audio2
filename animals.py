class Animals:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self, food):
        self.weight += food
        print(f'{self.name} поел(а)')

class Birds(Animals):
    def collect_eggs(self):
        print(f'Яйца у {self.name} собраны.')

class Cattle(Animals):
    def milking(self):
        if not isinstance(self, Sheep):
            print(f'{self.name} подоена')

class Goose(Birds):
    def sound(self):
        print('Го-го-го')

class Cow(Cattle):
    def sound(self):
        print('Мууууу')

class Sheep(Cattle):
    def cut(self):
        print(f'Овца {self.name} пострижена.')

    def sound(self):
        print('Бееееее')

class Chicken(Birds):
    def sound(self):
        print('Куд-кудах')

class Goat(Cattle):
    def sound(self):
        print('Меееее')

class Duck(Birds):
    def sound(self):
        print('Кря-Кря')

ferm = [Goose('Grey', 3), Goose('White', 2), Cow('Manka', 30), Sheep('Barashek', 15), Sheep('Kydravii', 12), Chicken('Koko', 2), Chicken('Kykareky', 5), Goat('Kopita', 11), Duck('Krakva', 7)]
sum = 0
max = 0
for i in ferm:
    sum += i.weight
    if max < i.weight:
        max = i.weight
print(sum)
print(max)
