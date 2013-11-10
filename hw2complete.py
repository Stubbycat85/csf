# Name: Samuel Stubbins
# Evergreen Login: stusam07
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

a = 0
b = 0
while a < 100:
    a+=1
    b+=a
    print b



###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

num = [1/1.0, 1/2.0, 1/3.0, 1/4.0, 1/5.0, 1/6.0, 1/7.0, 1/8.0, 1/9.0, 1/10.0]
for x in num:
    print


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0
for i in range(n):
    triangular = (i*n)/2 + n 
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10
factorial = 1
for i in range(n):
    factorial = factorial * (i+1) 
    print factorial

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

numlines = 10
factorial = 1
for i in range(1, numlines+1):
    for i in range(1,numlines+1):
        factorial = factorial * i
    print factorial
    factorial = 1
    numlines = numlines-1

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

numlines = 10
x = 0 
for i in range(1, numlines+1):       
    factorial = 1
    for i in range(1, i + 1):
        factorial = i * factorial
    x = (1.0/factorial) + x
print x + 1

##### Did not fully understand processes used to find solutions to #s 5 and 6, used help and experimentation to get solution


###
### Collaboration
###
# Collaborated with Nick Hefling
# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").
## Used help from google, github, and Khan Academy tutorials
###
### Reflection
###

# ... Entire assignment took me about 10 hours. Did not feel prepared at all by readings, lectures,
# ... or workshop. Was only able to complete at all with collaboration and online tutorials.
# ... 
