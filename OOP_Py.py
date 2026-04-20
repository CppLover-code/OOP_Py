class Person:
    # конструктор
    def __init__(self, name, age):
        print("Создание объекта Person")
        self.name = name
        self.age = age

tom = Person("Tom", 22)


