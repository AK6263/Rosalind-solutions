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
print(submission)
print("Time Taken {}".format(time.time()-start))