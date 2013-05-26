import MapReduce
import sys

"""
Consider a simple social network dataset consisting of key-value pairs where each key is a person and each value is a friend of that person. 
Describe a MapReduce algorithm to count he number of friends each person has.

Map Input
The input is a 2 element list: [personA, personB]


personA: Name of a person formatted as a string

personB: Name of one of personA's friends formatted as a string


This implies that personB is a friend of personA, but it does not imply that personA is a friend of personB.

Reduce Output
The output should be a (person,  friend count) tuple.


person is a string and friend count is an integer describing the number of friends 'person' has.

You can test your solution to this problem using friends.json:


        python friend_count.py friends.json


You can verify your solution against friend_count.json.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, friend)

def reducer(key, list_of_friends):
    # key: person
    # value: list of friends
    
    list_of_friends = set(list_of_friends)
    mr.emit((key, len(list_of_friends)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
