from elasticsearch import Elasticsearch
import json
import os
'''
es=ElasticSearch()
es.bulk([es.index_op({'title': 'All About Cats', 'pages': 20}),
         es.index_op({'title': 'And Rats', 'pages': 47}),
         es.index_op({'title': 'And Bats', 'pages': 23})],
        doc_type='book',
        index='library')#es._bulk((es.index_op(jsondoc,id=jsondoc.pop'_id'))for jsondoc in jsondocs),index='emp',doc_type='person')
'''

f=open('/home/f/Desktop/Log_Sample/workfile.json','r')
es = Elasticsearch()
count=1
no=1
for line in f:
    #print line
    res = es.index(index="test-index", doc_type='tweet', id=count, body=line)
    count+=1
    if(count%2000==0):
        print count