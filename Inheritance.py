"""
class Person:
 
    def __init__(self, name):
        self.__name = name   # имя человека
 
    @property
    def name(self):
        return self.__name
     
    def display_info(self):
        print(f"Name: {self.__name} ")


class Employee(Person):
    def work(self):
        print(f"{self.name} works")

tom = Employee("Tom")
print(tom.name)
tom.display_info()
tom.work()
"""

""" 
# Множественное наследование
#  класс работника
class Employee:
    def work(self):
        print("Employee works")
 
 
#  класс студента
class Student:
    def study(self):
        print("Student studies")
 
 
class WorkingStudent(Employee, Student):        # Наследование от классов Employee и Student
    pass
 
 
# класс работающего студента
tom = WorkingStudent()
tom.work()      # Employee works
tom.study()     # Student studies
"""

"""
# Переопределение функционала базового класса
class Person:
 
    def __init__(self, name: str):
        self.__name = name   # имя человека
 
    @property
    def name(self):
        return self.__name
 
    def display_info(self):
        print(f"Name: {self.__name}")
    
class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def display_info(self):
        super().display_info()
        print(f"Company: {self.company}")

    def work(self):
        print(f"{self.name} works")

tom = Employee("Tom", "Microsoft")
tom.display_info()
"""

"""
# Проверка типа объекта
class Person:
    # атрибуты класса - общие для всех объектов
    type = "Person"
    description = "Describes a person"
    default_name = "Undefined"
    
    # Если имя человека НЕ будет указано,
    # то при выводе инфо будет указано имя по умолчанию из атрибута класса
    def __init__(self, name):
        if name:
            self.name = name
        else:
            self.name = Person.default_name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
 
    def do_nothing(self):
        print(f"{self.name} does nothing")
 
 
#  класс работника
class Employee(Person):
 
    def work(self):
        print(f"{self.name} works")
 
 
#  класс студента
class Student(Person):
 
    def study(self):
        print(f"{self.name} studies")
 
 
def act(person):
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Employee):
        person.work()
    elif isinstance(person, Person):
        person.do_nothing()
 
elis = Person("")
print(elis.name)
tom = Employee("Tom")
bob = Student("Bob")
sam = Person("Sam")
mia = Student("Mia")
 
act(tom)    # Tom works
act(bob)    # Bob studies
act(sam)    # Sam does nothing
act(mia)
act(elis)
"""

"""
# Статические методы
# Кроме обычных методов класс может определять статические методы.
# Такие методы предваряются аннотацией @staticmethod и относятся в целом к классу.
# Статические методы обычно определяют поведение, которое не зависит от конкретного
# объекта

class Person:
    __type = "Person"
 
    @staticmethod
    def print_type():
        print(Person.__type)
 
 
Person.print_type()     # Person - обращение к статическому методу через имя класса
 
tom = Person()
tom.print_type()     # Person - обращение к статическому методу через имя объекта
"""

# Строковое представление объекта. Класс object
# все классы неявно имеют один общий суперкласс - 
# object и все классы по умолчанию наследуют его методы
# Одним из наиболее используемых методов класса object является 
# метод __str__(). Когда необходимо получить строковое представление
#  объекта или вывести объект в виде строки, то Python как раз вызывает
#  этот метод. И при определении класса хорошей практикой считается 
# переопределение этого метода

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")
    def __str__(self):
        return f"Person name: {self.name} Person age: {self.age}"
tom = Person("Tom", 23)
print(tom)
tom.display_info()
print(tom) # здесь срабатывает перегрузка метода __str__()

