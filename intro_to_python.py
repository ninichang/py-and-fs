###########################################################################################
#
#       A S S I G N M E N T    1
#
###########################################################################################

# In producing a solution, use the current file and simply replace the indicated slots in 
# the given templates below.
# Once you have a solution, RENAME the file as <your_matriculation_no>.py, and upload it
# to the corresponding submission folder in IVLE.

#------------------------------
# Exercise 1
#------------------------------

# Write a procedure that generates n random numbers between 0 and 100, 
# prints them, and computes and prints their average.

import random

def avg_of_random(n):
    sum = 0
    for i in range(1, n+1):
        num = random.randint(0, 100)
        print("Random number #",i, "is", num)
        sum = sum + num
    print("Average of", n, "random numbers is", sum/n)
      
avg_of_random(10)

# Desired output
#   Random number # 1 is 80
#   Random number # 2 is 6
#   Random number # 3 is 64
#   Random number # 4 is 18
#   Random number # 5 is 22
#   Random number # 6 is 32
#   Random number # 7 is 59
#   Random number # 8 is 45
#   Random number # 9 is 95
#   Random number # 10 is 71
#   Average of 10 random numbers is 49.2

# Desired output
#   Random number # 1 is 9
#   Random number # 2 is 7
#   Random number # 3 is 37
#   Random number # 4 is 59
#   Random number # 5 is 5
#   Random number # 6 is 33
#   Random number # 7 is 87
#   Random number # 8 is 5
#   Random number # 9 is 4
#   Random number # 10 is 89
#   Random number # 11 is 99
#   Random number # 12 is 32
#   Random number # 13 is 93
#   Random number # 14 is 53
#   Random number # 15 is 96
#   Random number # 16 is 16
#   Random number # 17 is 59
#   Random number # 18 is 75
#   Random number # 19 is 84
#   Random number # 20 is 11
#   Average of 20 random numbers is 47.65

#------------------------------
# Exercise 2
#------------------------------

# Write a procedure that prints a diamond pattern of size n (see below). 
# You may assume that n is always an odd number.
# Hint: you may want to experiment with the 'end' named parameter of the
# 'print' built-in procedure. E.g.
#
#          print('*', end='')
#
# prints a star, but does not move the current printing position to the next line.


def diamond(n):
    for i in range(1, n+1, 2):
        a = (n-i)//2 
        for k in range(a):
            print(' ', end = '')
        for j in range(i):
            print('*', end = '')
        print(' ')
    for b in range(n-2, 0, -2):
        a2 = (n-b)//2
        for p in range(a2):
            print(' ', end = '')
        for s in range(b):
            print('*', end = '')
        print(' ')
        
        
diamond(3)

# Desired output:
#     *
#    ***
#     *


diamond(7)

# Desired output:
#       *
#      ***
#     *****
#    *******
#     *****
#      ***
#       *

diamond(15)

# Desired output:
#           *
#          ***
#         *****
#        *******
#       *********
#      ***********
#     *************
#    ***************
#     *************
#      ***********
#       *********
#        *******
#         *****
#          ***
#           *

#------------------------------
# Exercise 3
#------------------------------

# Write a Python procedure that prints a diagonal pattern (see below). The arguments to this procedure are 
# the number of columns (stars) in each line, the number of lines, and the length of the gap between
# two consecutive stars on each line.

def diagonals(columns, lines, gap):
    for i in range(lines):
        for g in range(i % (gap+1)):
            print(' ', end = '')
        for stars in range(columns):
            print('*', end = '')
            for space in range(gap):
                print(' ', end = '')
        print('')
                

diagonals(20, 40, 5)

# Desired output:
#
#    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#        *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#         *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#        *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#         *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#        *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#         *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#        *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#         *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#        *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#         *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#        *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#         *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     


###########################################################################################
#
#       A S S I G N M E N T    2
#
###########################################################################################

# In producing a solution, use the current file and simply replace the indicated slots in 
# the given templates below.
# Once you have a solution, RENAME the file as <your_matriculation_no>.py, and upload it
# to the corresponding submission folder in IVLE.

