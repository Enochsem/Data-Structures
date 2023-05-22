# when you implement a class try using atleast __repr__()
"""so that usefull information is got when built in functions are called eg: repr(), print() ..."""

''' classes created without special methods return information like
<__main__.OBJECTorClassName at 0x000125565840>

the above is the class and its id or object id in hex
'''

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'Person("{self.name}", {self.age})'

    def __str__(self):
        return f'The person is called {self.name} and is {self.age} old'
    



if __name__ == "__main__" :
    person1 = Person("Enoch", 29)

    print(person1.__str__())
    print(str(person1))

    print(person1.__repr__())