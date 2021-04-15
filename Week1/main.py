#1.print my name and age
name = "Hema"
age = 37
print("Name:{}\n Age:{}".format(name, age))

#2. Create a list of your 5 favorite movies and store it in the variable
fav_list = ["Titanic", "Home alone", "Silence", "Dinosaur", "Frozen"]

#3. Display the first and last colors from the  list.
color_list = ["Red", "Green", "White" , "Black"]
print(color_list[0])
print(color_list[-1])

#4. A Python script to add a key to a dictionary
sample_dictionary= {0: 10, 1: 20}
sample_dictionary[2] = 30
print(sample_dictionary)

#5. Python program to calculate body mass index.
height = float(input("Enter your body weight in kg"))
weight = float(input("Enter your body height in feet"))
print("Your body mass index is: ", round(weight / (height * height)))

#6. Guess number
import random
user_number=random.randint(1, 9)
guess_number=0
while user_number != guess_number:
     guess_number=int((input("Guess a number between 1 and 9:")))
else:
     print("well guessed")

#7. Tuple with different datatypes
mytuple_one = ("apple", "banana", "cherry")
mytuple_two = (1, 5, 7, 9, 3)
mytuple_three = (True, False, False)
mytuple_four = ("abc", 34, True, 40, "male")

#8. Create a list of 5 city names and convert it into tuples.
my_list=["Copenhagen","Herlev","Roskilde","Malmo","Gentofte"]
print(my_list)
my_tuple=tuple(my_list)
print(my_tuple)

#9. Remove duplicated from the list:
sample_list = [10,20,30,20,10,50,60,40,80,50,40]
original_list = list(dict.fromkeys(sample_list))
print(original_list)

#10.remove the characters which have odd index values of a given string
original_string = input("Please Enter your Own String : ")
final_string = ''
for i in range(len(original_string)):
     if (i % 2 == 0):
          final_string = final_string + original_string[i]
print("Original String :  ", original_string)
print("Final String :     ", final_string)
