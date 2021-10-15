#!python3

"""
Create a LIST that contains the following strings, in order:
Cat
Fish
Dog
Bear
Turtle

Sort the list into alphabetical order and and then ask the user to enter a number corresponding
to the index of an element.  Print the element associated with that index.

inputs:
integer number

outputs:
string animal

example:
Enter the index for an animal:2
The animal at that index is Dog
"""


x = int(input("Enter Number: "))
animals = ["Cat", "Fish", "Dog", "Bear", "Turtle"]
animals.sort

if x == 2:
    print(animals[2])
elif x == 0:
    print(animals[0])
elif x == 3:
    print(animals[3])
elif x == 4:
    print(animals[4])
elif x == 1:
    print(animals[1])




