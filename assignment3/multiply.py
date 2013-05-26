import MapReduce
import sys

"""
Assume you have two matrices A and B in a sparse matrix format, where each record is of the form i, j, value.  
Design a MapReduce algorithm to compute matrix multiplication: A x B

Map Input
The input to the map function will be matrix row records formatted as lists. 
Each list will have the format [matrix, i, j, value] where matrix is a string and i, j, and value are integers.


The first item, matrix, is a string that identifies which matrix the record originates from. This field has two possible values:


        'an' indicates that the record is from matrix A

        'b' indicates that the record is from matrix B


Reduce Output
The output from the reduce function will also be matrix row records formatted as tuples. Each tuple will have the format (i, j, value) where each element is an integer.


You can test your solution to this problem using matrix.json:


        python multiply.py matrix.json


You can verify your solution against multiply.json.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: 
    # value: 
    matrix_name = record[0]
    row = record[1]
    col = record[2]

    if (matrix_name == 'a'):
      for x in range(0, 5):
        # print "%s: (%s, %s, %s)" % (matrix_name, row, x, record[3])
        mr.emit_intermediate((row, x), record)

    if (matrix_name == 'b'):
      for x in range(0, 5):
        # print "%s: (%s, %s, %s)" % (matrix_name, x, col, record[3])
        mr.emit_intermediate((x, col), record)

def reducer(key, list_of_values):
    # key: row, col
    # value: list of A and B values
    
    a, b = [], []
    
    for element in list_of_values:
      if element[0] == 'a':
        a.append(element)
      else:
        b.append(element)

    # print key
    # print a
    # print b

    total = 0

    for xa in a:
      for xb in b:
        if xa[2] == xb[1]:
          total += xa[3] * xb[3]
    
    mr.emit((key[0],key[1],total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
