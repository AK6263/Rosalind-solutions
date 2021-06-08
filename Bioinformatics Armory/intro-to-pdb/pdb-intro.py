from Bio import ExPASy
from Bio import SwissProt

try:
    handle = ExPASy.get_sprot_raw('Q5SLP9')
except Exception as e:
    print("HTTPError: %.s"%e)

record = SwissProt.read(handle)

cross_refs = [i[2][2:] for i in record.cross_references if i[0] == "GO" and i[2][0] == "P"]
for i in cross_refs:
    print(i)
