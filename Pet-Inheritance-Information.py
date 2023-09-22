# This code follows different types of inheritance while using the "setter" and "getter" function. 
# This code collect's the pet's name, age, and type wherein the type of pet is only limited to cat, dog and bird.

class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        if self.__age == 1:
            return "The age of your pet is " + str(self.__age) + " year old."
        elif -11 <= self.__age < 0:
            return "The age of your pet is " + str(12 - abs(self.__age)) + " month old."
        elif self.__age < -11 or self.__age >= 21:
            return "Invalid age value!"
        elif self.__age < 1:
            return "The age of your pet is " + str(12 - abs(self.__age)) + " months old."
        else:
            return "The age of your pet is " + str(self.__age) + " years old."


my_pet = Pet()

while True:
    name = input("Enter the name of your pet: ")
    if name.isnumeric():
        print("Invalid input! Name cannot be a number. Please try again.")
    else:
        my_pet.set_name(name)
        break

while True:
    animal_type = input("Enter the type of animal your pet is (Dog, Cat, or Bird): ")
    if animal_type not in ["Dog", "Cat", "Bird"]:
        print("Invalid input! Please enter a valid animal type (Dog, Cat, or Bird).")
    else:
        my_pet.set_animal_type(animal_type)
        break

while True:
    try:
        petAge = int(input("Enter the age of your pet (Use -11 to 0 for months): "))
        if -11 <= petAge <= 20:
            break
        else:
            print("Invalid input! Age must be between -11 and 20. Please try again.")
    except ValueError:
        print("Invalid input! Age must be a valid number. Please try again.")

my_pet.set_age(petAge)

print("Pet's Name: " + my_pet.get_name())
print("Animal Type (Dog, Cat, or Bird): " + my_pet.get_animal_type())
print(my_pet.get_age())
