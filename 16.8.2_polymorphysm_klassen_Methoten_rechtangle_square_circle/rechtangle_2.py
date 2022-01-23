from rechtangle import Rechtangle, Square, Circle

#  далее создаём два прямоугольника

recht_1 = Rechtangle(3,4)
recht_2 = Rechtangle(12,5)

# площади двух прямоугольников
print(recht_1.get_area())
print(recht_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

# создаём круг
krug = Circle(3)
print(krug.get_area_circle())

figures = [recht_1, recht_2, square_1, square_2, krug]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rechtangle):
        print(figure.get_area())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())