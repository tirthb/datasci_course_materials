import sys
import json
import re
import operator

#dictionary for holding all word counts
word_count = {}
all_words_count = 0

def init_word_count(tweet_file):
    global word_count
    global all_words_count
    for line in tweet_file.readlines():
        tweet = json.loads(line)
        tweet_text = tweet.get("text")
        if tweet_text != None:
            #print "tweet_text:" + tweet_text
            for word in tweet_text.split():
                all_words_count += 1
                count = word_count.get(word)
                if count == None:
                    count = 0
                count += 1
                word_count[word] = count
                #print word + ":" + str(count)

def calculate_frequency():

    sorted_word_count = sorted(word_count.iteritems(), key=operator.itemgetter(1))
    sorted_word_count.reverse()

    #print all_words_count
    #print sorted_word_count

    word_frequency = [(word, count/float(all_words_count)) for word, count in sorted_word_count]
    
    for (word, frequency) in word_frequency:
         print word.encode("utf-8") + " " + str(frequency)

def main():
    #print "******************************************************************" 
    tweet_file = open(sys.argv[1])
    init_word_count(tweet_file)
    calculate_frequency()

if __name__ == '__main__':
    main()
