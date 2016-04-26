__author__ = 'f'
from elasticsearch import Elasticsearch
import re,datetime
def esdate(strr):
    splitter1=strr.split(' ')
    dateandtime=splitter1[0]
    zone=splitter1[1]
    dateandtime=datetime.datetime.strptime(dateandtime,'%d/%b/%Y:%H:%M:%S')
    textmonth=''
    textday=''
    texthr=''
    textmin=''
    textsec=''
    textmilsec=''
    year= dateandtime.year
    month= dateandtime.month
    if month<10:

        textmonth='0'
    day=dateandtime.day
    if day<10:
        textday='0'
    hr= dateandtime.hour
    if hr<10:
        texthr='0'
    min= dateandtime.minute
    if min<10:
        textmin='0'
    sec= dateandtime.second
    if sec<10:
        textsec='0'
    micrsec= dateandtime.microsecond
    if micrsec<100 & micrsec>10:
        textmilsec='0'
    if micrsec<10:
        textmilsec='00'
    tosend=''
    tosend=tosend+str(year)+'-'+textmonth+str(month)\
           +'-'+textday+''+str(day)+'T'+texthr+str(hr)+':'+textmin+str(min)\
           +':'+textsec+str(sec)+'.'+textmilsec+str(micrsec)+zone[0:3]+':'+zone[3:5]
    return  tosend


def printjson(map):
    for k,v in map.iteritems():
        print '{\'Session\':\''+str(v.Session)+'\',\'Requests\':\'['
        for item in v.content:
            print '{\'Timestamp\':\''+str(item.Timestamp)+'\',\'Request_Type\':\''\
              +str(item.Request_Type)+'\',\'Requested_URL\':\''+str(item.Requested_URL)+'\',\'Request_Query\':\''+\
              str(item.Request_Query)+'\',\'Product_Id\':\''+str(item.Product_Id)+'\',\'Other_Request_query\':\''+\
              str(item.Other_Request_query)+'\',\'status\':\''+str(item.status)+'\',\'Referer\':'+\
              str(item.Referer)+'\',\'Referer_query\':\''+str(item.Referer_query)+'\',\'Referer_q\':\''+\
              str(item.Referer_q)+'\',\'Referer_q_other\':\''+str(item.Referer_q_other)+'\',\'Bytes_Sent\':\''+\
              str(item.Bytes_Sent)+'\'}'
        print '],\'IP\':\''+str(v.IP)+'\',\'Agent\':\''+str(v.Agent)+'\'}'
def printfile(map):
    fjson=open('/home/f/Desktop/Log_Sample/workfile.json','w')
    outercount=1
    for k,v in map.iteritems():
        duration=getduration(v)
        count=1
        #fjson.write('{"index":{"_id":"'+str(outercount)+'"}}')
        #fjson.write('\n')
        fjson.write( '{"Session":"'+str(v.Session)+'","Requests":[')
        for item in v.content:
            fjson.write( '{"Timestamp":"'+str(item.Timestamp)+'","Request_Type":"'\
              +str(item.Request_Type)+'","Requested_URL":"'+str(item.Requested_URL)+'","Request_Query":"'+\
              str(item.Request_Query)+'","Product_Id":"'+str(item.Product_Id)+'","Other_Request_query":"'+\
              str(item.Other_Request_query)+'","status":"'+str(item.status)+'","Referer":"'+\
              str(item.Referer)+'","Referer_query":"'+str(item.Referer_query)+'","Referer_q":"'+\
              str(item.Referer_q)+'","Referer_q_other":"'+str(item.Referer_q_other)+'","Bytes_Sent":"'+\
              str(item.Bytes_Sent)+'"}')
            if count!=len(v.content):
                fjson.write(',')
            count=count+1
        fjson.write( '],"IP":"'+str(v.IP)+'","Agent":"'+str(v.Agent)+'","Duration":"'+str(duration)+'"}')
        outercount+=1
        fjson.write('\n')

    fjson.close()

def getduration(v):

    diff=1.0
    if(len(v.content)==1):
        diff=1.0

    else:
        timestart=v.content[0].Timestamp
        #'%d/%b/%Y:%H:%M:%S'

        timestart=timestart.split('.')
        timestart=timestart[0]
       # print timestart
        timestart=datetime.datetime.strptime(timestart,"%Y-%m-%dT%H:%M:%S")
        timeend=v.content[len(v.content)-1].Timestamp
       # print '-----------------',timeend
        timeend=timeend.split('.')
        timeend=timeend[0]
       # print timeend
        timeend=datetime.datetime.strptime(timeend,"%Y-%m-%dT%H:%M:%S")
        duration=timeend-timestart
        diff=duration.total_seconds()
        if diff<1:
            diff=1.0

    return diff

   # print  'sessiond: '+str(v.Session)+'          duration: '+str(diff)


