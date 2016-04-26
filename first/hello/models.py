from django.db import models
import sys
import os

import string
import nltk
import os
import json
import nlp_process

from nltk import PorterStemmer
from nltk.corpus import stopwords
from extract_sentiment import decircExtractSentiment
#from extract_entities import decircExtractEntities
sys.path.append(os.path.abspath("/~/el/socialstore"))

# Create your models here.
class Steps:
    def classification(self,text):
        dn=nlp_process.DecircNLP()
        arr=[]
        arr.append(text)
        #arr.append("i like abhay film i like aamir khan ghajini movie chennai express movie is good")
        rec=dn.process_data(arr,0,1)
        print 'rec',rec
        return rec

    def sentiment(self,text):
        dn=nlp_process.DecircNLP()
        arr=[]
        arr.append(text)
        #arr.append("i like abhay film i like aamir khan ghajini movie chennai express movie is good")
        rec=dn.process_data(arr,0,2)
        print 'rec',rec
        return rec

    def er(self,text):
        dn=nlp_process.DecircNLP()
        arr=[]
        arr.append(text)
        #arr.append("i like abhay film i like aamir khan ghajini movie chennai express movie is good")
        rec=dn.process_data(arr,0,3)
        print 'rec',rec
        return rec
    def all(self,text):
        dn=nlp_process.DecircNLP()
        arr=[]
        arr.append(text)
        classification=dn.process_data(arr,0,1)
        sentiment=dn.process_data(arr,0,2)
        er=dn.process_data(arr,0,3)
