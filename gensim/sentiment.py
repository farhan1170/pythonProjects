from sklearn.cross_validation import train_test_split
from gensim.models.word2vec import Word2Vec
import numpy as np
from sklearn.preprocessing import scale
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


def buildWordVector(text, size):
    vec = np.zeros(size).reshape((1, size))
    count = 0.
    for word in text:
        try:
            vec += model[word].reshape((1, size))
            count += 1.
        except KeyError:
            continue
    if count != 0:
        vec /= count
    return vec

with open('/home/f/Desktop/pos1.txt', 'r') as infile:
    pos_tweets = infile.readlines()

print 'pos_tweets'


with open('/home/f/Desktop/neg1.txt', 'r') as infile:
    neg_tweets = infile.readlines()
print 'negtweets'
#use 1 for positive sentiment, 0 for negative
y = np.concatenate((np.ones(len(pos_tweets)), np.zeros(len(neg_tweets))))

x_train, x_test, y_train, y_test = train_test_split(np.concatenate((pos_tweets, neg_tweets)), y, test_size=0.2)

#Do some very minor text preprocessing
def cleanText(corpus):
    corpus = [z.lower().replace('\n','').split() for z in corpus]
    return corpus

x_train = cleanText(x_train)
print 'train cleared'
#print(x_train)
x_test = cleanText(x_test)
print 'test cleared'
n_dim = 200
#model = Word2Vec(x_train, min_count=1,size=200)
ft=open("some.txt",'w')
ft.write( str(x_train))
ft.close()
model= Word2Vec(size=n_dim, min_count=20)
print 'model initiate'
model.build_vocab(x_train)
print 'model vocab'
model.train(x_train)
print 'model trained'
model_name = "300features_40minwords_10context"
model.save(model_name)



print model.similarity('love','like')

train_vecs = np.concatenate([buildWordVector(z, n_dim) for z in x_train])
train_vecs = scale(train_vecs)
'''
#Train word2vec on test tweets
model.train(x_test)
#Build test tweet vectors then scale
test_vecs = np.concatenate([buildWordVector(z, n_dim) for z in x_test])
test_vecs = scale(test_vecs)

forest = RandomForestClassifier( n_estimators = 100 )
forest = forest.fit( train_vecs,x_train )
result = forest.predict( test_vecs )
print  result
output = pd.DataFrame( data={"text":x_test, "sentiment":result} )
output.to_csv( "Bag_of_Words_model.csv", index=False, quoting=3 )'''
'''
lr = SGDClassifier(loss='log', penalty='l1')
lr.fit(train_vecs, y_train)

print 'Test Accuracy: %.2f'%lr.score(test_vecs, y_test)

pred_probas = lr.predict_proba(test_vecs)[:,1]

fpr,tpr,_ = roc_curve(y_test, pred_probas)
roc_auc = auc(fpr,tpr)
plt.plot(fpr,tpr,label='area = %.2f' %roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.legend(loc='lower right')

plt.show()
'''
'''
#Initialize model and build vocab

imdb_w2v = Word2Vec(size=n_dim, min_count=10)
imdb_w2v.build_vocab(x_train)
imdb_w2v = Word2Vec(x_train)

#Train the model over train_reviews (this may take several minutes)
imdb_w2v.train(x_train)
'''