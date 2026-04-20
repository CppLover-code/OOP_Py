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

# Переопределение функционала базового класса
