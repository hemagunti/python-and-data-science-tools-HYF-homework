# 1.Write a function called fizz_buzz that takes a number
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num


print(fizzbuzz(60))

# 2. try and except block to avoid IndexError.
num_list = [5, 10, 20]
try:
    if num_list[5] == 20:
        print("number is the list")
except IndexError:
    print("List index out of range")


# 3. Create a class with arguments
class JetInventory():
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def jet_details(self):
        print(f'{self.name} {self.country}')


jetInventory1 = JetInventory("AirIndia", "India")
jetInventory1.jet_details()

# 4. Create a notebook
# import pandas as pd
# df = pd.read_csv('test.csv')
# data.head()

# 5. check whether a given key already exists in a dictionary.
dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def is_key_present(key):
    if key in dic:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')


is_key_present(5)
is_key_present(9)


# 6.Identify the even and odd numbers.

def show_numbers(limit):
    num = int(input("Enter a number: "))
    mod = num % 2
    if mod > 0:
        print("{0} is odd".format(num))
    else:
        print("{0} is even".format(num))

show_numbers(5)

# 7. Read the dataset
#import pandas as pd
#df = pd.read_csv('creditcard.csv')
#data.head()
#df.describe()
#df.info()


# 8. Create a classd Person, with firstname and lastname properties, and a print name method.
class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def name(self):
        print(f"My name is :   {self.first_name}  {self.last_name}")


person = Person("Hema", "Gunti")
person.name()

# 9.Write a program asks for numeric user input.
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


# 10. Write a Python program to create two empty classes,
class Student:
    pass


class Marks:
    pass


student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