#------------------------------
# Exercise 1
#------------------------------

# Write a Python procedure which, given an integer n as argument, returns the list
# of the first n Fibonacci numbers

def fibonacci_list(n):
    ans = []
    for i in range(0, n+1):
        if i == 0:
            ans.append(0)
        elif i == 1 or i == 2:
            ans.append(1)
        else:
            ans.append(ans[i-2] + ans[i-1])
    print(ans)

#------------------------------
# Exercise 2
#------------------------------

# Write a Python procedure which, given a list of integers as argument, returns 
# the sum of all the positive elemens of the list.

def sum_of_positives(l):
    answer = []
    for i in range(len(l)):
        if l[i] >= 0:
            answer.append(l[i])
    print(sum(answer))

sum_of_positives([10, -20, 30, -40])

# Evaluates to 40

sum_of_positives([-10, -20])

# Evaluates to 0 -- by convention

sum_of_positives([])

# Evaluates to 0 -- by convention

#------------------------------
# Exercise 3
#------------------------------

# Write a Python procedure which, given an integer k and a list of integers l 
# as arguments (i.e. two arguments), returns a list for which each element is 
# the sum of k consecutive elements in l.

def segment_sums(k, l):
    ans = l[0:len(l)-k+1] 
    for i in range(len(ans)):
        for j in range(1, k):
            ans[i] = ans[i] + l[i+j]
    print(ans)

segment_sums(3, [3,2,1,4,5,6])

# Evaluates to [6, 7, 10, 15], which is the same as [3+2+1, 2+1+4, 1+4+5, 4+5+6]

segment_sums(5, [2,3]) # by convention, if k > len(l), return []

# Evaluates to [] 

#------------------------------
# Exercise 4
#------------------------------

# Write a procedure which, given a list of strings l as argument, returns the 
# list of strings that appear only once in l.

# First I define a function that returns the indices of the occurencies of a specific
# element in a list.
def all_occurences(l, elem):
    indices = []
    for i in range(len(l)):
        if l[i] == elem:
            indices.append(i)
    return(indices)

def unique_strings(l):
    for i in range(len(l)):
        sublst1 = l[i+1:len(l)]
        if l[i] in sublst1:
            indices = all_occurences(l, l[i])
            for num in indices:
                l[num] = ""
    while '' in l:
        l.remove('')
    print(l)

unique_strings(['abc', 'def', 'abc', 'feg', 'def', 'abc', 'bcd'])

# Evaluates to ['feg', 'bcd']

#------------------------------
# Exercise 5
#------------------------------


# Write a Python procedure which, given a list of integers l, returns 
# the list of local maxima in l, i.e. the list of all integers who are 
# greater than both their left and right neighbor.

def peaks(l):
    ans = []
    for i in range(1, len(l)):
        if i == len(l)-1:
            print(ans)
        else:
            if l[i] > l[i-1] and l[i] > l[i+1]:
                ans.append(l[i])

peaks([2, 3, 4, 1, 2, 1, 6, 5, 4, 10, 9])

# Evaluates to [4, 2, 6, 10]

peaks([1,2]) # by convention, for any list whose length is less than or equal to 2, we return []

# Evaluates to []


###########################################################################################
#
#       A S S I G N M E N T    3
#
###########################################################################################

# In producing a solution, use the current file and simply replace the indicated slots in 
# the given templates below.
# Once you have a solution, RENAME the file as <your_matriculation_no>.py, and upload it
# to the corresponding submission folder in IVLE.

##########################################################
#
# C O N T E S T
#
##########################################################

"""
Experiment with the fractal code given in class, and create your own fractals.
Take a screenshot of your fractal graph, and put it in an archive together with
your code, and upload it into the sub-folder named "Contest" found in the student 
submission folder. The archive should have your matric number as a file name (and
extension dependent on the archive type, i.e. .zip, .tgz, .tar.gz, .rar, etc.)

The pictures will be anonymized and uploaded to a voting website, where you would
be able to vote on the ones that you like best. At the end of the voting, we will
have a winner and runner ups. The winning authors will be rewarded with small
prizes, and will have bragging rights ;)

All submissions where the code can be verified to execute correctly will receive
5% worth of the final grade.
"""

