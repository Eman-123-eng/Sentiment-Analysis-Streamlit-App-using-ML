import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.tokenize import word_tokenize



import string
punc=string.punctuation

def preprocessing(text):
  
  text = text.lower()
  text=''.join([char for char in text if char not in punc])
  # print(text)
  stopwords_En=nltk.corpus.stopwords.words('english')
  tokens = word_tokenize(text)
  # print(tokens)
  no_stopwords=[word for word in tokens if word not in stopwords_En]
  wn=nltk.WordNetLemmatizer()
  # print("f jknmp;kmnkv gf")
  lemmatized_text=[wn.lemmatize(word) for word in no_stopwords]
  lemmatized_text = ' '.join(lemmatized_text)
  return lemmatized_text