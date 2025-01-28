class Person:
    def __init__(self,name,age):
        self.name = name
        self.age= age

    def displayName(self):
        return f"Person name is {self.name} and age is {self.age}"
    

person = Person('Anamol Soman',26)

print(person.displayName())
        