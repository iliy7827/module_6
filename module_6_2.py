'''Задача "Изменять нельзя получать":'''

class Vehicle: # это любой транспорт
    __COLOR_VARIANTS = ['green','yellow', 'black', 'red'] # допустимый цвет для окрашивания
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner     # владелец тр-та (может меняться)
        self.__model = __model # марка тр-та (не меняется)
        self.__engine_power = __engine_power # мощность двигателя (не меняется)
        self.__color = __color # цвет авто (не можем менять)

    def get_model(self):
        return f'модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощьность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'цвет авто: {self.__color}'

    def print_info(self):
        print(self.get_model(), self.get_model(), self.get_color(),f'Владелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = new_color
        if new_color in self.__COLOR_VARIANTS:
            self.__color = self.new_color
        else:
            print(f'Нельзя сменить цвет на {self.new_color}')




class Sedan(Vehicle): # дочерний класс
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()