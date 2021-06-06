from Bio.Seq import Seq

# Reading the Seq
with open("rosalind_ini.txt","r") as file:
    string=file.readline().rstrip()
    print(string)
    seq = Seq(string)


print(seq.count("A"),seq.count("C"),seq.count("G"),seq.count("T"))
