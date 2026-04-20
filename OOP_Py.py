class Person:
    # конструктор
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
        print(f"Создание объекта Person с именем {self.__name}")

    # свойство-геттер
    # геттер для получения возраста
    @property
    def age(self):
        return self.__age
    
    # свойство-сеттер
    # сеттер для установки возраста
    @age.setter
    def age(self, age: int):
        if 0 < age <110:
            self.__age = age
        else:
            print("Недопустимый возраст!")
    
    # геттер для получения имени
    @property
    def get_name(self):
        return self.__name

    def print_info(self):
        print(f"Person name: {self.__name}\nPerson age: {self.__age}")

    def person_say(self, message: str):
        print(f"{self.__name} say: \"{message}\"")

    def __del__(self):
        print("Удалён объект Person с именем", self.__name)


tom = Person("Tom", 22)
#print(tom._Person__name)
#print(tom.__age)
#tom.__age = 37
#print(tom.__age)

tom.print_info()
tom.person_say("Hello, friends")
#tom.set_age(-98)
#tom.set_age(28)
tom.age = -57
tom.age = 44

tom.print_info()

def create_person():
    bob = Person("Bobby", 35)

create_person()
print("Конец программы")






