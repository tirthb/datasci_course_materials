import MapReduce
import sys

"""
Problem 1
Create an Inverted index. Given a set of documents, an inverted index is a dictionary where each word is associated with a list of the document identifiers in which that word appears.  

Mapper Input
The input is a 2 element list: [document_id, text]


document_id: document identifier formatted as a string

text: text of the document formatted as a string


The document text may have words in various cases or elements of punctuation. Do not modify the string, and treat each token as if it was a valid word. (That is, just use value.split())

Reducer Output
The output should be a (word, document ID list) tuple where word is a String and document ID list is a list of Strings.


You can test your solution to this problem using books.json:

        python inverted_index.py books.json


You can verify your solution against inverted_index.json.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: document identifier
    list_of_docs = []
    for v in list_of_values:
      list_of_docs.append(v)
    list_of_docs = list(set(list_of_docs))
    mr.emit((key, list_of_docs))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