def getip(line):
    matcher = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
    return matcher[0]

def gettimestamp(line):
    #\[\d{1,2}\/(JAN|FEB|May|MAY)/\d*:\d*:\d*:\d*\s*-?(\d*)?]
    matcher = re.search(r'\[\d{1,2}\/(Jan|Feb|Mar|Apr|May|June|July|Aug|Sep|Oct|Nov|Dec|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\/\d*:\d*:\d*:\d*\s*-?(\d*)?]',line)
    return matcher.group()


def getrequesttype(line):
    matcher=re.search(r'(GET|POST)',line)
    return matcher.group()

def getrequestedurl(line):
    matcher= re.search(r'\s\/(\w+|\d+|\_+)(.*?)(?=\s)',line)
    if matcher:
        return matcher.group()
    else:
        return 'N.A'

def getstatus(line):
    matcher=re.search(r'\s\d\d\d\s',line)
    return matcher.group()

def getreferer(line):
    matcher=re.search(r'\"(http|https):\/\/www.(.*?)(?=\")',line)
    if matcher:
        return matcher.group()
    else:
        return ' N.A'

def getquery(line):
    matcher=re.search(r'\?(\w+)(.*?)(?=\=)=(\w+|\d+)(.*?)(?=\sHTTP)',line)
    if matcher:
        return matcher.group()
    else:
        return ' N.A'

def getagent(line):
    matcher=re.search(r'(\"\w+\/\d+\.\d+(\.\d+){0,2})(.*?)(?=")',line)
    return matcher.group()

def getsession(line):
    matcher =re.search(r'(SESSIONID)=(\d+)',line)
    return matcher.group(2)

def getbytessent(line):
    matcher=re.findall(r'\s\d+',line)
    return matcher[1]

def getfile():
    f = open("/home/f/Desktop/Log_Sample/access.log")
    return f
def getbaseurl(requestedurl):
    if(requestedurl=='N.A'):
        return 'N.A'
    else:
        matcher=re.match(r'(\/(.*?)(?=\?))|\/(.*?)(?=\s)',requestedurl)
        if matcher:
            return matcher.group()
        else:
            return requestedurl
def getrequestproduct(query):
    if query=='N.A':
        return 'N.A'
    else:
        matcher=re.match(r'(productid)=(.*)',)
        if matcher:
            return matcher.group(2)
        else:
            return 'N.A'
def getrequestproduct(query):
    if query=='N.A':
        return 'N.A'
    else:
        matcher=re.match(r'(productid)=(.*)',query)
        if matcher:
            return matcher.group(2)
        else:
            return 'N.A'

def getotherproduct(query):
    if query=='N.A':
        return 'N.A'
    else:
        matcher=re.match(r'(productid)=(.*)',query)
        if matcher:
            return 'N.A'
        else:
            return query

def getrefererquery(referer):
    matcher=re.search(r'(\/www.(.+?)(?=\/))((\/\w+|d+)(.*))',referer)
    if matcher:
        return matcher.group(3)
    else:
        return 'N.A'

def getrefererq(refererquery):
    if refererquery=='N.A':
        return 'N.A'
    matcher=re.search(r'(\?q)=(.*?)(?=\&)|(\?q)=(.*)',refererquery)
    if matcher:
        return matcher.group()[3:]
    else:
        return 'N.A'

def getrefererqother(refererquery):
    if refererquery=='N.A':
        return 'N.A'
    matcher=re.search(r'(\?q)=(.*?)(?=\&)|(\?q)=(.*)',refererquery)
    if matcher:
        return 'N.A'
    else:
        return refererquery


def writecsvhead(fcsv):
        fcsv.write('IP')
        fcsv.write(',')
        fcsv.write('Timestamp')
        fcsv.write(',')
        fcsv.write('Request_Type')
        fcsv.write(',')
        fcsv.write('Requested_URL')
        fcsv.write(',')
        fcsv.write('Base_URL')
        fcsv.write(',')
        fcsv.write('Request_Query')
        fcsv.write(',')
        fcsv.write('Product_Id')
        fcsv.write(',')
        fcsv.write('Other_Request_query')
        fcsv.write(',')
        fcsv.write('status')
        fcsv.write(',')
        fcsv.write('Referer')
        fcsv.write(',')
        fcsv.write('Referer_query')
        fcsv.write(',')
        fcsv.write('Referer_q')
        fcsv.write(',')
        fcsv.write('Referer_q_other')
        fcsv.write(',')
        fcsv.write('Agent')
        fcsv.write(',')
        fcsv.write('Session')
        fcsv.write(',')
        fcsv.write('Bytes_Sent')
        fcsv.write('\n')
