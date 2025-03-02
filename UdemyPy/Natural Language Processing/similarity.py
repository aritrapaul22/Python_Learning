from comparison import lemma_me
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk, pandas

text = 'Originally, vegetables were collected from the wild by hunter-gatherers.  Vegetables are all plants.  Vegetables can be eatern either raw or cooked.'
question = 'What are vegetables?'

sentence_tokens = nltk.sent_tokenize(text)
sentence_tokens.append(question)

tv = TfidfVectorizer(tokenizer=lemma_me)
tf = tv.fit_transform(sentence_tokens)

# df = pandas.DataFrame(tf.toarray(), columns=tv.get_feature_names_out())

values = cosine_similarity(tf[-1], tf)
index = values.argsort()[0][2]
values_flat = values.flatten()
values_flat.sort()

coeff = values_flat[-2]

if coeff > 0.3:
    print(sentence_tokens[index])
