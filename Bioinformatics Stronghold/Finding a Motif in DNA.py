import re

f = open("rosalind_subs.txt", 'r').read().split('\n')
repeat = f[1]
string = f[0]
output = ""
#print(repeat, string)
l = len(repeat)
for i,o in enumerate(string[0:len(string)-l]):
    print(o)
    k = string[i:i+l]
    print(k,len(k),l)
    
    if repeat == k:
        output += str(i+1) + " "
        print(i)
print(output)
