"""клас який склад з 5 полів"""

class univercity():
    def __init__(self, studgroup, number_of_students, number_of_professors, number_of_laborants, number_of_classes):
        self.group = studgroup
        self.students = number_of_students
        self.number_of_professors = number_of_professors
        self.number_of_laborants = number_of_laborants
        self.number_of_classes = number_of_classes
#атрибуты: имена групп, количество студентов
    def studgroup(self):
        return self.group
    def number_of_students(self):
        return self.students
    def number_of_professors(self):
        return self.number_of_professors
    def number_of_laborants(self):
        return self.number_of_laborants
    def number_of_classes(self):
        return self.number_of_classes


group1 = univercity("k-01", 30, 5, 15, 50)
group2 = univercity("c-02", 15, 3, 10, 45)
group3 = univercity("b-03", 20, 6, 8, 33)


print(group1.studgroup(), group2.studgroup(), group3.studgroup())
print(group1.number_of_students(), group2.number_of_students(), group3.number_of_students())

groups = []
groups.append(group1.studgroup())
groups.append(group2.studgroup())
groups.append(group3.studgroup())

print(sorted(groups)) #сортировка по возрастанию
print(sorted(groups, reverse=True))#сортировка по убыванию

numbers_of_students = []
numbers_of_students.append(group1.number_of_students())
numbers_of_students.append(group2.number_of_students())
numbers_of_students.append(group3.number_of_students())

print(sorted(numbers_of_students))
print(sorted(numbers_of_students, reverse = True))






