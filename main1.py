# Экземпляр должен запоминать последние k значений. Параметр k передаётся при создании экземпляра. Добавьте метод для просмотра ранее вызываемых чисел и их факториалов.
# Доработаем задачу 1. Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.

import json

class Factorial:
    def __init__(self, k):
        self.k = k
        self.res_list = []

    def __call__(self, num):
        res = 1
        for i in range(1, num + 1):
            res *= i

        self.res_list.append((num, res))
        if len(self.res_list) > self.k:
            self.res_list.pop(0)

        return res
        
    def __str__(self):
        return str(self.res_list)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        my_dict = {}
        for key, value in self.res_list:
            my_dict[key] = value
        with open('res_json.json', 'w', encoding='utf-8') as f_json:
            json.dump(my_dict, f_json)


with Factorial(4) as my_fact:
    print(my_fact(5))
    print(my_fact(6))
    print(my_fact(7))
    print(my_fact(2))
    print(my_fact(10))
    print(my_fact(11))


# my_fact = Factorial(4)
# print(my_fact(5))
# print(my_fact(6))
# print(my_fact(7))
# print(my_fact(2))
# print(my_fact(10))
# print(my_fact(11))
# print(my_fact)