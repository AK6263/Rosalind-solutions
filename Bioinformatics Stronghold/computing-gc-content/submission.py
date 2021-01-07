#  reading the fasta file
import io 

fasta = open('computing-gc-content/rosalind_gc.txt',"r").read().splitlines()
# print(fasta)

# storing the name best seq
best_seq_name = None
best_seq = None
best_gc_score = 0

def calc_gc_score(seq):
    counts = 0
    seq_length = len(seq)
    for i in seq:
        if i in "GC":
            counts += 1 
    # print(seq,seq_length)
    return (counts/seq_length) * 100

def get_seq(i):
    """
    input get the starting of the seq
    return: the seq
    """
    seq = []
    for k,line in enumerate(fasta[i:]):
        if line[0] != '>':
            seq.append(line)
            if k+1 == len(fasta):
                break
        else:
            break

    return "".join(seq)
for i, line  in enumerate(fasta):
    if line[0] == '>':
        seqname = line[1:]
        seq = get_seq(i+1)
        gc_score = calc_gc_score(seq)
        if gc_score > best_gc_score:
            best_gc_score = gc_score
            best_seq = seq
            best_seq_name = seqname

print(best_seq_name)
print(best_seq)
print(best_gc_score)