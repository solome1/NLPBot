# importing the  important libraries
from typing import final
import nltk
import sklearn
import numpy as np
import string
import random
from nltk.stem.porter import PorterStemmer
stemmer =PorterStemmer()

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# importing and reading the corpus 
f=open('all.txt','r',errors='ignore')
raw_doc=f.read()
raw_doc=raw_doc.lower()   #converts text to lowercase
nltk.download('punkt')    #using the punkt tokenizer
nltk.download('wordnet')  #using the wordnet dictionary
sent_tokens=nltk.sent_tokenize(raw_doc) #converts doc to list of sentences
word_tokens=nltk.sent_tokenize(raw_doc) #converts doc to list of words

# text preprocessing 

lemmar=nltk.stem.WordNetLemmatizer()
def lemTokens(tokens):
    return[lemmar.lemmatize(token) for token in tokens]
remove_punct_dict=dict((ord(punct),None) for punct in string.punctuation)

def LemNormalize(text):
    return lemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

#defining the greeting function

greet_input=("hello","hi","hey","greeting","what's up","selam")
greet_responce=["hello","hi","hey","greeting","what's up"]

def greet(sentence):
    for word in sentence.split():
        if word.lower() in greet_input:
            return random.choice(greet_responce)


#responce generation
# idf is picksup ana realize this words are rare and this words are repated so many times
def responce(user_responce):
      robo1_responce=''
      TfidfVec=TfidfVectorizer(tokenizer=LemNormalize,stop_words='english')
      tfidf=TfidfVec.fit_transform(sent_tokens)
      vals=cosine_similarity(tfidf[-1],tfidf)
      idx=vals.argsort()[0][-2]
      flat=vals.flatten()
      flat.sort()
      req_tfidf=flat[-2]
      if(req_tfidf==0):
          robo1_responce=robo1_responce+"I am sorry! I don't understand you"
          return robo1_responce
      else:
          robo1_responce=robo1_responce+sent_tokens[idx]
          return robo1_responce

#defining conversation start/end protocols
def botReact(mytext):
    flag=True
    while(flag==True):
        user_responce=mytext
        user_responce=user_responce.lower()
        if(user_responce!='bye'):
            if(user_responce=='thank you'):
                flag=False
                return 'you are welcome'
            else:
                if(greet(user_responce)!=None):
                    return greet(user_responce)
                else:
                    sent_tokens.append(user_responce)
                    word_tokens=nltk.word_tokenize(user_responce)
                    final_words=list(set(word_tokens))
                    return  responce(user_responce)  
        else:
            flag=False
            return "Goodbye!"