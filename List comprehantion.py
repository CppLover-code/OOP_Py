# LIST COMPREHANTION
# Функциональность list comprehension предоставляет более 
# краткий и лаконичный синтаксис для создания списков на 
# основе других наборов данных. Она имеет следующий синтаксис:
# newlist = [expression for item in iterable (if condition)]

# обычный синтаксис
numbers = [-15, 9, 8, 0, -8, -74, 5]
pos_numbers = []
for n in numbers:
    if n > 0:
        pos_numbers.append(n)

print(pos_numbers)

# list comprehantion
numbers = [-9, 89, 0, 12, -6, 77]
pos_numbers = [n for n in numbers if n > 0]
print(pos_numbers)

# Создание списка из словаря
dictionary = {"red": "красный","blue": "синий", "green": "зеленый"}
words = [word for word in dictionary]
print(words)

# Возвращение результата
numbers = [-3, -2, -1, 0, 1, 2, 3]
new_numbers = [n * 2 for n in numbers]
print(new_numbers)      # [-6, -4, -2, 0, 2, 4, 6]

# Но могут быть и более сложные выражения
numbers = [-3, -2, -1, 0, 1, 2, 3]
new_numbers = [n * 2 if n > 0 else n for n in numbers]
print(new_numbers)      # [-3, -2, -1, 0, 2, 4, 6]

# В expression можно производить различные трансформации с данными. 
# Например, возвратим также из словаря значение по ключу:
dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
words = [f"{key}: {dictionary[key]}" for key in dictionary]
print(words)    # ['red: красный', 'blue: синий', 'green: зеленый']

