# -*- coding: utf-8 -*-
##Problem 3: Creating Data Structures

## Data structures hold collections of objects that share some relationship to# each 
## other.  We use these to bundle together things like votes, book titles, or 
## monthly profits.

##Create a dictionary containing the months of the year and the number of days in each.

Months = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 
'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
print Months

##Create a list of the first 10 values of x^2

Values_squared = [1**2, 2**2, 3**2, 4**2, 5**2, 6**2, 7**2, 8**2, 9**2, 10**2]
print Values_squared

##Create a tuple for a 3-dimensional coordinate, aka x, y, z

my_tuple = (14, 0, 45)
print my_tuple



## Problem 4: Running Through a List
## For changing data in a large list, doing it one at a time can be tedious and 
## rather inefficient.  We often have to call upon values to bring up then change in succession.

## Without doing it one by one, go through the list of x^2 values from the first problem and change them to the values of x^2 + x + 1

import math
sqrt = math.sqrt

Values_squared[:] = [i + (math.sqrt(i)) + 1 for i in Values_squared]

print Values_squared

## Problem 5: Grabbing Information from a Dictionary
## In order to use the data that has been collected in a data structure, we have to know exactly what we want to pull out.  In the case of a dictionary, there are keys and values.

## Use your dictionary from the first problem to print out each of the months and number of days, one month per line. EX: “January has 31 days in it.”

for key, value in Months.iteritems():
    print (key) + " " + "has" + " " + str(value) + " " + "days"
    
## Problem 6: Creating Nested Data Structures

## Sometimes we require a list of objects that have multiple values in each. 
## Labels, Dates, and Prices for a salesman’s various products to sell is a 
## good example.

 

## Create a dictionary containing tuples that define the coordinates for the 
## first 10 values of x^2 + x + 1.  Use the format of coordinate from the first 
## problem.  Note, this means the z coordinate will always be 0 since this is a 
## 2-dimensional function.
        
        ######### I do not understand this question #########

## Create a dictionary of the months of the year, this time each holding a 
## dictionary of the days in it.  Each day should key to the value of 
## “No Holiday”.  Next, append 10 of those days, in any month, to values of 
## holiday names.  EX: December – 25 - “Christmas”

       ########## There must be a better way to do this other than copy and pasting
       ########## but I could not figure it out. Also, not 10 holidays because I 
       ########## couldnt think of 10.....

