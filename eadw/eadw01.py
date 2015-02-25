from utils import Count, Intersection, MySplit, Quicksort

file1 = open("file_02.txt","r")
file2 = open("file_03.txt","r")
file3 = open("file_04.txt","r")

text1 = file1.read()
text2 = MySplit(file2.read())
text3 = MySplit(file3.read())

file1.close()
file2.close()
file3.close()

print "Exercise 2"
vec = eval(text1)
Quicksort(vec)
print vec

print "Exercise 3"
print Count(text2)

print "Exercise 4"
print Intersection(text2,text3)




print Quicksort(["a","c","b"])