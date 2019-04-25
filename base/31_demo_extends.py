class Animal():
    def run(self):
        print('Animal is running')

class Cat(Animal):
    def run(self):
        print('cat is running')

class Dog(Animal):
    def run(self):
        print('dog is running')

def run_twice(animal):
    animal.run()
    animal.run()

if __name__ == '__main__':
    cat = Cat()
    dog = Dog()
    cat.run()
    dog.run()
    run_twice(Animal())
    run_twice(cat)
    run_twice(dog)