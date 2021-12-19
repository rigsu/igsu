# Напишите код для описания геометрической фигуры.
# Создайте класс «прямоугольник» с помощью метода  __init__().
# На выходе в консоли вам необходимо получить длину и ширину с итоговыми значениями.

class Rechtangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rechtangle_area(self):
        return self.length*self.width

newRechtangle = Rechtangle(12, 10)
print(newRechtangle.rechtangle_area())