Months_and_Days = {'January': {1: "New Years Day!", 2: "No Holiday", 3: "No Holiday", 
4: "No Holiday", 5:"No Holiday", 6:"No Holiday", 7:"No Holiday", 8:"No Holiday", 
9:"No Holiday", 10:"No Holiday", 11:"No Holiday", 12:"No Holiday", 13:"No Holiday",
14:"No Holiday", 15:"No Holiday", 16:"No Holiday", 17:"No Holiday", 18:"No Holiday", 
19:"No Holiday", 20:"No Holiday", 21:"No Holiday", 22:"No Holiday", 23:"No Holiday", 
24:"No Holiday", 25:"No Holiday", 26:"No Holiday", 27:"No Holiday", 28:"No Holiday", 
29:"No Holiday", 30:"No Holiday", 31:"No Holiday"},'February': {1: "No Holiday", 
2: "No Holiday", 3: "No Holiday", 4: "No Holiday", 5:"No Holiday", 6:"No Holiday", 
7:"No Holiday", 8:"No Holiday", 9:"No Holiday", 10:"No Holiday", 11:"No Holiday", 
12:"No Holiday", 13:"No Holiday",14:"Valentines Day?", 15:"No Holiday", 16:"No Holiday", 
17:"No Holiday", 18:"No Holiday", 19:"No Holiday", 20:"No Holiday", 21:"No Holiday", 
22:"No Holiday", 23:"No Holiday", 24:"No Holiday", 25:"No Holiday", 26:"No Holiday", 
27:"No Holiday", 28:"No Holiday"},'March': {1: "No Holiday", 2: "No Holiday", 
3: "No Holiday", 4: "No Holiday", 5:"No Holiday", 6:"No Holiday", 7:"No Holiday", 8:"No Holiday", 
9:"No Holiday", 10:"No Holiday", 11:"No Holiday", 12:"No Holiday", 13:"No Holiday",
14:"No Holiday", 15:"No Holiday", 16:"No Holiday", 17:"No Holiday", 18:"No Holiday", 
19:"No Holiday", 20:"No Holiday", 21:"No Holiday", 22:"No Holiday", 23:"No Holiday", 
24:"No Holiday", 25:"No Holiday", 26:"No Holiday", 27:"No Holiday", 28:"No Holiday", 
29:"No Holiday", 30:"No Holiday", 31:"No Holiday"},'April': {1: "No Holiday", 2: "No Holiday", 3: "No Holiday", 
4: "No Holiday", 5:"No Holiday", 6:"No Holiday", 7:"No Holiday", 8:"No Holiday", 
9:"No Holiday", 10:"No Holiday", 11:"No Holiday", 12:"No Holiday", 13:"No Holiday",
14:"No Holiday", 15:"No Holiday", 16:"No Holiday", 17:"No Holiday", 18:"No Holiday", 
19:"No Holiday", 20:"No Holiday", 21:"No Holiday", 22:"No Holiday", 23:"No Holiday", 
24:"No Holiday", 25:"No Holiday", 26:"No Holiday", 27:"No Holiday", 28:"No Holiday", 
29:"No Holiday", 30:"No Holiday"},'May': {1: "No Holiday", 2: "No Holiday", 3: "No Holiday", 
4: "No Holiday", 5:"No Holiday", 6:"No Holiday", 7:"No Holiday", 8:"No Holiday", 
9:"No Holiday", 10:"No Holiday", 11:"No Holiday", 12:"No Holiday", 13:"No Holiday",
14:"No Holiday", 15:"No Holiday", 16:"No Holiday", 17:"No Holiday", 18:"No Holiday", 
19:"No Holiday", 20:"No Holiday", 21:"No Holiday", 22:"No Holiday", 23:"No Holiday", 
24:"No Holiday", 25:"No Holiday", 26:"No Holiday", 27:"No Holiday", 28:"No Holiday", 
29:"No Holiday", 30:"No Holiday", 31:"No Holiday"}, 'June': {1: "No Holiday", 2: "No Holiday", 3: "No Holiday", 
4: "No Holiday", 5:"No Holiday", 6:"No Holiday", 7:"No Holiday", 8:"No Holiday", 
9:"No Holiday", 10:"No Holiday", 11:"No Holiday", 12:"No Holiday", 13:"No Holiday",
14:"No Holiday", 15:"No Holiday", 16:"No Holiday", 17:"No Holiday", 18:"No Holiday", 
19:"No Holiday", 20:"No Holiday", 21:"No Holiday", 22:"No Holiday", 23:"No Holiday", 
24:"No Holiday", 25:"No Holiday", 26:"No Holiday", 27:"No Holiday", 28:"No Holiday", 
29:"No Holiday", 30:"No Holiday", 31:"No Holiday"}, 'July': {1: "No Holiday", 2: "No Holiday", 3: "No Holiday", 
4: "No Holiday", 5:"No Holiday", 6:"No Holiday", 7:"My Birthday!", 8:"No Holiday", 
9:"No Holiday", 10:"No Holiday", 11:"No Holiday", 12:"No Holiday", 13:"No Holiday",
14:"No Holiday", 15:"No Holiday", 16:"No Holiday", 17:"No Holiday", 18:"No Holiday", 
19:"No Holiday", 20:"No Holiday", 21:"No Holiday", 22:"No Holiday", 23:"No Holiday", 
24:"No Holiday", 25:"No Holiday", 26:"No Holiday", 27:"No Holiday", 28:"No Holiday", 
29:"No Holiday", 30:"No Holiday", 31:"No Holiday"},'August': {1: "No Holiday", 2: "No Holiday", 3: "No Holiday", 
4: "No Holiday", 5:"No Holiday", 6:"No Holiday", 7:"No Holiday", 8:"No Holiday", 
9:"No Holiday", 10:"No Holiday", 11:"No Holiday", 12:"No Holiday", 13:"No Holiday",
14:"No Holiday", 15:"No Holiday", 16:"No Holiday", 17:"No Holiday", 18:"No Holiday", 
19:"No Holiday", 20:"No Holiday", 21:"No Holiday", 22:"No Holiday", 23:"No Holiday", 
24:"No Holiday", 25:"No Holiday", 26:"No Holiday", 27:"No Holiday", 28:"No Holiday", 
29:"No Holiday", 30:"No Holiday", 31:"No Holiday"},'September': {1: "No Holiday", 2: "No Holiday", 3: "No Holiday", 
4: "No Holiday", 5:"No Holiday", 6:"No Holiday", 7:"No Holiday", 8:"No Holiday", 
9:"No Holiday", 10:"No Holiday", 11:"No Holiday", 12:"No Holiday", 13:"No Holiday",
14:"No Holiday", 15:"No Holiday", 16:"No Holiday", 17:"No Holiday", 18:"No Holiday", 
19:"No Holiday", 20:"No Holiday", 21:"No Holiday", 22:"No Holiday", 23:"No Holiday", 
24:"No Holiday", 25:"No Holiday", 26:"No Holiday", 27:"No Holiday", 28:"No Holiday", 
29:"No Holiday", 30:"No Holiday"}, 'October': {1: "No Holiday", 2: "No Holiday", 3: "No Holiday", 
4: "No Holiday", 5:"No Holiday", 6:"No Holiday", 7:"No Holiday", 8:"No Holiday", 
9:"No Holiday", 10:"No Holiday", 11:"No Holiday", 12:"No Holiday", 13:"No Holiday",
14:"No Holiday", 15:"No Holiday", 16:"No Holiday", 17:"No Holiday", 18:"No Holiday", 
19:"No Holiday", 20:"No Holiday", 21:"No Holiday", 22:"No Holiday", 23:"No Holiday", 
24:"No Holiday", 25:"No Holiday", 26:"No Holiday", 27:"No Holiday", 28:"No Holiday", 
29:"No Holiday", 30:"No Holiday", 31:"No Holiday"},'November': {1: "No Holiday", 2: "No Holiday", 3: "No Holiday", 
4: "No Holiday", 5:"No Holiday", 6:"No Holiday", 7:"No Holiday", 8:"No Holiday", 
9:"No Holiday", 10:"No Holiday", 11:"No Holiday", 12:"No Holiday", 13:"No Holiday",
14:"No Holiday", 15:"No Holiday", 16:"No Holiday", 17:"No Holiday", 18:"No Holiday", 
19:"No Holiday", 20:"Thanksgiving sometimes", 21:"No Holiday", 22:"No Holiday", 23:"No Holiday", 
24:"No Holiday", 25:"No Holiday", 26:"No Holiday", 27:"No Holiday", 28:"No Holiday", 
29:"No Holiday", 30:"No Holiday"},'December': {1: "No Holiday", 2: "No Holiday", 3: "No Holiday", 
4: "No Holiday", 5:"No Holiday", 6:"No Holiday", 7:"No Holiday", 8:"No Holiday", 
9:"No Holiday", 10:"No Holiday", 11:"No Holiday", 12:"No Holiday", 13:"No Holiday",
14:"No Holiday", 15:"No Holiday", 16:"No Holiday", 17:"No Holiday", 18:"No Holiday", 
19:"No Holiday", 20:"No Holiday", 21:"No Holiday", 22:"No Holiday", 23:"No Holiday", 
24:"No Holiday", 25:"Christmas", 26:"No Holiday", 27:"No Holiday", 28:"No Holiday", 
29:"No Holiday", 30:"No Holiday", 31:"No Holiday"}}
print Months_and_Days ['January'] [1]
print Months_and_Days ['December'] [25]
print Months_and_Days ['July'] [7]