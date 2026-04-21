"""
Список (list) представляет тип данных, который хранит
набор или последовательность элементов. 
"""

# СОЗДАНИЕ СПИСКА
numbers = [1, 2, 3, 4, 5]
people = ["Tom", "Sam", "Bob"]

# Также для создания списка можно использовать функцию-конструктор list():
numbers1 = [] # empty list
numbers2 = list() # empty list

# Список может содержать объекты разных типов данных
objects = [1, 2.6, "Hello", True]

print(numbers)
print(people)

# Конструктор list может принимать набор значений, на основе которых создается список
letters = list("Hello")
print(letters)      # ['H', 'e', 'l', 'l', 'o']

# Создаем список, в котором повторяется одно и то же значение несколько раз
numbers = [5] * 6   # 6 раз повторяем 5
print(numbers)      # [5, 5, 5, 5, 5, 5]
 
people = ["Tom"] * 3    # 3 раза повторяем "Tom"
print(people)           # ["Tom", "Tom", "Tom"]
 
students = ["Bob", "Sam"] * 2   # 2 раза повторяем "Bob", "Sam"
print(students)

# ОБРАЩЕНИЕ К ЭЛЕМЕНТАМ СПИСКА
"""
Для обращения к элементам списка надо использовать индексы,
которые представляют номер элемента в списка. Индексы начинаются
с нуля. То есть первый элемент будет иметь индекс 0, второй элемент -
индекс 1 и так далее. Для обращения к элементам с конца можно
использовать отрицательные индексы, начиная с -1. То есть у последнего
элемента будет индекс -1, у предпоследнего - -2 и так далее.
"""

people = ["Tom", "Sam", "Bob"]
print(people[0])
print(people[1])
print(people[2])
print(people[-2])
print(people[-1])
print(people[-3])

# изменение элемента списка
people[1] = "Mike"  # изменение второго элемента
print(people[1])    # Mike
print(people)       # ["Tom", "Mike", "Bob"]

# Python позволяет разложить список на отдельные элементы:
people = ["Tom", "Bob", "Sam"]
 
tom, bob, sam = people
 
print(tom)      # Tom
print(bob)      # Bob
print(sam)      # Sam

# Перебор элементов

people = ["Tom", "Sam", "Bob"]
for person in people:
    print(person)

i = 0
while i <len(people):
    print(people[i])
    i+=1

# Сравнение списков
# Два списка считаются равными, если они содержат один и тот же набор элементов

numbers1 = [1, 2, 3, 4, 5]
numbers2 = list([1, 2, 3, 4, 5])
if numbers1 == numbers2:
    print("numbers1 equal to numbers2")
else:
    print("numbers1 is NOT equal to numbers2")

# Получение части списка
people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
 
slice_people1 = people[:3]   # с 0 по 3
print(slice_people1)   # ["Tom", "Bob", "Alice"]
 
slice_people2 = people[1:3]   # с 1 по 3
print(slice_people2)   # ["Bob", "Alice"]
 
slice_people3 = people[1:6:2]   # с 1 по 6 с шагом 2
print(slice_people3)   # ["Bob", "Sam", "Bill"]

slice_people4 = people[0:5:2]
print(slice_people4)

# Методы и функции по работе со списками

cars = ["Toyota", "Geely"]
 
# добавляем в конец списка
cars.append("Mers")
# добавляем на вторую позицию
cars.insert(0,"Nissan")
# добавляем набор элементов 
cars.extend(["Volvo", "Lincoln"])
print(cars)
# получаем индекс элемента
ind_toyota = cars.index("Toyota")
# удаляем по этому индексу
removed_item = cars.pop(ind_toyota)
# удаляем последний элемент
last_item = cars.pop()
# удаляем элемент "Geely"
cars.remove("Geely")
print(cars)      
# удаляем все элементы
cars.clear()
print(cars)       # []

# Проверка наличия элемента
people = ["Tom", "Bob", "Alice", "Sam"]
 
if "Alice" in people:
    people.remove("Alice")
print(people)       # ["Tom", "Bob", "Sam"]

# Удаление с помощью del
people = ["Tom", "Bob", "Alice", "Sam", "Bill", "Kate", "Mike"]
 
del people[1]   # удаляем второй элемент
print(people)   # ["Tom", "Alice", "Sam", "Bill", "Kate", "Mike"]
del people[:3]   # удаляем  по четвертый элемент не включая
print(people)   # ["Bill", "Kate", "Mike"]
del people[1:]   # удаляем  со второго элемента
print(people)   # ["Bill"]

# Изменение подсписка
nums = [10, 20, 30, 40, 50]
nums[1:4]=[11, 22]
print(nums)     # [10, 11, 22, 50]

# Подсчет вхождений
numb = [1, 4, 5, 8, 1, 9, 10, 19, 1, 5]
counter = numb.count(1)
print(counter)

# Сортировка
numb.sort()
print(numb)
numb.reverse()
print(numb)

# Фильтрация списка
# Для фильтрации списка применяется функция filter(),
# в которую передается функция-условие и фильтруемый список

numbers = [-5, -4, -3 ,-2, -1, 0, 1, 2, 3, 4, 5]
 
def condition(number): return number > 1
 
result = filter(condition, numbers)
 
for n in result: print(n, end=" ")      # 2 3 4 5



numbers1 = [-5, -4, -3 ,-2, -1, 0, 1, 2, 3, 4, 5]
 
result1 = filter(lambda n: n > 1, numbers1)
 
for n in result1: print(n, end=" ")      # 2 3 4 5

# Фильтрация более сложных объектов
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
         
people = [ Person("Tom", 38), Person("Kate", 31), Person("Bob", 42), 
        Person("Alice", 34),  Person("Sam", 25) ]
 
# фильтрация элементов, у которых age > 33
view = filter(lambda p: p.age > 33, people)
  
for person in view:
    print(f"Name: {person.name} Age: {person.age}")

# Проекция списка
"""
Для проекции/преобразования элементов списка применяется
функция map(), в которую передается функция-условие и список,
элементы которого надо преобразовать.
Из результата функции мы получим преобразованные элементы списка
"""

