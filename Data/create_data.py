import nltk
import gensim
from gensim import corpora, models, similarities
from gensim.models import word2vec
import string
from nltk.corpus import stopwords
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import  os

cachedStopWords = stopwords.words("english")
class MySentences(object):
     def __init__(self, dirname):
         self.dirname = dirname

     def __iter__(self):
         for fname in os.listdir(self.dirname):
             for line in open(os.path.join(self.dirname, fname)):
                 yield line.split()


def stemmer(tokens):
    try:
     lemma = nltk.wordnet.WordNetLemmatizer()

     stem_word = ""
     for word in tokens:
        stem_word = stem_word + " " + lemma.lemmatize(word)
    except Exception:
      #print '----INVALID in stemming----'
      return '----INVALID in stemming----'


    return stem_word


def tokenize(text):
    try:
        text = "".join(
            [ch for ch in text if ch not in string.punctuation])
        words = ""
        for word in text.split():
            if word.decode('utf-8') not in stopwords.words("english"):
                words = words + " " + word
            else:
                words = words + " "
        tokens = nltk.word_tokenize(words)
        stems = stemmer(tokens)
    except Exception:
        #print '----INVALID in tokenizing----'
        return '----INVALID in tokenizing----'
    return stems


categories = [0, 1, 2, 3]
count = 0;
path = '/home/f/socialstore/Autoscale'
fwrite = open('/home/f/Desktop/stemmed.txt', 'w')
with open('/home/f/Desktop/train_utf8.txt', 'r') as feeds:
    for feed in feeds:
        lower_feed = feed.lower()
        tokens = tokenize(lower_feed)
        #print('tokens',tokens)
        #model = gensim.models.Word2Vec()
        #print(tokens)
        #data=unicodedata.normalize('NFKD', tokens).encode('ascii','ignore')
        fwrite.write(tokens)
        fwrite.write('\n')
        count += 1
        if (count % 1000 == 0):
            print(count)
fwrite.close()
sentences = MySentences('/home/f/Desktop/stemmed.txt')
model = gensim.models.Word2Vec(sentences,min_count=50,size=200)
