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
1 = input("Enter a word: ")
2 = input("Enter a word: ")
3 = input("Enter a word: ")
4 = input("Enter a word: ")
5 = input("Enter a word: ")
list = [1,2,3,4,5]

x = json.dumps(list)

