"""
To run this code, execute these two commands in Python console separately once.
import nltk
nltk.download('wordnet')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
"""

import nltk
from nltk.stem import WordNetLemmatizer

def word_compare(word1, word2):
    lemmatizer = WordNetLemmatizer()

    lemma1 = lemmatizer.lemmatize(word1, 'v')
    lemma2 = lemmatizer.lemmatize(word2, 'v')

    if lemma1 == lemma2:
        print(f"Both words mean same! '{lemma1}'")
    else:
        print(f"Both words have different meaning! '{lemma1}' & '{lemma2}' ")

def lemma_me(sent):
    lemmatizer = WordNetLemmatizer()

    sentence_tokens = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemmas = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)
    return sentence_lemmas

def sentence_compare():
    lemma1 = lemma_me('Vegetables are types of plants.')
    lemma2 = lemma_me('A vegetable is a type of plant.')

    if lemma1 == lemma2:
        print(f"Both words mean same! '{lemma1}'")
    else:
        print(f"Both words have different meaning! '{lemma1}' & '{lemma2}' ")


if __name__ == '__main__':
    # word_compare('is','was')
    sentence_compare()