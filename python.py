This is my first python code 

===================================================
Program1:

    number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

===================================================
This is my second Python Program 
===================================================
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a non-negative number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is: {factorial(num)}")

===================================================
This is my Third Python Program 
===================================================

    class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy", "Golden Retriever")
print(f"My dog's name is {my_dog.name} and he is a {my_dog.breed}.")
my_dog.bark()

======================================================
print("Hello, World!")

