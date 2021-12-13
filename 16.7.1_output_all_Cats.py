# Откройте сайт Дом питомца» и на основе имеющихся в нем данных создайте конструктор класса Cat
# со следующими параметрами: имя, пол, возраст.
# В отдельный файл импортируйте и создайте объект Cat, который выводит имеющихся на сайте котов, с одинаковыми параметрами, но с разными значениями.

from Constructor_Class_Cat import Cat

cats = [{"name": "Барон", "gender": "male", "age": 2},
        {"name": "Сэм", "gender": "male", "age": 2}]

for cat in cats:
        obj_cat = Cat()  # creating object    obj_cat    from the class Cat
        obj_cat.init_from_dict(cat)
        print("name cat", obj_cat.name)
        print("gender cat", obj_cat.gender)
        print("age cat", obj_cat.age)
        print('\n')
