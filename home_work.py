# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых. 

import csv

class ValidateName:
    def __init__(self, param):
        self.param = param
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value:str):
        if not value.istitle() or not value.isalpha():
            raise ValueError(f'имя {value} некорректное ')

class Student:

    first_name = ValidateName(str)
    patronymic_name = ValidateName(str)
    last_name = ValidateName(str)

    def __init__(self, first_name, patronymic_name, last_name, subjects):
        self.first_name = first_name
        self.patronymic_name = patronymic_name
        self.last_name = last_name
        self.subjects = subjects

    
    def subjects_dictionary(self, filename):
        self.subjects = {'предметы': {}}
        with open('my_lessons.csv', 'r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.subjects['предметы'][row[0]] = []
        return self.subjects
        
   
    def add_estimate(self, name_sub: str, num: int):
        if num < 2 or num > 5:
            raise ValueError('оценка должна быть в диапазоне от 2 до 5')
        self.subjects['предметы'][name_sub].append(num)



    def midd_estimate(self):
        midd_est_dict = {}
        for name_sub, num in self.subjects['предметы'].items():
            average = round(sum(num) / len(num), 2)
            midd_est_dict[name_sub] = average
        return midd_est_dict

        
    def __repr__(self):
        return f'Student: {self.first_name} {self.patronymic_name} {self.last_name}'


std_1 = Student('Ivan', 'Ivanovich', 'Ivanov', 'my_lessons.csv')
print(std_1)  
print(std_1.first_name)
std_1.subjects_dictionary('my_lessons.csv')
print(std_1.subjects)
std_1.add_estimate('труд', 3)
std_1.add_estimate('труд', 4)
std_1.add_estimate('труд', 2)
std_1.add_estimate('алгебра', 5)
std_1.add_estimate('алгебра', 4)
std_1.add_estimate('алгебра', 5)
std_1.add_estimate('химия', 5)
std_1.add_estimate('химия', 5)
std_1.add_estimate('химия', 5)
print(std_1.subjects)
print(std_1.midd_estimate())
