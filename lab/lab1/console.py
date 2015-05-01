# Lab 1 - Python (Re-)Introduction
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
"""Lab 1: interactive console.

This module contains a script to run an interactive console,
in which the user types in commands and sees results.
Your task is to add to the (very bare) functionality.
"""
"""
Implementing new features

Add the following commands to the console:

exit: print a goodbye message and stop the loop. Hint: look up the break keyword. When we say "look up", we mean "Google 'Python break'".
op n m, where op is one of add, subtract, multiply, or divide, and n and m are numbers: the program prints the result of performing the arithmetic operation on n and m. Sample interaction:

>>> Say something: add 3 2
5
>>> Say something: subtract 10 3
7
>>> Say something: multiply 3 4
12
Hints: to accomplish this you need to do three things: take the input string and split it into the separate words; convert the second and third words (the arguments) into integers; output a result depending on what the first word (the command) is.
Spend a lot of time on this one to make sure you understand how this works: once you do, you'll apply the same strategy to the rest of the commands.

store key value and lookup key: key and value are strings without any spaces in them. Use a Python dictionary to store and retrieve values. Sample interaction:

>>> Say something: store food banana
>>> Say something: lookup food
'banana'
If you need a refresher on Python dictionaries, click here. Note that the easiest way to implement this feature is to use a global variable to store the dictionary.
What happens when the user asks to lookup a key that hasn't been stored? Your program shouldn't crash!

execute file: Reads in the commands in file and executes them one by one. Your program should print both the commands and the outputs; distinguish them. For example, suppose we have the file instructions.txt containing the following:

add 4 5
store name David
multiply 3 7
lookup name
The following interactions could take place:

>>> Say something: execute instructions.txt
Executing: add 4 5
9
Executing: store name David
Executing: multiply 3 7
21
Executing: lookup name
'David'
** Done executing file instructions.txt **
>>> Say something: lookup name
'David'
"""

import sys

# Constants in Python generally named with ALL_CAPS
EASTER_EGG = 'I\'m giving up on you'
EASTER_EGG_RESPONSE = 'That\'s not very nice!'
dictionary=dict()


def start_interaction():
    """ () -> NoneType

    Begin an infinite loop that repeatedly asks for a command
    and then executes an action.
    """
    # Loop infinitely
    while True:
        # Prints 'Say something: ' and then waits for user input
        # Note: line gets a string value
        line = input('Say something: ')
        words= line.split(' ')

        # Right now, not very interesting...?
        if line == EASTER_EGG:
            print(EASTER_EGG_RESPONSE)

        elif line=='exit':
            print('Good bye!')
            break

        elif words[0]=='add' or words[0]=='subtract' or words[0]=='multiply':
            calculate(words)

        elif words[0]=='store' or words[0]=='lookup':
            diction(words)

        elif words[0]=='execute':
            execute(words)

        elif words[0]=='python-go!':
            evaluate(words)
        
        else:
            print(repeat(line))

def operation(line):
        # Prints 'Say something: ' and then waits for user input
        # Note: line gets a string value
        words= line.split(' ')

        # Right now, not very interesting...?
        if line == EASTER_EGG:
            print(EASTER_EGG_RESPONSE)

        elif line=='exit':
            print('Good bye!')

        elif words[0]=='add' or words[0]=='subtract' or words[0]=='multiply':
            calculate(words)

        elif words[0]=='store' or words[0]=='lookup':
            diction(words)

        elif words[0]=='execute':
            execute(words)

        elif words[0]=='python-go!':
            evaluate(words)
        else:
            print(repeat(line))

def repeat(s):
    """ (str) -> str

    Return a string identical to the input.
    Note the difference between *returning* a string and printing it out!

    Params
    - s: string to repeat
    """

    return s

def calculate(words):
    """(list)->NoneType
    Return the calculated result
    """
    num1=float(words[1])
    num2=float(words[2])
    if words[0]=='add':
        print(num1+num2) 
    elif words[0]=='subtract':
        print(num1-num2) 
    else:
        print(num1*num2) 

def diction(words):
    """
    list->NoneType
    """
    w1=words[1]

    global dictionary
    if words[0]=='store':
        w2=words[2]
        dictionary[w1]=w2
    else:
        if words[1] not in dictionary:
            print ('Not found!')
        else:
            w2=dictionary[w1]
            print (w2)

def execute(words):
    """list->NoneType
    execute a text file as command
    """
    with open(words[1],'r') as myFile:
        for line in myFile:
            print('Executing:',line)
            operation(line)


def evaluate(words):
    """list->NoneType
    using evaluate excute a string
    """
    s=' '.join(words)
    string=s[11:] 
    print(eval(string))
# This is the main function; called when program is run.
if __name__ == '__main__':
    start_interaction()
