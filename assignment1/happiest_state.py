import sys
import json
import re
import operator

#dictionary for holding all sentiment scroes keyed by word/phrase
sentiment_dict = None
state_score = {}

def init_sentiment_dict(sent_file):
    rows = ( line.split('\t') for line in sent_file.read().splitlines() )
    global sentiment_dict
    sentiment_dict = {row[0]:int(row[1]) for row in rows}

def evaluate_sentiment(tweet_file):
    global state_score
    for line in tweet_file.readlines():
        tweet = json.loads(line)
        tweet_text = tweet.get("text")
        tweet_place=tweet.get("place")
        if tweet_text != None:
            #print "tweet_text:" + tweet_text
            sum_sentiment_score = 0
            for word in re.findall(r'[a-z\']+', tweet_text.lower(), re.I):
                sentiment_score = sentiment_dict.get(word)
                #print "sentiment_score:" + sentiment_score
                if sentiment_score != None:
                    sum_sentiment_score += sentiment_score
        if tweet_place != None and tweet_place.get("place_type") == 'city' and tweet_place.get("country_code") == 'US':
            state = tweet_place.get("full_name").split(", ")[1]
            score = state_score.get(state)
            if score == None:
                score = 0
            score += sum_sentiment_score
            state_score[state] = score

def print_happiest_state():
    sorted_state = sorted(state_score.iteritems(),key=operator.itemgetter(1), reverse=True)
    print sorted_state[0][0]

def main():
    #print "******************************************************************" 
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    init_sentiment_dict(sent_file)
    evaluate_sentiment(tweet_file)
    print_happiest_state()

if __name__ == '__main__':
    main()
