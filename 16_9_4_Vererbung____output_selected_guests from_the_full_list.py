# Вам необходимо написать программу, которая позволяла бы составлять список нескольких гостей.
#  Решите задачу с помощью метода конструктора и примените один из принципов наследования.
# При выводе в консоль вы должны получить:  “Иван Петров, г.Москва, статус "Наставник"

# your programm-code should perform a list of some selected guests (from the list of all vollunteers, here list: all_volunteers_datas).
# Solve the problem with a constructor method and apply one of the principles of inheritance.
# When outputting to the console, you should get: “Ivanov, Moscow, status "Mentor"

class Volunteer:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'{self.name}'

class Guest(Volunteer):
    def __init__(self, name: str, place: str, status: str):
        super().__init__(name)                                   # Обеспечивает доступ к оригиналам наследованных методов. Это полезно для доступа к унаследованным методам, которые были переопределены в классе.
        self.place = place
        self.status = status

    def __str__(self):
        return f'{self.name}, {self.place}, {self.status}'

all_volunteers_datas = [
        {"name": "Ivanov", "place": "Moscow", "status": 'Consultant'},
        {"name": "Petrov", "place": "St. Petersburg", "status": 'Mentor'},
	    {"name": "Schwarz", "place": "Viena", "status": 'Trainer'}]

print('list of selected guests :')
for all_volunteers_data in all_volunteers_datas:
    if all_volunteers_data['name'] in ['Petrov', 'Schwarz']:
        selected_guests = Guest(all_volunteers_data['name'], all_volunteers_data['place'], all_volunteers_data['status'])
        print(selected_guests)

