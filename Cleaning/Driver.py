__author__ = 'f'
import re
import os,datetime
__author__ = 'f'
from Classes import  Requests,Outer_Arr
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
        r=Requests()
        timestamp=gettimestamp(line)
        timestamp=timestamp[1:len(timestamp)-1].strip()
        timestamp=esdate(timestamp)
        r.Timestamp=timestamp
        requesttype = getrequesttype(line).strip()
        r.Request_Type=requesttype
        requestedurl = getrequestedurl(line).strip()
        baseurl=getbaseurl(requestedurl).strip()
        r.Requested_URL=requestedurl
        urlwrite.write(r.Requested_URL)
        urlwrite.write('\n')
        query=getquery(line)
        query=query[1:].strip()
        r.Request_Query=query
        requestproduct=getrequestproduct(query).strip()
        r.Product_Id=requestproduct
        requestotherproduct=getotherproduct(query).strip()
        r.Other_Request_query=requestotherproduct
        status = getstatus(line).strip()
        r.status=status
        referer = getreferer(line)
        referer=referer[1:].strip()
        if referer!='N.A':
            justdomain=referer.split('.')
            r.Referer=justdomain[1]
        else:
            r.Referer='N.A'
        refererquery=getrefererquery(referer).strip()
        r.Referer_query=refererquery
        referersearchq=getrefererq(refererquery).strip()
        r.Referer_q=referersearchq
        referersearchqother=getrefererqother(refererquery).strip()
        r.Referer_q_other=referersearchqother
        sessionid = getsession(line).strip()
        bytessent=getbytessent(line).strip()
        r.Bytes_Sent=bytessent
        if map.has_key(sessionid):
            outer=map.get(sessionid)
            outer.content.append(r)
        else:
            ip = getip(line).strip()
            outer=Outer_Arr()
            outer.IP=ip
            outer.Session=sessionid
            agent = getagent(line)
            agent=agent[1:].strip()
            outer.Agent=agent
            map[sessionid]=outer
            outer.content.append(r)

        recs=recs+1
        if(recs%10000==0):
            print 'recs= ',recs
printfile(map)

fr.close()
#fcsv.close()
urlwrite.close()