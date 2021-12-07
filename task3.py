#!python3

'''
Ask the user to enter in a list of 5 words.
Convert the word to a string literal JSON object
Write the contents to a file called 'task3.txt'

Example:
Enter a word: frog
Enter a word: french
Enter a word: puppy
Enter a word: escalate
Enter a word: ice

task3.txt contents:
["frog","french","puppy","escalate","ice"]

'''
import json

file = open("task3.txt", "w")
print("||||Please Enter 5 words||||")
a1 = input("Enter a word: ")
a2 = input("Enter a word: ")
a3 = input("Enter a word: ")
a4 = input("Enter a word: ")
a5 = input("Enter a word: ")
list = [a1,a2,a3,a4,a5]

x = json.dumps(list)
file.write(x)

