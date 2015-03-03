from utils import Count, Intersection, Split, Quicksort

file1 = open("file_02.txt","r")
file2 = open("file_03.txt","r")
file3 = open("file_04.txt","r")

text1 = eval(file1.read())
text2 = Split(file2.read())
text3 = Split(file3.read())

file1.close()
file2.close()
file3.close()

print "Exercise 2"
print Quicksort(text1)

print "Exercise 3"
print Count(text2)

print "Exercise 4"
print Intersection(text2,text3)

