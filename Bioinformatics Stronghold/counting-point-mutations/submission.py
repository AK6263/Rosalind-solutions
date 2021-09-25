"""
# Evolution as a sequence of mistakes

ALGORITHM
Hamming distance is the number of mutations d_H(s,t_)

Given : Two DNA strings s and t of equal lenght (not exceeding 1kbp)
Return : The Hamming distance d_H(s,t)

"""

reader =  open("rosalind_hamm.txt","r").read().split('\n')
print(reader)
s = reader[0]
t = reader[1]

if len(s) == len(t):
    print(len(s))
d_H = 0
for i in range(len(s)):
    if s[i] != t[i]:
        d_H += 1

print(s)
print(t)
print(d_H)
