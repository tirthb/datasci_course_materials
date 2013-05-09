import sys
import json
import re
import operator

#hashtag:count
hash_count = {}

def init_hash_count(tweet_file):
    global hash_count
    
    for line in tweet_file.readlines():
        tweet = json.loads(line)
        tweet_entities = tweet.get("entities")
        if tweet_entities != None:
            tags = tweet_entities.get("hashtags")
            if tags != None:
                for tag in tags:
                    hashtag = tag["text"]
                    count = hash_count.get(hashtag)
                    if count == None:
                        count = 0
                    count += 1
                    hash_count[hashtag] = count
                    #print hashtag + ":" + str(count)

def print_top_ten():

    sorted_hash_count = sorted(hash_count.iteritems(), key=operator.itemgetter(1), reverse = True)
    #print sorted_hash_count

    for (hashtag, count) in sorted_hash_count[:10]:
         print hashtag.encode("utf-8") + " " + str(count)

def main():
    #print "******************************************************************" 
    tweet_file = open(sys.argv[1])
    init_hash_count(tweet_file)
    print_top_ten()

if __name__ == '__main__':
    main()
