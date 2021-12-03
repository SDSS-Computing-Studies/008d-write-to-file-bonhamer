#!python3

'''
Have the user enter in their name and email address.
Have the program create a file called 'task1.txt'
Write their name to the first line and their email to the second line.

Example:
```
What is your name? Joe Lunchbox
What is your email? joe@sandwiches.org 
```

task1.txt contents:
```
Joe Lunchbox
joe@sandwiches.org 
```
(3 points) 
'''

file = open('task1.txt','w')

Line1 = input("What is your name?")
Line2 = input("What is your email?")

file.write(Line1)
file.write(f'\n')
file.write(Line2)