#!/usr/bin/env python
# Note: 
#   Please save this as diagnostic_firstname.py
#       (replace firstname w/ yours)
#   Do not edit lines that say: "# Last line in ____"
###############################################################################
# Imports  # there will only be one import added here.
import os
###############################################################################
# Write f01 that prints "Hello World!" and calls f02. (three lines)
def f01():
    print "Hello World!"
    f02()
###############################################################################
# Write f02 that sets the variables x, y, and z equal to the words 
# necessary to have the f03 print "i love python!" (five lines)
def f02():
    x = "i"
    y = "love"
    z = "python!"
    f03(x,y,z)  # Last line in f2()
###############################################################################
# Finish f03 (replace the ????). 
def f03(*words):
    truth = " ".join(words)  # This is broken.
    truth_emphasized = truth + "!"
    print truth_emphasized
    f04(truth)  # Last line in f03()
###############################################################################
# Write f04 that prints truth backwards (edit one line only)
# Ex. f4("Littlest Bear") prints "raeB tselttiL"
def f04(string):
    print string[::-1]
    f05(string)  # Last line in f04()
###############################################################################
# Write f05 that for each char in a word passed as a parameter, prints that 
# word on a new line, and for each consecutive print, prints it indented by one
# more char. (possibly a few lines)
# Ex. f05("Info")
# Info
#  Info
#   Info
#    Info
def f05(word):
    n_times = len(word)
    for x in range(1, n_times):
        print (" "*x) + word

    f06("South Hall", "Python Rocks!")  # Last line in f05()
###############################################################################
# Write f06 that takes two strings:
# (1) prints: "'string' is longer than 'string' by x chars"
#   replace string and string w/ the actual strings, replace x w/ proper value
# (2) prints: "'string' has only xx.xx% the number of chars of 'string'"
#   replace string and string w/ the actual strings
#   replace xx.xx w/ proper value
# (several lines)
# Ex. f06("short_string", "longer_string")
# 'longer_string' is longer than 'short_string' by 1 chars
# 'short_string' has only 92.31% the number of chars of longer_string
def f06(string1, string2):
    len_s1 = len(string1)
    len_s2 = len(string2)
    if len_s1 > len_s2:
        print "{0} is longer than {1} by {2} chars".format(string1, string2, len_s1-len_s2)
        print "{0} has only {1}%% the number of chars of {2}".format(string2, round(100*(len_s2/float(len_s1)), 2), string1)
    elif len_s2 > len_s1:
        print "{0} is longer than {1} by {2} chars".format(string2, string1, len_s2-len_s1)
        print "{0} has only {1}%% the number of chars of {2}".format(string1, round(100*(len_s1/float(len_s2)), 2), string2)
    else:
        print "The strings are equal length!"

    various_solutions()  # Last line in f06()
###############################################################################
# Write f07, f08, f09, f10 to find the sum of all the multiples of 3 or 5 
# below 500 (starting at 1)
# f07 should demonstrate a while loop, returning the sum
# f08 should demonstrate a for loop, returning the sum
# f09 should demonstrate list comprehension, returning the sum
# f10 should demonstrate recursion, returning the sum
# check_solution_vals() will call the functions and check solutions.
# only edit the parameters in the function calls (if you want to)
###############################################################################
def various_solutions():
    """ This checks solutions. ONLY EDIT PARAMETERS PASSED TO FUNCTIONS. """
    while_ = f07()
    for_ = f08()
    list_comprehension = f09()
    recursion = f10()
    # DO NOT EDIT BELOW THIS LINE
    vals = [while_, for_, list_comprehension, recursion]
    for val in vals:
        print val
    if len(set(vals)) == 1:
        print("Not sure if it's right, but all your solutions agree!")
    else: print ("Oops...")
    f11_args = [1,"2", 3.0, '4', 5.0, 6]  # Last lines in various_solutions()
    for arg in f11_args:
        f11(arg)
    f12()
###############################################################################
def f07():
    i = 0
    total = 0
    while i < 500:
        if i % 3 == 0 or i % 5 == 0:
            total += i
        i += 1

    return total


###############################################################################
def f08():
    total = 0
    for i in range(1,500):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total


###############################################################################
def f09():
    sum_list = range(1,500)
    total_list = [i for i in sum_list if i % 3 == 0 or i % 5 == 0]
    total = sum(total_list)
    return total


###############################################################################
def f10(total=0, i=0):
    #This is wrong
    if i <= 500:
        total += i
        i += 1
        return f10(total, i)

###############################################################################
# Write f11() to take arguments, printing them as floats if they started as
# strings, integers if they started as floats, and as the value 0 if they
# started as ints.
def f11(args):
    if type(args) == type(" "):
        print float(args)
    elif type(args) == type(1.0):
        print int(args)
    elif type(args) == type(1):
        print 0

###############################################################################
# Write f12() to ask for raw_input from the user. Change the input to a float.
# Create log_file.txt to log the input that cannot be changed to a float. 
#   - write one faulty input per line
# Print, as a list, all converted input.
# Proceed to the last line, calling f13, when the user types done or "done"
# Ex. log_file.txt
#   TEST
#   123abc
#   python rules
# Ex. printing
#   [1.0, 1.3, 2.443]
def f12():
    good_stuff = []
    bad_stuff = []
    while True:
        users_stuff = raw_input("Enter some stuff: ")
        if users_stuff == "done":
            break
        else:
            try:
                users_stuff_float = float(users_stuff)
            except ValueError:
                bad_stuff.append(users_stuff)
                continue
            else:
                good_stuff.append(float(users_stuff))
                continue
    with open("log_file.txt", "w") as f:
        for item in bad_stuff:
          f.write("{0}\n".format(item))
    print good_stuff
    f13()  # Last line in f12()
