# Name: Samuel Stubbins
# Evergreen Login: Stusam07
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print test-high-gc-1-expected.txt

    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
at_count = 0
a_count = 0
t_count = 0
g_count = 0
c_count = 0


# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1
    
    elif bp == 'A' or bp == 'T':
        # increment the count of at
        at_count = at_count + 1
for bp in seq:
    if bp == 'A':
        a_count = a_count + 1
    
    elif bp == 'T':
        t_count = t_count + 1
    
    elif bp == 'C':
        c_count = c_count + 1
    
    elif bp == 'G':
        g_count = g_count + 1

AT_GC_Ratio = float(at_count) / (gc_count)       
sum_count = (a_count + t_count + g_count + c_count)        

# divide the gc_count and at_count by the total_count
gc_content = float(gc_count) / sum_count
at_content = float(at_count) / sum_count


# Print the answer
print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'A Count:', a_count
print 'T Count:', t_count
print 'G Count:', g_count
print 'C Count:', c_count
print 'Sum Count:', sum_count
print 'Total Count:', total_count
print 'Length of sequence:', len(seq)
print 'AT/GC Ratio:', AT_GC_Ratio

if gc_content > 0.6:
    print 'CG Classification: This is a high GC content organism'
elif gc_content < 0.4:
    print 'CG Classification: This is a low GC content organism'
else:
    print 'CG Classification: This is a moderate GC content organism'


