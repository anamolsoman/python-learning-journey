class Person:
    def __init__(self,name,age):
        self.name = name
        self.age= age

    def displayName(self):
        return f"Person name is {self.name} and age is {self.age}"
    
class Job(Person):
    def __init__(self,name,age,job):
        super().__init__(name,age)
        self.job = job
    
    def displayEmployeeInfo(self):
        return f"Person name is {self.name} and age is {self.age} and he work as {self.job}"

job = Job('Anamol Soman',26,'Software Developer')

print(job.displayEmployeeInfo())
        