# Распаковка (unpacking, также называемая Деструктуризация) представляет 
# разложение коллекции (кортежа, списка и т.д.) на отдельные значения.

# Python поддерживает концепцию множественного присваивания

# присваивем значения сразу двум переменным. Присвоение идет по позиции:
# переменная x получает значение 1, а переменная y - значениe 2
x, y = 1,2
print(x)
print(y)

name, age, company = ("Tom", 38, "Google") # деструктуризация кортежа
print(name)         # Tom
print(age)          # 38
print(company)      # Google

people = ["Tom", "Bob", "Sam"] # деструктуризация списка
first, second, third = people
print(first)      # Tom
print(second)     # Bob
print(third)      # Sam

# При разложении словаря переменные получают ключи словаря:
dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
r, b, g = dictionary
print(r)    # red
print(b)    # blue
print(g)    # green
# получаем значение по ключу
print(dictionary[g])    # зеленый

# Деструктуризация в циклах

# перебор списка кортежей people
people = [
    ("Tom", 38, "Google"),
    ("Bob", 42, "Microsoft"),
    ("Sam", 29, "JetBrains")
]
 
for name, age, company in people:
    print(f"Name: {name}, Age: {age}, Company: {company}")

# функция enumerate(). Она принимает в качестве параметра коллекцию, 
# создает для каждого элемента кортеж и возвращает набор из подобных 
# кортежей. Каждый кортеж содержит индекс, который увеличивается с 
# каждой итерацией

people = ["Tom", "Bob", "Sam"]
for index, name in enumerate(people):
    print(f"{index}.{name}")
 
# результат
# 0.Tom
# 1.Bob
# 2.Sam
 
# Игнорирование значений, переменная с именем _ (прочерк)
person =("Tom", 38, "Google")
name, _, company = person
print(name)     # Tom
print(company)  # Google
# Здесь нам не важен второй элемент кортежа, поэтому для него 
# определяем переменную _. Хотя в реальности _ - такое же действительное 
# имя, как name и company:
name, _, company = person
print(_)     # 38

# Упаковка значений и оператор *
# Оператор * упаковывает значение в коллекцию
num1=1
num2=2
num3=3
*numbers,=num1,num2,num3 # чтобы получить список, после numbers указывается запятая
print(numbers)  #[1, 2, 3]

# Как правило, упаковка применяется для сбора значений, которые остались после 
# присвоения результатов деструктуризации. Например:
head, *tail = [1, 2, 3, 4, 5]
 
print(head)  # 1
print(tail)  # [2, 3, 4, 5]

# Аналогичным образом можно получить все кроме последнего:
*head, tail = [1, 2, 3, 4, 5]
 
print(head)  # [1, 2, 3, 4]
print(tail)  # 5

# Или элементы по середине, кроме первого и последнего:
head, *middle, tail = [1, 2, 3, 4, 5]
 
print(head)    # 1
print(middle)  # [2, 3, 4]
print(tail)    # 5

# Или все кроме первого и второго:
first, second, *other = [1, 2, 3, 4, 5]
 
print(first)    # 1
print(second)   # 2
print(other)    # [3, 4, 5]

# Другой пример с больщим количеством элементов
first, _, third, *_, last = [1, 2, 3, 4, 5, 6, 7, 8]
 
print(first)   # 1
print(third)   # 3
print(last)    # 8

# Также можно получить ключи словаря:
red, *other, green = {"red":"красный", "blue":"синий", "yellow":"желтый", "green":"зеленый"}
 
print(red)          # red
print(green)        # green
print(other)        # ['blue', 'yellow']

# Распаковка и операторы * и **
# Оператор * вместе с оператором ** также может применяться для распаковки значений. 
# Оператор * используется для распаковки кортежей, списков, строк, множеств, а 
# оператор ** - для распаковки словарей. Особенно это может быть полезно, когда 
# на основе одних коллекций создаются другие. Например, распаковка кортежей и списков:
nums1 = [1, 2, 3]
nums2 = (4, 5, 6)
 
# распаковываем список nums1 и кортеж nums2
nums3 = [*nums1, *nums2] 
print(nums3)        # [1, 2, 3, 4, 5, 6]

# Подобным образом раскладываются словари, только применяется оператор **:
dictionary1 = {"red":"красный", "blue":"синий"}
dictionary2 = {"green":"зеленый", "yellow":"желтый"}
 
# распаковываем словари
dictionary3 = {**dictionary1, **dictionary2}
print(dictionary3)  # {'red': 'красный', 'blue': 'синий', 'green': 'зеленый', 'yellow': 'желтый'}

# Упаковка и распаковка в параметрах функций
"""
Термины args и kwargs — это соглашения по программированию на Python, в реальности
вместо них можно использовать любые именования. *args представляет параметры, 
которые передаются по позиции. А **kwargs означает параметры, которые передаются 
по имени. обозначает аргументы ключевого слова.
Оператор * применяется с любым итерируемым объектом (например, кортежем, списком 
и строками). Тогда как оператор ** можно использовать только со словарями.
"""

# *args
# Оператор * позволяет передать в функцию несколько значений, и все они будут упакованы в кортеж:
def fun(*args):
    # обращаемся к первому элементу кортежа
    print(args[0])
  
    # выводим весь кортеж
    print(args)
  
fun("Python", "C++", "Java", "C#")

# Оператор **
# Оператор ** упаковывает аргументы, переданные по имени, в словарь. 
# Имена параметров служат ключами. Например, определим функцию, 
# которая просто будет выводить все переданные параметры
def fun(**kwargs):
    print(kwargs)   # выводим словарь на консоль
  