#------------------------------
# Exercise 1
#------------------------------

"""
A diophantine equation is an equation whose solutions are expected to be
integers. For instance, the equation x^2 - y^2 = 15, where both x and y
are unknown, has two sets of diophantine solutions: x = 4, y = 1, and
x = 8, y = 7. (If you would consider it as an equation over real numbers,
then it would have an infinity of solutions)

Solving diophantine equations is in general very hard. A naive solution
is to 'guess' intervals for each unknown where solutions might reside,
and perform a sweep of the cartesian product of those intervals. You are
required to implement such a solution here. Your procedure should take
as arguments a function (lambda) of two variables, and the 'low' and 
'high' limits of the 'guess' interval. Let's denote the lambda expression
by 'f', just to add clarity to this description. The diophantine equation
to solve would be f(x,y) == 0, where x and y are the unknowns. The
procedure should return a list of solutions to this equation from whithin
the interval [low, high] (we use the same interval for both unknowns).
You are expected to use set comprehensions in your solution. 
"""

def diophantine(f, x, y):
    ansSet = set()
    for value1 in range(x, y):
        for value2 in range(x, y):
            if f(value1, value2) == 0:
                ans = (value1, value2)
                ansSet.add(ans)
    print(ansSet)

diophantine(lambda x,y: x**2 - y**2 - 15, 0, 100)

# Evaluates to {(4,1), (8,7)}

#------------------------------
# Exercise 2
#------------------------------

"""
Write a procedure that takes a string as an argument, and returns
a new string where all the vowels (irrespective of case) are
replaced with the character '-' (minus), whereas all the consonants
(again, irrespective of case) are replaced with the character '+'
(plus).
"""

import string
def plus_and_minus(s):
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    for i in s:
        if i in vowels:
            s = s.replace(i, "-") 
        elif i in string.ascii_lowercase or i in string.ascii_uppercase:
            s = s.replace(i, "+")
    print(s)
plus_and_minus("The price is $100")

# Should evaluate to: '++- ++-+- -+ $100'

#------------------------------
# Exercise 3
#------------------------------

"""
Write a procedure that takes a string as an argument and returns the
set of letters, both upper- and lower-case, that DO NOT appear
in the string.
"""

import string
def non_appearing(s):
    lower = set(string.ascii_lowercase)
    upper = set(string.ascii_uppercase)
    all = set.union(lower, upper)
    for i in s:
        if i in all:
            all.remove(i)
    print(all)
    
non_appearing("The rain in Spain stays mainly in the plain")

# Evaluates to: { 'K', 'U', 'W', 'P', 'k', 'O', 'N', 'Z', 'f', 
#                 'A', 'M', 'g', 'Q', 'L', 'D', 'E', 'X', 'd', 
#                 'J', 'G', 'R', 'v', 'H', 'V', 'u', 'b', 'I', 
#                 'c', 'Y', 'j', 'q', 'C', 'o', 'B', 'w', 'z', 'F', 'x' }

non_appearing("the quick brown fox jumps over the lazy dog")

# Evaluates to: {'K', 'U', 'W', 'P', 'O', 'N', 'Z', 'A', 'M', 'Q', 
#                'L', 'D', 'E', 'X', 'J', 'T', 'G', 'R', 'H', 'V', 
#                'S', 'I', 'Y', 'C', 'B', 'F'}

non_appearing("the quick brown fox jumps over the lazy dog".upper())

# Evaluates to: {'m', 'k', 'f', 'g', 'n', 't', 'd', 'y', 'v', 'u', 'a', 
#                'b', 'l', 'c', 'p', 'j', 'h', 'e', 'q', 'i', 'o', 'w', 
#                'z', 's', 'r', 'x'}

#------------------------------
# Exercise 4
#------------------------------

