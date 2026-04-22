# Множества
# Множество (set) представляют еще один вид набора, который хранит 
# только уникальные элементы. Для определения множества используются
# фигурные скобки, в которых перечисляются элементы

users = {"Tom", "Bob", "Alice", "Tom"}
print(users)    # {"Alice", "Bob", "Tom"}

people = ["Mike", "Bill", "Ted"]
users = set(people)
print(users)    # {"Mike", "Bill", "Ted"}

users = set() # пустое множество

# Добавление элементов
users.add("Sam")
print(users)
print(len(users))

# Удаление элементов
users = {"Tom", "Bob", "Alice"}
 
user = "Tom"
if user in users: 
    users.remove(user)
print(users)    # {"Bob", "Alice"}

# Также для удаления можно использовать метод discard(), 
# который не будет генерировать исключения при отсутствии элемента
users = {"Tom", "Bob", "Alice"}
 
users.discard("Tim")    # элемент "Tim" отсутствует, и метод ничего не делает
print(users)    #  {"Tom", "Bob", "Alice"}
 
users.discard("Tom")    # элемент "Tom" есть, и метод удаляет элемент
print(users)    #  {"Bob", "Alice"}

users.clear() # удаление всех элементов

# Перебор множества
users = {"Tom", "Bob", "Alice"}
 
for user in users:
    print(user)

# Операции с множествами
users = {"Tom", "Bob", "Alice"}
students = users.copy()
print(students)     # {"Tom", "Bob", "Alice"}

# Объединение множеств
# Метод union() объединяет два множества и возвращает новое множество:
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
 
users3 = users.union(users2)
print(users3)   # {"Bob", "Alice", "Sam", "Kate", "Tom"}

# Вместо метода union() мы могли бы использовать операцию логического сложения - |:
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
 
print(users | users2)   # {"Bob", "Alice", "Sam", "Kate", "Tom"}

# Пересечение множеств
# Пересечение множеств позволяет получить только те элементы, которые 
# есть одновременно в обоих множествах. Метод intersection() производит 
# операцию пересечения множеств и возвращает новое множество
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
 
users3 = users.intersection(users2)
print(users3)   # {"Bob"}

# Вместо метода intersection мы могли бы использовать операцию логического умножения:
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
 
print(users & users2)   # {"Bob"}

# Разность множеств
# разность множеств возвращает те элементы, которые есть в первом множестве,
# но отсутствуют во втором. Для получения разности множеств можно использовать
# метод difference или операцию вычитания:
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
 
users3 = users.difference(users2)
print(users3)           # {"Tom", "Alice"}
print(users - users2)   # {"Tom", "Alice"}

"""
Отдельная разновидность разности множеств - симметрическая разность производится 
с помощью метода symmetric_difference() или с помощью операции ^. Она возвращает 
все элементы обоих множеств за исключением общих:
"""
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
 
users3 = users.symmetric_difference(users2)
print(users3)   # {"Tom", "Alice", "Sam", "Kate"}
 
users4 = users ^ users2
print(users4)   # {"Tom", "Alice", "Sam", "Kate"}

# Отношения между множествами
# Метод issubset позволяет выяснить, является ли текущее множество подмножеством 
# (то есть частью) другого множества

users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
 
print(users.issubset(superusers))   # True
print(superusers.issubset(users))   # False

# Метод issuperset, наоборот, возвращает True, если текущее множество является 
# надмножеством (то есть содержит) для другого множества
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
 
print(users.issuperset(superusers))   # False
print(superusers.issuperset(users))   # True

# frozen set
# Тип frozen set является видом множеств, которое не может быть изменено. Для его 
# создания используется функция frozenset

users = frozenset({"Tom", "Bob", "Alice"})
# В функцию frozenset передается набор элементов - список, кортеж, другое множество
# В такое множество мы не можем добавить новые элементы, как и удалить из него уже 
# имеющиеся

