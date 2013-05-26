import MapReduce
import sys

"""
Consider a set of key-value pairs where each key is sequence id and each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....


Write a MapReduce query to remove the last 10 characters from each string of nucleotides, then remove any duplicates generated.

Map Input
The input is a 2 element list: [sequence id, nucleotides]


sequence id: Unique identifier formatted as a string

nucleotides: Sequence of nucleotides formatted as a string

Reduce Output
The output from the reduce function should be the unique trimmed nucleotide strings.


You can test your solution to this problem using dna.json:


        python unique_trims.py dna.json


You can verify your solution against unique_trims.json.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence
    # value: nuceotides
    key = record[0]
    value = record[1]
    mr.emit_intermediate(value[:-10], 1)

def reducer(key, list_of_values):
    # key: trimmed nucleotide
    # value: list of occurrence counts
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
