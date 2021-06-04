from Bio.Seq import Seq
# REading the files
rna = ""
with open("rosalind_prot.txt","r") as f:
    for line in f:
        rna = rna + line.rstrip()

###### Method One Without Biopython ######

aminoacids = {
    'UUU':'F',  'CUU':'L',  'AUU': 'I',  'GUU': 'V',
    'UUC' : 'F',      'CUC': 'L'    ,  'AUC': 'I'   ,   'GUC': 'V',
    'UUA' : 'L',      'CUA': 'L'   ,   'AUA':'I'   ,   'GUA' :'V',
    'UUG' : 'L',      'CUG':'L' ,     'AUG' :'M'   ,   'GUG': 'V',
    'UCU' : 'S',      'CCU': 'P' ,     'ACU' :'T'  ,    'GCU': 'A',
    'UCC': 'S',      'CCC': 'P'   ,   'ACC':'T'   ,   'GCC': 'A',
    'UCA': 'S' ,     'CCA': 'P'  ,    'ACA': 'T' ,     'GCA' :'A',
    'UCG': 'S' ,     'CCG':'P'  ,    'ACG': 'T'    ,  'GCG': 'A',
    'UAU': 'Y' ,     'CAU':'H'     , 'AAU' :'N'   ,   'GAU': 'D',
    'UAC': 'Y'    ,  'CAC':'H'   ,   'AAC' :'N'   ,   'GAC': 'D',
    'UAA': 'Stop'  , 'CAA' :'Q'   ,   'AAA' :'K'   ,   'GAA': 'E',
    'UAG': 'Stop'  , 'CAG': 'Q'  ,    'AAG': 'K',      'GAG': 'E',
    'UGU': 'C'   ,   'CGU' :'R'  ,    'AGU': 'S' ,     'GGU': 'G',
    'UGC': 'C'     , 'CGC' :'R'  ,    'AGC' :'S' ,     'GGC': 'G',
    'UGA': 'Stop' ,  'CGA': 'R'    ,  'AGA' :'R'  ,    'GGA': 'G',
    'UGG': 'W'     , 'CGG': 'R'    ,  'AGG': 'R'  ,    'GGG': 'G'
}
protein = ""
for i in range(0, len(rna), 3):
    # print(i)
    protein = protein + aminoacids[rna[i:i+3]]
print(protein)


###### Method Two With Biopython ######
mrna = Seq(rna)
prot = mrna.translate()
print(prot)
print(prot[:-1] == protein[:-4])
# with open("prot_sol.txt","w") as file:
#     print(prot)
#     file.write(str(prot.seq) + "\n") 