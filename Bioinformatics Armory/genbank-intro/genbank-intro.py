from Bio import Entrez
Entrez.email = 'ask19ms172@iiserkol.ac.in'

try:
    handle = Entrez.esearch(db='nucleotide', term='("Asphondylia"[Organism]) AND ("2003/07/28"[Publication Date] : "2007/07/29"[Publication Date]) ')
except Exception as e:
    print("HTTPError: %.s"%e)
record = Entrez.read(handle)
print(record['Count'])