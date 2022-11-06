#!/bin/python

cp /localdisk/data/BPSM/Lecture12/input.txt .

#identify the adapter
#open('input.txt').readlines()
readingInput=open("input.txt")

#identify the adapter
readingInput.readline()
#read the line, \rstrip adapter and append to new txt
#duplicate file \rstrip to remove adapter
adapter=readingInput.readline()[:14]
print(adapter)
print(readingInput.read().rstrip(adapter))



#cut adapter by using index numbers
#write to file

############################################

count=0
my_file = open('input.txt')
for eachline in my_file :
    count+=1
    print(adapter)
    no_adapter = eachline.rstrip('ATTCGATTATAAG')#use replace or substringreplacement
    print(f"{no_adapter}\n")
