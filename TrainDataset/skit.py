from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from utf8 import convert
from sklearn import datasets
__author__ = 'f'
'''
def read_file (file_name, mode):
	file_content = open(file_name,mode).read().lower().replace("\n"," ")
	return file_content.split()

path='/home/f/socialstore/Autoscale'
movie_words = list(set(read_file(path+"/Datasets/Movies/movieMfw.txt","r")))
music_words = list(set(read_file(path+"/Datasets/Music/musicMfw.txt","r")))
game_words = list(set(read_file(path+"/Datasets/Games/gamesMfw.txt","r")))

categories = ['movie','music','game']
count_vect = CountVectorizer()
filename="/home/f/Desktop/train_utf8.txt"
read_train=open(filename,'r')

X_train_counts = count_vect.fit_transform(read_train)
tfidf_transformer = TfidfTransformer()

X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
read_train.close()
'''

iris = datasets.load_iris()
digits = datasets.load_digits()
print digits.data