"""
Write a procedure that takes two arguments. The first argument is a string,
and the second argument is a set of characters (i.e. strings, each comprising
of a single character). The procedure should return the count of all
occurrences of characters from the set inside the first argument.
"""

def count_from_set(s, chars):
    count = 0
    for i in s:
        for j in chars:
            if i == j:
                count = count + 1
    print(count)

count_from_set("The rain in Spain stays mainly in the plain.", {'a', 'i', 'y'})

# Evaluates to: 13

#------------------------------
# Exercise 5
#------------------------------

"""
Write a procedure that takes in an integer and returns the integer that has all the digits in reverse order.
"""

def reverse_digits(n):
    transformed = str(n)
    for i in range(len(transformed)-1, -1, -1):
        if i == 0:
            print(transformed[i], end = "\n")
        else:
            print(transformed[i], end = "")

reverse_digits(12345)

# Evaluates to: 54321

##########################################################################################
#
#       A S S I G N M E N T    4
#
###########################################################################################

# In producing a solution, use the current file and simply replace the indicated slots in
# the given templates below.
# Once you have a solution, RENAME the file as <your_matriculation_no>.py, and upload it
# to the corresponding submission folder in IVLE.

#------------------------------
# Exercise 1
#------------------------------

"""
Download Singapore's monthly total rainfall data from
https://data.gov.sg/dataset/f0b330c4-18c5-4d8e-ba95-7c7739297bd2/download
Write a Python procedure that loads this data and computes the _year_ with most rainfall.
"""

# my csv file is located in the current working directory. 
def year_with_most_rainfall(filename):
    f1 = open(filename, 'r', encoding = 'big5')
    txtLst = f1.readlines()
    f1.close()
    txtLst.pop(0) # remove the column names
    d = {} # initialize a dictionary that will contain the year and the cumulative rainfall
    for i in range(len(txtLst)):
        txtLst[i] = txtLst[i].strip().split(',')
        txtLst[i][0] = txtLst[i][0][0:4]  # only keep the year values
        if txtLst[i][0] not in d:
            d[txtLst[i][0]] = int(txtLst[i][1])
        else:
            d[txtLst[i][0]] += int(txtLst[i][1])
    print(max(d, key = d.get))
    

year_with_most_rainfall('rainfall-monthly-number-of-rain-days.csv')

# can also do this
import os
import csv

def year_with_most_rainfall(filename):
    data = []
    if os.access(filename, os.F_OK):
        f = open(filename)
        for row in csv.reader(f):
            data.append(row)
        f.close()
    rain_dict = {}
    for i in range(1, len(data)):
        year = data[i][0]
        y = year[0:4]
        rain = int(data[i][1])
        if y in rain_dict:
            rain_dict[y] = rain_dict[y] + rain
        else:
            rain_dict[y] = rain
    maximum = 0
    year = ''
    for item in rain_dict:
        if rain_dict[item] > maximum:
            maximum = rain_dict[item]
            year = item
    return year

#------------------------------
# Exercise 2
#------------------------------

"""
Download Singapore's mobile data usage from
https://data.gov.sg/dataset/22d7cb93-b85d-4e93-ab90-a10cfabca507/download
Write a Python procedure that loads the data and computes the quarter with the highest
increase in mobile data usage (i.e. the quarter where the difference between the current
value and the previous value is the largest.)
"""

# my csv file is located in the current working directory. 

def highest_increase_in_mobile_data(filename):
    f2 = open(filename, 'r', encoding = 'big5')
    txtLst = f2.readlines()
    f2.close()
    d = {} # initialize a dictionary that stores the quarter and the increase in mobile data usage.
    txtLst.pop(0)
    for i in range(len(txtLst)):
        txtLst[i] = txtLst[i].strip().split(',')
        if i == 0:
            d[txtLst[i][0]] = 0
        else:
            d[txtLst[i][0]] = float(txtLst[i][1]) - float(txtLst[i-1][1])
    print(max(d, key = d.get))

highest_increase_in_mobile_data('mobile-data-usage.csv')

