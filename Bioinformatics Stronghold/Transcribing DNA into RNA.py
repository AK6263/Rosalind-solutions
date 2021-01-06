f = open("rosalind_rna.txt", 'r').read().split('\n')
k = open("transcription.txt",'w')
l = ""
for i in f[0]:
    print(i)
    if i == 'T':
        print("t")
        l+='U'
    else:
        l+=i
k.write(l)
k.close()
