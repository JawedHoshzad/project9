class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def print_name(self):
        return f"{self.name} {self.last_name}"

p1 = Person("Ali", "Rezaei")
print(p1.print_name())

