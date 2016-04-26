# Entity Recognition 

import re
import os
from ConfigParser import SafeConfigParser

def data_clean(string):
	string = string.replace('\'',' ')
	string = string.replace('\\',' ')
	string = string.replace('/',' ')	
	return string

# Non ascii removal
def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

# Write to DB
def insertDB(feedFromId,item,cat):
	query = {
			"item_id": item[0],
			"item_name" : data_clean(strip_non_ascii(item[1])),
			"item_category": data_clean(strip_non_ascii(item[2]))
			}
	return query
	
	
class decircExtractEntities:
	def entity_recognition(self,user_feed,named_entities_list,user_id,category) :
		print 'user feed',user_feed
		print 'named_entities_list',named_entities_list
		print 'user_id',user_id
		print 'category',category
		named_entities_found=[]
		Db_batch =[]
		# Write extracted feeds to file	
		write_feed = open(os.path.dirname(os.path.abspath(__file__))+'/NER_feed.txt','a+')
		for word in named_entities_list:
			if (word !=''):
				word =word.split('|')
				if(re.search(word[1],user_feed)):
					write_feed.write(user_feed)
					write_feed.write('\n')
					named_entities_found.append(word)  
		for item in sorted(named_entities_found) :
			if item !='\n':
				result = insertDB(user_id,item,category)
				Db_batch.append(result)
		return Db_batch
		write_feed.close()
		