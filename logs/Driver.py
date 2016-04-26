__author__ = 'f'
import re
import os,datetime
__author__ = 'f'
from Classes import Outer_Arr,Requests
from Base import writecsvhead,getfile,getip,gettimestamp,esdate,getrequesttype,\
    getrequestedurl,getbaseurl,getquery,getrequestproduct,getotherproduct,getstatus,getreferer,getrefererquery,\
    getrefererqother,getrefererq,getsession,getagent,getbytessent,printjson,printfile

#fcsv = open("/home/f/Desktop/Log_Sample/workfile.csv",'w')
#if os.stat("/home/f/Desktop/Log_Sample/workfile.csv").st_size == 0:
 #   writecsvhead(fcsv)
#fcsv.write('farhan')
recs=0
fr=getfile()
map={}
urlwrite=open('/home/f/Desktop/Log_Sample/urlfile.txt','w')
for line in fr:

        timestamp=gettimestamp(line)
        timestamp=timestamp[1:len(timestamp)-1].strip()
        timestamp=esdate(timestamp)
        print 'timestamp: ',timestamp
        requesttype = getrequesttype(line).strip()
        print 'requesttype: ',requesttype
        requestedurl = getrequestedurl(line).strip()
        print  'requestedurl: ',requestedurl
        matcher=re.search('(png|jpg|js|css|gif|N\.A|woff2?|ico)$',requestedurl)
        if not matcher:
            urlwrite.write(requestedurl)
            urlwrite.write('\n')
        baseurl=getbaseurl(requestedurl).strip()
        print 'baseurl: ',baseurl

        query=getquery(line)
        query=query[1:].strip()

        print 'query: ',query

        requestproduct=getrequestproduct(query).strip()

        requestotherproduct=getotherproduct(query).strip()
        print 'requested product: ',requestproduct
        status = getstatus(line).strip()
        print 'status: ',status
        referer = getreferer(line)
        referer=referer[1:].strip()
        if referer!='N.A':
            justdomain=referer.split('.')

        else:
            justdomain='N.A'
        print 'referer: ',justdomain
        refererquery=getrefererquery(referer).strip()
        print 'regerer query :',refererquery
        referersearchq=getrefererq(refererquery).strip()
        print 'referer q :',referersearchq
        referersearchqother=getrefererqother(refererquery).strip()
        print 'referer search other query: ',referersearchqother
        #sessionid = getsession(line).strip()
        bytessent=getbytessent(line).strip()
        print 'bytes sent: ',bytessent

        ip = getip(line).strip()
        print 'ip',ip
        outer=Outer_Arr()


        agent = getagent(line)
        agent=agent[1:].strip()

        print 'agent: ',agent

        print('---------------------------------------------------')

        recs=recs+1
        if(recs%10000==0):
            print 'recs= ',recs
printfile(map)

fr.close()
#fcsv.close()
urlwrite.close()