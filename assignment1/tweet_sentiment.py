import sys
import json
import re

#dictionary for holding all sentiment scroes keyed by word/phrase
sentiment_dict = None

def init_sentiment_dict(sent_file):
    rows = ( line.split('\t') for line in sent_file.read().splitlines() )
    global sentiment_dict
    sentiment_dict = {row[0]:int(row[1]) for row in rows}

def evaluate_sentiment(tweet_file):
    for line in tweet_file.readlines():
        tweet = json.loads(line)
        tweet_text = tweet.get("text")
        if tweet_text != None:
            #print "tweet_text:" + tweet_text
            sum_sentiment_score = 0
            for word in re.findall(r'[a-z\']+', tweet_text.lower(), re.I):
                sentiment_score = sentiment_dict.get(word)
                #print "sentiment_score:" + sentiment_score
                if sentiment_score != None:
                    sum_sentiment_score += sentiment_score
            print sum_sentiment_score
        else:
            print 0

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #print "******************************************************************" 
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    init_sentiment_dict(sent_file)
    evaluate_sentiment(tweet_file)

if __name__ == '__main__':
    main()
