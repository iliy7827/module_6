"""Задача "Съедобное, несъедобное":"""
class Animal:  #родительский класс
    alive = True #живой
    fed = False  #накормленный
    def __init__(self,name):
        self.name = name

    def eat(self, food):
        self.food = food
        if food.edible: # если растение съедобное вывести съел
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:       # если же нет вывести не стал есть
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Plant:   #родительский класс
    edible = False  #съедобность
    def __init__(self,name):
        self.name = name

class Mammal(Animal):  #дочерний класс от Animal
    pass

class Predator(Animal): #дочерний класс от Animal
    pass

class Flower(Plant): #дочерний класс от Plant
    def __init__(self, name):
        super().__init__(name) #вызываем конструктор родительского класса для инициализации
        self.edible = False # переопределям


class Fruit(Plant): #дочерний класс от Plant
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.