fun(name="Tom", age="38", company="Google")
fun(language="Python", version="3.11")

def fun(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
  
fun(name="Tom", age="38", company="Google")

# Распаковка аргументов
# Оператор * и распаковка
def sum(*args):
  result = 0
  for arg in args:
    result += arg
  return result
  
numbers = (1, 2, 3, 4, 5)
# применяем распаковку - *numbers, иначе TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
print(sum(*numbers))     # 15

# Другим случаем распаковки может быть ситуация, когда функция принимает несколько параметров, а мы 
# передаем один кортеж или список
def print_person(name, age, company):
  print(f"Name:{name}, Age: {age}, Company: {company}")
  
person =("Tom", 38, "Google")
# выполняем распаковку кортежа person
print_person(*person)   # Name:Tom, Age: 38, Company: Google

# Оператор ** и распаковка
# Оператор ** применяется для распаковки словарей:
def print_person(name, age, company):
  print(f"Name:{name}, Age: {age}, Company: {company}")
  
tom ={"name":"Tom", "age":38, "company":"Google"}
# выполняем распаковку словаря tom
print_person(**tom) # Name:Tom, Age: 38, Company: Google

bob ={"name":"Bob", "age":44, "company":"Luxsoft"}
# выполняем распаковку словаря tom
print_person(**bob) 

# Сочетание параметров
# Параметры *args и *kwargs могут использоваться в функции вместе с другими параметрами. Например
def sum(num1, num2, *nums):
    result=num1+num2
    for n in nums:
        result += n
    return result
 
print(sum(1,2,3))       # 6
print(sum(1,2,3,4))     # 10

# ВСТРОЕННАЯ ФУНКЦИЯ zip() 
"""
Встроенная функция zip() в Python позволяет объединить элементы из нескольких
коллекций (таких как списки, словари, кортежи или строки) в один набор кортежей. 
Объединяемые коллекции передаются в качестве параметра через запятую
	
zip(*iterables)

В качестве результата функция возвращает итератор на набор кортежей, где каждый 
кортеж содержит элементы из соответствующей позиции коллекций-параметров. 
Например, 1-й кортеж содержит 1-е элементы из каждой коллекции, 2-й кортеж 
содержит 2-е элементы из каждой коллекции и так далее. Причем итератор 
останавливается, когда завершается самая короткая коллекция-параметр. 
То есть по сути на выходе мы получим набор, где количество кортежей равно 
количеству элементов в наименьшей объединяемой коллекции.
"""
names = ["Tom", "Bob", "Sam"]
ages = [41, 46, 35]
 
for user in zip(names, ages):
    print(user)
 
# Консольный вывод
# ("Tom", 41)
# ("Bob", 46)
# ("Sam", 35)

# мы можем сразу разложить полученный кортеж на отдельные переменные:
names = ["Tom", "Bob", "Sam"]
ages = [41, 46, 35]
 
for name, age in zip(names, ages):
    print(f"Name: {name}  Age: {age}")
 
# Консольный вывод
# Name: Tom  Age: 41
# Name: Bob  Age: 46
# Name: Sam  Age: 35

# Также мы могли бы получить результат функции в отдельную переменную и затем ее перебрать:
names = ["Tom", "Bob", "Sam"]
ages = [41, 46, 35]
 
users = zip(names, ages)
print(users)        # <zip object at 0x7c2307627c40>
 
for user in users:
    print(user)

# Объединение списков
names = ["Tom", "Bob", "Sam"]
ages = [41, 46, 35]   
 
users = list(zip(names, ages)) 
print(users)        # [("Tom", 41), ("Bob", 46), ("Sam", 35)]
 
for user in users:
    print(user)
 
# Консольный вывод
# ("Tom", 41)
# ("Bob", 46)
# ("Sam", 35)

# ///////////////////////////////////////////////
names = ["Tom", "Bob", "Sam"]
ages = [41, 46, 35]   
companies = ["Sber", "VK", "Yandex"]
 
users = list(zip(names, ages, companies)) 
print(users)        # [("Tom", 41, "Sber"), ("Bob", 46, "VK"), ("Sam", 35, "Yandex")]
 
for user in users:
    print(user)
 
# Консольный вывод
# ("Tom", 41, "Sber")
# ("Bob", 46, "VK")
# ("Sam", 35, "Yandex")

# Разложение списка кортежей
sers = [("Tom", 41), ("Bob", 46), ("Sam", 35)]
 
names, ages = zip(*users)
 
print(names)    # ("Tom", "Bob", "Sam")
print(ages)     # (41, 46, 35)

# Одновременный перебор нескольких списков
names = ["Tom", "Bob", "Sam"]
ages = [41, 46, 35]
 
for name, age in zip(names, ages):
    print(f"Name: {name}  Age: {age}")
 
# Консольный вывод
# Name: Tom  Age: 41
# Name: Bob  Age: 46
# Name: Sam  Age: 35

# Создание словарей
keys = ["name", "age", "city"]
values = ["Tom", 41, "Volgograd"]
 
user = dict(zip(keys, values))
print(user)  # {"name": "Tom", "age": 41, "city": "Volgograd"}

# Работа с диапазонами
# Объединение диапазонов или последовательностей:
numbers = range(1, 4)
letters = ["a", "b", "c"]
 
result = list(zip(numbers, letters))
print(result)  # [(1, "a"), (2, "b"), (3, "c")]

# Сравнение элементов в списках
list1 = [1, 2, 3]
list2 = [1, 4, 3]
 
comparison = [a == b for a, b in zip(list1, list2)]
print(comparison)   # [True, False, True]
