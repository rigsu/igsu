# given is the list 'works' with collection of workPackages/workParts. Asked is to select und to print
# the given workPackages (in this case: positions 1, 2, 3 of the list 'works')
# and to add/sum the costs from the selected workPackages and to print the sum

class Work:
    def __init__(self, name="", activity="", costs=0):
        self.name = name
        self.activity = activity
        self.costs = costs
works = [{"name": "Max Must", "activity": "Software development 1", "costs": 100},
         {"name": "Peter Beisp", "activity": "Software development 1", "costs": 95},
         {"name": "Jacky Sparrowson", "activity": "Management", "costs": 70},
         {"name": "Tonia Tirolsenia", "activity": "Software Testing area 1", "costs": 85},
         {"name": "Antony Tirolsen", "activity": "Software Testing area 2", "costs": 80},
         {"name": "Mister A", "activity": "buying materials group A", "costs": 35},
         {"name": "Mister X", "activity": "buying materials group B", "costs": 35},
         {"name": "Mister Y", "activity": "buying materials group Y", "costs": 30},
         {"name": "Mister Z", "activity": "buying materials group Z", "costs": 25}]
obj_lst = []
for work in works:
    obj_lst.append(Work(**work))

for i in range(1, 4):
    print("name work:", obj_lst[i].name)
    print("activity work:", obj_lst[i].activity)
    print("costs work:", obj_lst[i].costs)
    print('\n')

out = sum(i['costs'] for i in works[1:4])
print(out)