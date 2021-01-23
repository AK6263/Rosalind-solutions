# We need to create a overlap graph with weighted edges that
# is the common overlap between two sequences

# The following are the steps that can be taken
# we will be using greedy search( to find the shortest path
# the path that has the most overlap will we considered

# Step 1 : find the overlap and run "k" from "length of the read" -> 1
# step 2 : remove the two reads from the lists and then append the resultant
#          to the list 

reads = []


with open("rosalind_long.txt", "r") as sequences:
    sequences.readline()
    seq = ""
    line = sequences.readline().strip()
    while line!="":
        # combine the lines before >
        if line[0] == ">":
            reads.append(seq)
            seq = ""
        else:
            seq += line
        line = sequences.readline().strip()
    reads.append(seq)

print(len(reads))

def check_ovelap(reads):
    """
    we can keep calling this function as well as changing the reads list
    """
    for read in reads:
        for k in range(len(reads[-1]),0,-1):
            suffix = read[-k:]
            for read_2 in reads:
                if read != read_2:
                    prefix = read_2[:k]
                    if suffix == prefix:
                        combine = read + read_2[k:]
                        reads.remove(read)
                        reads.remove(read_2)
                        reads.insert(0, combine)
                        return reads
                    elif read_2[-k:] == read[:k]:
                        combine = read_2 + read[k:]
                        reads.remove(read)
                        reads.remove(read_2)
                        reads.insert(0, combine)
                        return reads
    return reads

while len(reads) > 1:
    reads = check_ovelap(reads)
    print(len(reads))

print(reads)
with open("submission.txt","w") as submission:
    submission.write(reads[0])