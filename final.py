In [3]: import os

In [4]: from os import path

In [5]: files = filter(path.isfile, os.listdir("fasta_problem"))

#this is supposed to give me a list of all the files in the directory

fasta = open('file', 'r')
fasta = open('files', 'r')
fasta = open("files")

#it kept saying there are no such file or directory, since I had no clue what to do i tried to read it

files.read()

#here it told me the 'list object had no attribute ' read'

item.read() for item in files
[item.read() for item in files]

#I found this in stack overflow but the output had nothing in it so I don't know where to go from here

fasta = open("fasta_problem")
fasta = open("fasta_problem").readlines()
import glob
path = '~/final/fasta_problem'
files=glob.glob(path)
for file in files:
    f=open(file, 'r')
    print '%s' % f.readlines()
    f.close
for file in files:
    f=open(file, 'r')
    print '%s' % f.readlines()

#this failed too it won't give me any output

import os
os.listdir("C:\fasta_problem")
help ()
import os
os.listdir("~/final/fasta_problem") #this gave me an error



import os
os.listdir("fasta_problem")
for file in os.listdir("fasta_problem)
help()

import os
os.listdir("fasta_problem") # this actually gave me an output with a list of all the files in the fasta_problem directory but I cannot figure out how to read all the files.

for file in os.listdir("fasta_problem") #everything from here on has given me errors
for file in os.listdir("fasta_problem"):
    when fasta = ".seq"
    fasta.read()
for file in os.listdir("fasta_problem"):
    fasta = os.listdir("fasta_problem")
    new = fasta.read()
    print new
for file in os.listdir("fasta_problem"):
    fasta = os.listdir("fasta_problem")
    [item.read() for item in fasta]
    print fasta
InFile = open("os.listdir("fasta_problem")", "r")

#Im trying to see what os.listdir() does because whenever I search how to read the file in a directory this is all i get. 

fasta = os.listdir("fasta_problem")

for line in fasta:
             new = "it works" +line.lower()
             print new
    
#this was the output

it worksfec00005_1.seq
it worksfec00003_1.seq
it worksfec00005_2.seq
it works.ds_store
it worksfec00004_1.seq
it worksfec00002_1.seq
it worksfec00001_1.seq
it worksfec00006_1.seq
it worksfec00007_1.seq
it worksfec00007_3.seq
it worksfec00007_2.seq

#so os.listdir only gives me a list of the names of the files in the directory but it doesn't read the files so i can format the names but no the actual file content.
