f = open("rosalind_revc.txt", 'r').read().split('\n')
k = open("complement.txt",'w')
l = ""
nuct = {'A' : 'T',
        'C' : 'G',
        'G' : 'C',
        'T' : 'A'}
for i in f[0][::-1]:
    print(i,nuct[i])
    l += nuct[i]
    
k.write(l)
k.close()
