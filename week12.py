# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:07:16 2020

@author: Paloma
"""

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

corpus = [
        'This is the first document.',
        'This is the second second document.',
        'And the third one.',
        'Is this the first document?'
        '']

X = vectorizer.fit_transform(corpus)

features = vectorizer.get_feature_names()
X_array = X.toarray()

from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer()

tfidf = transformer.fit_transform(X_array)

tfidf_array = tfidf.toarray()

import tensorflow as tf
from keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)
words = tokenizer.word_index
encoded_text = tokenizer.texts_to_sequences(corpus)