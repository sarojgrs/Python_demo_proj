from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def eat(self):
        print("Animal is eating.")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

    def perform_operation(self):
        animal = self.create_animal()
        animal.eat()
        sound = animal.speak()
        print(f"The animal says: {sound}")


class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()


class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()


class MainClass:

    def dogWala():
        dog_factory = DogFactory()
        dog_factory.perform_operation()


# Create objects using the factories
dog_factory = DogFactory()
dog_factory.perform_operation()
# Output:
# Animal is eating.
# The animal says: Woof!

# cat_factory = CatFactory()
# cat_factory.perform_operation()

# Output:
# Animal is eating.
# The animal says: Meow!