# 
#------------------------------
# Exercise 3
#------------------------------

"""
Use the previous mobile data usage dataset and find the local maxima in
the data set. That is, find the quarters where the current data usage is greater
than both the previous and the next values. Output the result as a list of
of strings, each in the format "YYYY-Q".
"""


def data_usage_local_maxima(filename):
    f3 = open(filename, 'r', encoding = 'big5')
    txtLst = f3.readlines()
    f3.close()
    ans = [] # initialize a dictionary that stores the quarter and the increase in mobile data usage.
    txtLst.pop(0)
    for i in range(len(txtLst)):
        txtLst[i] = txtLst[i].strip().split(',')
    for i in range(1, len(txtLst)-1): 
        if float(txtLst[i][1]) > float(txtLst[i-1][1]) and float(txtLst[i][1]) > float(txtLst[i+1][1]):
            ans.append(txtLst[i][0])
    print(ans)

data_usage_local_maxima('mobile-data-usage.csv')


#------------------------------
# Exercise 4
#------------------------------

"""
Download Singapore's population data from
https://data.gov.sg/dataset/d1778088-f56a-4353-891f-21f803b2dad5/download.
A description of this data set can be found at
https://data.gov.sg/dataset/resident-population-by-ethnicity-gender-and-age-group?view_id=b8e25fcd-2cae-4093-a935-c86496482774&resource_id=f9dbfc75-a2dc-42af-9f50-425e4107ae84
Write a Python procedure that finds the average yearly population increase.
The yearly population increase is defined as the difference between
the current population and the population of the previous year.
"""

def average_population_increase(filename):
    f4 = open(filename, 'r', encoding = 'big5')
    txtLst = f4.readlines()
    f4.close()
    txtLst.pop(0) # remove the column names
    d = {} # initialize a dictionary that will contain the year and the total population
    for i in range(len(txtLst)):
        txtLst[i] = txtLst[i].strip().split(',')
        if txtLst[i][0] not in d:
            d[txtLst[i][0]] = int(txtLst[i][2])
        else:
            d[txtLst[i][0]] += int(txtLst[i][2])
    all = sum(d.values())
    sum_without_first_year = all - list(d.values())[0]
    sum_without_final_year = all - list(d.values())[len(d)-1]
    print((sum_without_first_year - sum_without_final_year)/len(d)-1)
 
average_population_increase('singapore-residents-by-ethnic-group-and-sex-end-june-annual.csv')

#------------------------------
# Exercise 5
#------------------------------

"""
Using the previous population dataset, write a Python procedure that finds
the year in which the female population became larger than the male
population in Singapore. That is, find the year where the female population
is larger than the male population, and it is also the case that for the
previous year the male population is larger than the female one.
"""

def year_females_took_over(filename):
    f5 = open(filename, 'r', encoding = 'big5')
    txtLst = f5.readlines()
    f5.close()
    txtLst.pop(0) # remove the column names
    d_male = {}
    d_female = {}
    for i in range(len(txtLst)):
        txtLst[i] = txtLst[i].strip().split(',')
        if txtLst[i][1] == 'Total Male Residents':
            if txtLst[i][3] == "na":
                continue
            elif txtLst[i][0] not in d_male:
                d_male[txtLst[i][0]] = int(txtLst[i][3])
            else:
                d_male[txtLst[i][0]] += int(txtLst[i][3])
        elif txtLst[i][1] == "Total Female Residents":
            if txtLst[i][3] == "na":
                continue
            elif txtLst[i][0] not in d_female:
                d_female[txtLst[i][0]] = int(txtLst[i][3])
            else:
                d_female[txtLst[i][0]] += int(txtLst[i][3])
    diff = {x: d_female[x] - d_male[x] for x in d_female if x in d_male}
    for i in diff:
        if diff[i] > 0 and diff[str(int(i)-1)] < 0:
            ans = i
    print(ans)

year_females_took_over('singapore-residents-by-age-group-ethnic-group-and-sex-end-june-annual.csv')