###############################################################################
# Fix the error in f13:
def f13():
    for each in "string":
         print each
    f14()  # Last line in f13()
###############################################################################
# Write f14 to print the path and filename of this script. DO NOT HARD CODE.
# You must add an import statement. Please do so at the top of the file.
# Ex. /Users/dsg/Desktop/python-boot-camp/HW11/diagnostic.py
def f14():
    print os.getcwd()
    print __file__

    f15()  # Last line in f14()
###############################################################################
# Write f15 to print the goal below. Do not print any strings.
# Do not take more than nine lines to code.
# Goal:
# [[0], [], [], [], [], [], [], [], [], []]
# [[], [0], [], [], [], [], [], [], [], []]
# [[], [], [0], [], [], [], [], [], [], []]
# [[], [], [], [0], [], [], [], [], [], []]
# [[], [], [], [], [0], [], [], [], [], []]
# [[], [], [], [], [], [0], [], [], [], []]
# [[], [], [], [], [], [], [0], [], [], []]
# [[], [], [], [], [], [], [], [0], [], []]
# [[], [], [], [], [], [], [], [], [0], []]
# [[], [], [], [], [], [], [], [], [], [0]]
def f15():
    design_list = [[], [], [], [], [], [], [], [], [], []]
    for i in range(0, 10):
        designlist = [[], [], [], [], [], [], [], [], [], []]
        designlist[i] = [0]
        print designlist

    f16([1,2,3],[4,5,6])  # Last line in f15()
###############################################################################
# Write f16() that takes two lists and prints a list with the nth elements of 
# each list sharing a tuple.
# Ex.
# [1,2,3] and [4,5,6] would produce [(1, 4), (2, 5), (3, 6)]
def f16(list1, list2):
    print zip(list1, list2)
    f17()  # Last line in f16()
###############################################################################
# Write f17() to take the 2nd line from few_words.txt, and print a list
# with the index of the word in that line and the word, sharing tuples.
# Ex. [(0, 'To'), (1, 'be'), (2, 'or'), (3, 'not'), (4, 'to'), (5, 'be')]
def f17():
    with open("few_words.txt", "r") as f:
        few_words = f.readlines()

    line2 = few_words[1].strip()
    line2_list = line2.split()
    length_line2 = len(line2_list)
    indices = [i for i in range(0,length_line2+1)]

    shared_list = zip(indices, line2_list)
    print shared_list

    # Be sure to save the list that you print to list_
    list_ =  shared_list  # Change to your list 
    f18(list_)  # Last line in f17()
# Write f18 to take the list above and create a dictionary, use the words as
# keys and the numbers as values.
# Print the dictionary.
# Call the dictionary in f19()
def f18(list_):
    converted_dict = {item[0]:item[1] for item in list_}
    print converted_dict
    f19(converted_dict)  # Last line in f18()
# Write f19 to update that dictionary by changing the values by adding the 
# number of chars in the word to the current value (if the resulting value
# would be even), otherwise change the value to the ascii number for the last
# char in the word. Print the new dictionary.
def f19(d):
    for key in d.keys():
        print key
        print len(d[key])
        if (len(d[key]) + key) % 2 == 0:
            print "Change!"
            #This prints change when it's supposed to, but I'm not sure how to modify
            #the current key (the below line seems to do nothing in the final product)
            key += len(d[key])
        else:
            key = ord(d[key][-1])
    print d

    f22()  # Last line in f19()
# Write f21() to find if a word is capitalized. Return True/False.
# Ex.
# f21("Yes") = True, f21("NO") = False, 
# f21("nope") = False, f21("nADA") = False
def f21(word):
    if word[0].isupper() and word[1:].islower():
        return True
    else:
        return False

# Write f22() to use f21() to
# (1) print a list of all capitalized words in 
# few_words.txt sorted by length. Then
# (2) remove all duplicate words.
# (3) If our favorite word (Python) is in the list, move it to the front of the 
# list (because it deserves to be there). (4) Make Python all uppercase.
# (5) If magic is in the list. Delete it. 
# (6) Add an exlamation mark to Python.
# (7) To show how special Python is to us, put all the other words in a nested
# list so they don't contaminate Python.
# (8) This latest version (second print in this function)
# Ex. second print:
# ['PYTHON!', ['Other1', 'Other_2']]
def f22():
    """This function is to programmers as waterboarding is to prisoners"""
    





    f23([["o","o","x"],["x","o","x"],["o","","x"]])  # Last lines in f22()
    f23([["o","","o"],["x","o","x"],["o","x","x"]])
    f23([["o","o","x"],["x","x","x"],["o","","o"]])
# Write f23() that takes a list of three lists of len 3, and says who won in 
# tic-tac-toe (you can expect all moves to have been legal, made turn-by-turn)
# you can expect there is a winner. Print the x or o and the type of win:
# "col1", "col2", "row3", "falling_back_diag", "falling_front_diag" 
# Ex. of rows (not a finished game)
# row1 = ["o","",""]
# row2 = ["","x",""]
# row3 = ["","",""]
# Ex. of print: x, col2
def f23(lists_):
    #Didn't get to this one
    pass













# Write main() that calls f01, then prints the The Zen of Python, by Tim Peters.
# (three lines)
def main():
    f01()
    print " "
    import this

# Write the boilerplate code. (two lines)
if __name__ == '__main__':
    main()