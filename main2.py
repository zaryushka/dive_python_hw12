# Создайте класс-генератор. Экземпляр класса должен генерировать факториал числа 
# в диапазоне от start до stop с шагом step. Если переданы два параметра, считаем step=1. 
# Если передан один параметр, также считаем start=1.

class Fact_gen:
    def __init__(self, *args):
        if len(args) == 3:
            self.start, self.stop, self.step = args
        elif len(args) == 2:
            self.start, self.stop = args
            self.step = 1
        else:
            self.stop = args[0]
            self.start = 1
            self.step = 1


    def __iter__(self):
        return self


    def __next__(self):
        while self.start < self.stop:
            fact = 1
            for num in range(1, self.start + 1):
                fact *= num
            self.start += self.step
            return fact
        raise StopIteration


gener = Fact_gen(1, 50)
for fact in gener:
    print(fact)