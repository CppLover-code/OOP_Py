"""
Список (list) представляет тип данных, который хранит
набор или последовательность элементов. 
"""
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

