# read the fasta file 

sequences = []
with open("rosalind_cons.txt", "r") as file:
    file.readline()
    seq = ""
    line = file.readline().strip()
    while line!="":
        # combine the lines before >
        if line[0] == ">":
            sequences.append(seq)
            seq = ""
        else:
            seq += line
        line = file.readline().strip()
    sequences.append(seq)

# print(sequences)
# Creating a Profile Matrix
# profile = [[0]*len(sequences[0])]*4
# profile = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
profile = [[0]*len(sequences[0]) for i in range(4)]
# print(profile)
nucs = ['A', 'C', 'G', 'T']

for i in sequences: # Going through each seq
    for j,n in enumerate(i):
        profile[nucs.index(n)][j] += 1

print(profile)

# Now getting the Consensus
consensus = []
for j in range(len(profile[0])):
    maxvote = 0
    maxvote_nuc = 0
    for i in range(len(profile)):
        # print(profile[i][j])
        # votes.append(profile[i][j])
        vote = profile[i][j]
        if vote > maxvote:
            maxvote_nuc = i
            maxvote = vote
    consensus.append(nucs[maxvote_nuc])

print("".join(consensus))

with open("solution.txt", "w") as file:
    file.write("{}\n".format("".join(consensus)))
    print("".join(consensus))
    for i,n in enumerate(profile):
        file.write("{}: {}\n".format(nucs[i]," ".join([str(integer) for integer in n])))
        print("{}: {}".format(nucs[i]," ".join([str(integer) for integer in n])))
