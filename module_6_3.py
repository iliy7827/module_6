'''Задача "Мифическое наследование":'''
class Horse:  #Класс лошадь

    def __init__(self):
        self.x_distance = 0   #пройденный путь
        self.sound = 'Frrr'   #звук, который издаёт лошадь

    def run(self, dx):
        self.x_distance += dx   #увеличивает путь на dx

class Eagle:    #Класс орел

    def __init__(self):
        self.y_distance = 0  #высота полёта
        self.sound = 'I train, eat, sleep and repeat'  #вук, который издаёт орёл
    def fly(self, dy):   #увеличивает высоту на dy
        self.y_distance += dy

class Pegasus(Horse, Eagle):    #Класс Пегаса наследуется от Horse и Eagle
    def __init__(self):
        super().__init__()
        Eagle.__init__(self)
    def move(self, dx, dy):  #изменение дистанции
        self.run(dx)
        self.fly(dy)

    def get_pos(self):    #возвращаем положение пегаса в виде кортежа
        return self.x_distance, self.y_distance

    def voice(self):  #выводим значение унаследованного атрибута sound
        print(self.sound)



p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()