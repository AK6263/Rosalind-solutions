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
print(submission2)
print("Igors Solution : Time Taken {}".format(time.time()-start))