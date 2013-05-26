import MapReduce
import sys

"""
Problem 2
Implement a relational join as a MapReduce query


Consider the query:


SELECT * 

FROM Orders, LineItem 

WHERE Order.order_id = LineItem.order_id


Your MapReduce query should produce the same information as this SQL query.  You can consider the two input tables, Order and LineItem, as one big concatenated bag of records which gets fed into the map function record by record.                                                

Map Input
The input will be database records formatted as lists of Strings.


Every list element corresponds to a different field in it's corresponding record.


The first item(index 0) in each record is a string that identifies which table the record originates from. This field has two possible values:


        'line_item' indicates that the record is a line item.

        'order' indicates that the record is an order.


The second element(index 1) in each record is the order_id.


LineItem records have 17 elements including the identifier string.

Order records have 10 elements including the identifier string.

Reduce Output
The output should be a joined record.


The result should be a single list of length 27 that contains the fields from the order record followed by the fields from the line item record. Each list element should be a string.


You can test your solution to this problem using records.json:


        python join.py records.json


You can verify your solution against join.json.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    
    # the first record will be order, rest are line items
    order = list_of_values[0]
    
    for x in range(1,len(list_of_values)):
      record = []
      record.extend(order)
      record.extend(list_of_values[x])
      mr.emit(record)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
