
# Sentiment Analysis
import os
path =os.path.dirname(os.path.abspath(__file__))

## Read Dictionary from file, Return words in lowercase
def read_file (file_name, mode):
	file_content = open(file_name,mode).read().lower().replace("\n"," ")
	return file_content.split()
	
positive_words_list = list(read_file(path+"/Datasets/Sentiment/positive.txt","r"))
negative_words_list = list(read_file(path+"/Datasets/Sentiment/negative.txt","r"))

class decircExtractSentiment(object):
	
	def sentiment_analysis(self,total_words):
		positive_word_count = negative_word_count = 0
		positve_words_found = []
		negative_words_found = []

		for word in total_words:
			positive_word_count +=  positive_words_list.count(word)
			negative_word_count +=  negative_words_list.count(word)
		
        # Sentiment Classification
		if (positive_word_count>negative_word_count):
			#print "\n Positive Sentiment Words Are :", positve_words_found	
			#print "\n Negative Sentiment Words Are :", negative_words_found
			#print "\n Post Classified as Positive !!! \n"	
			sentiment = "positive"+" score "+str(positive_word_count-negative_word_count)

		else:
			#print "\n Negative Sentiment Words Are :", negative_words_found	
			#print "\n Positive Sentiment Words Are :", positve_words_found	
			#print "\n Post Classified as Negative  !!! \n"
			sentiment = "negative"+" score "+str(positive_word_count-negative_word_count)

		return sentiment
	
	