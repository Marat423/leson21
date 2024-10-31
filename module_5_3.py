class House: # Создаем Класс
    def __init__(self, name, number_is_floors): # Метод и атрибуты
        self.name = name
        self.number_is_floors = number_is_floors

   # def __len__(self):
     #   return self.number_is_floors

    def __str__(self):
        return str(f'Название Жк: {self.name}, кол-во этажей {self.number_is_floors}')
        return name_nambers


    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_is_floors == other.number_is_floors
        elif isinstance(other, int):
            return self.number_is_floors == other


    def __add__(self, value):
        if isinstance(value, int):
            self.number_is_floors += value
            return self

    def __iadd__(self, value):
        self.number_is_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)



    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_is_floors < other.number_is_floors
        elif isinstance(other, int):
            return self.number_is_floors < other
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_is_floors <= other.number_is_floors
        elif isinstance(other, int):
            return self.number_is_floors <= other
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_is_floors > other.number_is_floors
        elif isinstance(other, int):
            return self.number_is_floors > other
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_is_floors >= other.number_is_floors
        elif isinstance(other, int):
            return self.number_is_floors >= other
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_is_floors != other.number_is_floors
        elif isinstance(other, int):
            return self.number_is_floors != other








h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
#print(len(h1))
#print(len(h2))

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
