"""
nltk.download('vader_lexicon')
nltk.download('twitter_samples')
"""
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

text1 = 'Hey, what a beautiful day! How amazing it is!'
tweet1 = nltk.corpus.twitter_samples.strings()[1045]

if analyzer.polarity_scores(tweet1)['compound'] > 0:
    print('Positive text')
else:
    print('Negative Text')
