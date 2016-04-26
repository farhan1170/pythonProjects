
# -*- encoding: utf-8 -*-z

import string
import nltk
import os
import json

from nltk import PorterStemmer
from nltk.corpus import stopwords
from extract_sentiment import decircExtractSentiment
from extract_entities import decircExtractEntities

path =os.path.dirname(os.path.abspath(__file__))

des = decircExtractSentiment()
dee  = decircExtractEntities()

def read_file (file_name, mode):
	file_content = open(file_name,mode).read().lower().replace("\n"," ")
	return file_content.split()

def stem_data(words):
	stopwords =open(path+"/Datasets/stopwords.txt","r").read().split()
	stemmer = PorterStemmer()
	after_stem =[]
	for word in words :
		word = word.decode("utf8")
		if word not in stopwords:
			after_stem.append(PorterStemmer().stem_word(word))
	return after_stem

## Dictionaries

movie_words = list(set(stem_data(read_file(path+"/Datasets/Movies/movieMfw.txt","r"))))
music_words = list(set(stem_data(read_file(path+"/Datasets/Music/musicMfw.txt","r"))))
game_words = list(set(stem_data(read_file(path+"/Datasets/Games/gamesMfw.txt","r"))))

movie_named_entities = open(path+"/Datasets/Movies/movieNerBolMal.txt","r").read().lower().split('\n') + open(path+"/Datasets/Movies/movieNerBolFem.txt","r").read().lower().split('\n') + open(path+"/Datasets/Movies/movieNerBolNam.txt","r").read().lower().split('\n')
music_named_entities = open(path+"/Datasets/Music/musicNerBolFem.txt","r").read().lower().split('\n') + open(path+"/Datasets/Music/musicNerBolMal.txt","r").read().lower().split('\n') + open(path+"/Datasets/Music/musicNam.txt","r").read().lower().split('\n')
game_named_entities = open(path+"/Datasets/Games/gamesNer.txt","r").read().lower().split('\n')


## Write feeds to file
class DecircNLP(object):

	def classify_data(self,feed_length,category_word_count,category_default):
		if feed_length > 50 and category_word_count > 10:
			category = category_default
		elif feed_length > 25 and category_word_count > 5:
			category = category_default
		elif feed_length > 10 and category_word_count > 2:
			category = category_default
		elif feed_length > 1 and category_word_count >= 1:
			category = category_default
		else:
			category = "None"
		return category

	def process_data(self,feed_list, user_id,code):
		print feed_list
		NLP_List=[]
		# Write extracted feeds to file	
		write_feed = open(os.path.dirname(os.path.abspath(__file__))+'/user_feed.txt','w')
		for feed in feed_list:
			movie_words_count = game_words_count = music_words_count = 0
                        write_feed.write(feed)
                        write_feed.write('\n')
			for punct in string.punctuation:
					feed = feed.replace(punct," ")

			lower_feed=feed.lower()
			words =lower_feed.split()
			stem_word= stem_data(words)
			print stem_word
			for word in stem_word:
			    movie_words_count += movie_words.count(word)
			    music_words_count += music_words.count(word)
			    game_words_count += game_words.count(word)

			if movie_words_count>0 and movie_words_count>=music_words_count and movie_words_count>=game_words_count :
				category_default="Movie"

				category = self.classify_data(len(stem_word),movie_words_count,category_default)
				if code==1:
					return category+" score "+str(movie_words_count)
				if (category !='None'):
					sentimentcount = des.sentiment_analysis(words)
					sentiment=sentimentcount.split(' ')
					sentiment=sentiment[0]
					if code==2:
						return sentimentcount
				if (sentiment == 'positive'):
					NLP_List.extend(dee.entity_recognition(lower_feed,movie_named_entities,user_id,category))

			elif music_words_count>0 and music_words_count>=movie_words_count and music_words_count>game_words_count :
				category_default="Music"+" score is"+music_words_count
				category = self.classify_data(len(stem_word),music_words_count,category_default)
				if code==1:
					return category+" score "+str(music_words_count)
				if (category !='None'):
					sentimentcount = des.sentiment_analysis(words)
					sentiment=sentimentcount.split(' ')
					sentiment=sentiment[0]
					if code==2:
						return sentimentcount
				if (sentiment == 'positive'):
					NLP_List.extend(dee.entity_recognition(lower_feed,music_named_entities,user_id,category))

			elif game_words_count>0 and game_words_count>movie_words_count and game_words_count>=music_words_count :
				category_default="Games"
				category = self.classify_data(len(stem_word),game_words_count,category_default)
				if code==1:
					return category+" score "+str(game_words_count)
				if (category!='None'):
					sentimentcount = des.sentiment_analysis(words)
					sentiment=sentimentcount.split(' ')
					sentiment=sentiment[0]
					if code==2:
						return sentimentcount
				if (sentiment == 'positive'):
					NLP_List.extend(dee.entity_recognition(lower_feed,game_named_entities,user_id,category))					
		write_feed.close()
		return NLP_List