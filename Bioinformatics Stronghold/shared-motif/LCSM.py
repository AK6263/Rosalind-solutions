import time
start = time.time()

seqs = []
with open("./Bioinformatics Stronghold/shared-motif/input.txt", "r") as file:
    file.readline()
    seq = ""
    line = file.readline().strip()
    while line!="":
        # combine the lines before >
        if line[0] == ">":
            seqs.append(seq)
            seq = ""
        else:
            seq += line
        line = file.readline().strip()
    seqs.append(seq)
# print(seqs)
print("Sequences Loaded: Time Taken {}".format(time.time() - start))
start = time.time()
def lcs(S,T):
    # Comparison matrix if S[i-1][j-1] are same then M[i][j] = M[i-1][j-1] + 1
    M = [[0 for i in range(len(T)+1)] for j in range(len(S)+1)]
    # z has the length of the longest common substring
    z = 0
    # The substring that we have to return
    ret = []
    
    for i in range(len(S)+1):
        for j in range(len(T)+1):
            if i == 0 or j == 0:
                M[i][j] = 0
            elif S[i-1] == T[j-1]:
                M[i][j] = M[i-1][j-1] + 1
                if M[i][j] > z:
                    z = M[i][j]
                    ret = [S[(i-1)-z+1 : i]]
                elif M[i][j] == z:
                    ret = ret + [S[(i-1)-z+1:i]]
#                 printmatrix(M,S,T)
            else:
                M[i][j] = 0
            
    return ret

coms = lcs(seqs[0],seqs[1])
notcoms = []
for subs in coms:
    for seq in seqs:
        if subs not in seq:
            notcoms.append(subs)
submission = set(coms) - set(notcoms)

print("First Solution : Time Taken {}".format(time.time()-start))
start = time.time()
def substr_in_all(arr, part):
    for dna in arr:
        if dna.find(part)==-1:
            return False
    return True

def common_substr(arr, l):
    first = arr[0]
    for i in range(len(first)-l+1):
        part = first[i:i+l]
        if substr_in_all(arr, part):
            return part
    return ""

def longest_common_substr(arr):
    l = 0; r = len(arr[0])

    while l+1<r:
        mid = (l+r) // 2
        if common_substr(arr, mid)!="":
            l=mid   
        else:
            r=mid

    return common_substr(arr, l)

submission2 = longest_common_substr(seqs)
print("Igors Solution : Time Taken {}".format(time.time()-start))
print(submission,submission2)
print(0.2767932415008545 / 0.04814028739929199)