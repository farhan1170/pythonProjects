import re
import os,datetime
__author__ = 'f'

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

fcsv = open("/home/f/Desktop/Log_Sample/workfile.csv",'w')
if os.stat("/home/f/Desktop/Log_Sample/workfile.csv").st_size == 0:
    writecsvhead(fcsv)
#fcsv.write('farhan')
recs=0
fr=getfile()
for line in fr:

        #print line
        ip = getip(line).strip()
        #print 'IP= ',ip
        fcsv.write('"'+ip+'"')
        fcsv.write(',')
        timestamp=gettimestamp(line)
        timestamp=timestamp[1:len(timestamp)-1].strip()
        timestamp=esdate(timestamp)
        #print 'Timestamp= ', timestamp
        fcsv.write(str(timestamp))
        fcsv.write(',')
        requesttype = getrequesttype(line).strip()
        #print 'Request Type ',requesttype
        fcsv.write(requesttype)
        fcsv.write(',')
        requestedurl = getrequestedurl(line).strip()
        #print 'Requested URL= ',requestedurl
        fcsv.write(requestedurl)
        fcsv.write(',')
        baseurl=getbaseurl(requestedurl).strip()
        fcsv.write(baseurl)
        fcsv.write(',')
        query=getquery(line)
        query=query[1:].strip()
        #print 'Query= ',query
        fcsv.write(query)
        fcsv.write(',')
        requestproduct=getrequestproduct(query).strip()
        fcsv.write(requestproduct)
        fcsv.write(',')
        requestotherproduct=getotherproduct(query).strip()
        fcsv.write(requestotherproduct)
        fcsv.write(',')
        status = getstatus(line).strip()
        #print 'status= ',status
        fcsv.write(status)
        fcsv.write(',')
        referer = getreferer(line)
        referer=referer[1:].strip()
        #print 'Referer= ',referer
        fcsv.write(referer)
        fcsv.write(',')
        refererquery=getrefererquery(referer).strip()
        fcsv.write(refererquery)
        fcsv.write(',')
        referersearchq=getrefererq(refererquery).strip()
        fcsv.write(referersearchq)
        fcsv.write(',')
        referersearchqother=getrefererqother(refererquery).strip()
        fcsv.write(referersearchqother)
        fcsv.write(',')
        agent = getagent(line)
        agent=agent[1:].strip()
        #print 'Agent= ',agent
        fcsv.write('"'+agent+'"')
        fcsv.write(',')
        sessionid = getsession(line).strip()
        #print 'Session= ',sessionid
        fcsv.write(sessionid)
        fcsv.write(',')
        bytessent=getbytessent(line).strip()
        fcsv.write('"'+bytessent+'"')
        #print 'Bytes Sent= ',bytessent
        fcsv.write('\n')
        recs=recs+1
        if(recs%10000==0):
            print 'recs= ',recs
fr.close()
fcsv.close()