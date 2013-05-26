import MapReduce
import sys
from collections import Counter

"""
Problem 4
The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. Implement a MapReduce algorithm to check 
whether this property holds. Generate a list of all non-symmetric friend relationships.

Map Input
The input is a 2 element list: [personA, personB]


personA: Name of a person formatted as a string

personB: Name of one of personA's friends formatted as a string


This implies that personB is a friend of personA, but it does not imply that personA is a friend of personB.

Reduce Output
The output should be the (person, friend) and (friend, person) tuples for each asymmetric friendship.


Note however that only one of the (person, friend) or (friend, person) output tuples will exist in the input. This indicates friendship asymmetry.


You can test your solution to this problem using friends.json:


        python asymmetric_friendships.py friends.json


You can verify your solution against asymmetric_friendships.json.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    person = record[0]
    friend = record[1]

    # A has a friend B
    mr.emit_intermediate(person, friend)

    # B is friended by A
    mr.emit_intermediate(friend, person)

def reducer(key, list_of_friends):
    # key: person
    # value: list of friends
    
    # if a friend repeats in the list, it is symmetric.
    c = Counter(list_of_friends)
    # print c

    # new list with only non-repeating friends
    asymmetric_friendships = []
    for friend in list_of_friends:
        if (c.get(friend) == 1):
            asymmetric_friendships.append(friend)
    
    for friend in asymmetric_friendships:
        mr.emit((key, friend))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
