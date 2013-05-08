import sys
import json
import re

#dictionary for holding all sentiment scroes keyed by word/phrase
sentiment_dict = {}
evaluated_sentiment_dict = {}

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
            
            #print "sum:" + str(sum_sentiment_score)

            all_words = re.findall(r'[a-z\']+', tweet_text.lower())
            #all_words = tweet_text.lower().split()
            #all_words = [word for word in all_words if re.match(r'[a-z]', word)]
            #print "all_words:" + str(all_words)

            #words_to_score = [x for x in all_words if x not in sentiment_dict.keys()]
            words_to_score = list(set(all_words)-set(sentiment_dict.keys()))

            #print "words_to_score:" + str(words_to_score)
            
            # Grade the tweet normally,
            # Extract all the new words, add to new dictionary and:
            # if the tweet was overall positive, increment the sentiment of every new word in the tweet
            # if the tweet was overall negative, decrement the sentiment of every new word in the tweet
            # if the tweet was graded 0 (most of the non-European alphabet), just add the words with sentiment 0

            for word in words_to_score:
                
                evaluated_sentiment_score = evaluated_sentiment_dict.get(word)
                
                if evaluated_sentiment_score == None:
                    evaluated_sentiment_score = 0

                if sum_sentiment_score > 0:
                    evaluated_sentiment_score += 1
                if sum_sentiment_score < 0:
                    evaluated_sentiment_score -= 1

                evaluated_sentiment_dict[word] = evaluated_sentiment_score
        #else:
            #print 0
    for key in evaluated_sentiment_dict:
        print key + " " + str(evaluated_sentiment_dict[key])

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #trying to evaluate the sentiment score of any word using the small set of words with scores
    #print "******************************************************************" 
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    init_sentiment_dict(sent_file)
    evaluate_sentiment(tweet_file)

if __name__ == '__main__':
    main()
