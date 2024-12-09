class House:
    def __init__(self, name, number_of_floors): # Инициализируем атрибуты объекта
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor): # Проверка на допустимость этажа
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        for i in range(1, new_floor + 1):
            if new_floor < self.number_of_floors:
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, '
                f'Кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other



    def __add__(self, value):
        new_number = self.number_of_floors
        if isinstance(value, House):
            new_number += value.number_of_floors
        elif isinstance(value, int):
            new_number += value
        else:
            return NotImplemented
        return House(self.name, new_number)

    def __iadd__(self, other):
        return self + other

    def __radd__(self, other):
        return self.__add__(other)

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        return  self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

# __eq__
print(h1==h2)

#__add__
h1 = h1 + 10
print(h1)
print(h1==h2)

#__iadd__
h1+= 10
print(h1)

#__radd__
h2 = 10 + h2
print(h2)

print(h1>h2)# __gt__

print(h1 >= h2) # __ge__

print(h1 < h2) # __lt__

print(h1 <= h2) # __le__

print(h1 != h2) # __ne__
