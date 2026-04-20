# Перегрузка опертора сложения
class Counter:
    def __init__(self, value):
        self.value = value
    # Переопределение оператора сложения
    def __add__(self, other):
        return Counter(self.value + other.value)
    
counter1 = Counter(5)
counter2 = Counter(16)
counter3 = counter1 + counter2
print(counter3.value)

# Истинность объекта
class Count:
    def __init__(self, value):
        self.value = value
    def __bool__(self):
        return self.value > 0
     
def test(counter):
    if counter: print("Counter = True")
    else: print("Counter = False")
     
counter1 = Count(3)
test(counter1)              # Counter = True
 
counter2 = Count(-3)
test(counter2)              # Counter = False

# Операции обращения по индексу obj[index]
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
         
    # Операции обращения по индексу obj[index]
    def __getitem__(self, prop):
        if prop == "name": return self.__name
        elif prop == "age": return self.__age
        return None
    
    # Проверка наличия свойства
    def __contains__(self, prop):
        if prop == "name" or prop == "age": return True
        return False
     
tom = Person("Tom", 39)
 
print("Name:", tom["name"])     # Name: Tom
print("Age:", tom["age"])       # Age: 39
print("Id:", tom["id"])         # Id: None

bob = Person("Bob", 39)
print("name" in bob)        # True
print("id" in bob)          # False