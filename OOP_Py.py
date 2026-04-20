class Person:
    # конструктор
    def __init__(self, name, age):
        print("Создание объекта Person")
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Person name: {self.name}\nPerson age: {self.age}")

    def person_say(self, message):
        print(f"{self.name} say: \"{message}\"")

    def __del__(self):
        print("Удалён человек с именем", self.name)


tom = Person("Tom", 22)
print(tom.name)
print(tom.age)
tom.age = 37
print(tom.age)

tom.print_info()
tom.person_say("Hello, friends")

def create_person():
    bob = Person("Bobby", 35)

create_person()
print("Конец программы")






