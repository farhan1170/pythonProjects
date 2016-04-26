from sklearn.cross_validation import train_test_split
import nltk
import gensim
from gensim import  models, similarities
from gensim.models import word2vec


with open('twitter_data/pos_tweets.txt', 'r') as infile:
    pos_tweets = infile.readlines()

with open('twitter_data/neg_tweets.txt', 'r') as infile:
    neg_tweets = infile.readlines()

#use 1 for positive sentiment, 0 for negative
y = np.concatenate((np.ones(len(pos_tweets)), np.zeros(len(neg_tweets))))

x_train, x_test, y_train, y_test = train_test_split(np.concatenate((pos_tweets, neg_tweets)), y, test_size=0.2)

#Do some very minor text preprocessing
def cleanText(corpus):
    corpus = [z.lower().replace('\n','').split() for z in corpus]
    return corpus

x_train = cleanText(x_train)
x_test = cleanText(x_test)

n_dim = 300
#Initialize model and build vocab
imdb_w2v = word2vec(size=n_dim, min_count=10)
imdb_w2v.build_vocab(x_train)

#Train the model over train_reviews (this may take several minutes)
imdb_w2v.train(x_train)