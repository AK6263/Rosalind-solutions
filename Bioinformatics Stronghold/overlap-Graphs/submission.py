
"""
The nodes of the graph are sequences and they are connected 
only if the suffix of the "tail end" sequence matches the 
prefix of the "head end" of the node. The length of the suffix
and prefix is k.
Here we will take k to be 3
The directed graph O3 is created

Steps to go about we will make a adjacency list
"""

from Bio import SeqIO

sequences = open("overlap-Graphs/rosalind_grph.txt", "r")
result = open("overlap-Graphs/submission.txt","w")
seq_dict = SeqIO.to_dict(SeqIO.parse(sequences,"fasta"))
k = 3
seq_keys = list(seq_dict.keys())
print(seq_keys)
for i,sequence in enumerate(seq_keys):

    s = seq_dict[sequence].seq
    suffix = s[-k:]

    for nextseq in seq_keys:
        if sequence == nextseq:
            continue
        t = seq_dict[nextseq].seq
        prefix = t[:k]

        if suffix == prefix:
            result.write("{} {}\n".format(sequence,nextseq))
            print(sequence,nextseq)
