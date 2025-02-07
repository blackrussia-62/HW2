class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} кушает.")
    
    def sleep(self):
        print(f"{self.name} спит.")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} мяукает: Мяу!")
    
    def scratch(self):
        print(f"{self.name} точит когти.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} лает: Гав!")
    
    def fetch(self):
        print(f"{self.name} приносит палку.")

cat = Cat("кошако", 3)
cat.eat()
cat.sleep()
cat.meow()
cat.scratch()

dog = Dog("гафыч", 5)
dog.eat()
dog.sleep()
dog.bark()
dog.fetch()
