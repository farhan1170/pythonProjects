import csv,json
class Outer_Arr:
    def __init__(self):
        self.Session=''
        self.Agent=''
        self.IP=''
        self.content=[]

class Requests:
    def __init__(self):
        self.Timestamp=''
        self.Request_Type=''
        self.Requested_URL=''
        self.Base_URL=''
        self.Request_Query=''
        self.Product_Id=''
        self.Other_Request_query=''
        self.status=''
        self.Referer=''
        self.Referer_query=''
        self.Referer_q=''
        self.Referer_q_other=''
        self.Bytes_Sent=''

map={}
f=open("/home/f/Desktop/Log_Sample/workfile.csv",'r')
reader=csv.DictReader(f)

for row in reader:
    current=row['Session']
    r=Requests()
    r.Timestamp=row['Timestamp']
    r.Request_Type=row['Request_Type']
    r.Requested_URL=row['Requested_URL']
    r.Request_Query=row['Request_Query']
    r.Product_Id=row['Product_Id']
    r.Other_Request_query=row['Other_Request_query']
    r.status=row['status']
    r.Referer=row['Referer']
    r.Referer_query=row['Referer_query']
    r.Referer_q=row['Referer_q']
    r.Referer_q_other=row['Referer_q_other']
    r.Bytes_Sent=row['Bytes_Sent']

    if(map.has_key(row['Session'])):
        outer=map.get(row['Session'])
        outer.content.append(r)
    else:
        outer=Outer_Arr()
        outer.Session=row['Session']
        outer.Agent=row['Agent']
        outer.IP=row['IP']
        outer.content.append(r)
        map[current]=outer

    prev=current
for k,v in map.iteritems():
    print '{\'Session:\''+str(v.Session)+'\',\'Requests\':\'['
    for item in v.content:
        print '{\'Timestamp\':\''+str(item.Timestamp)+'\',\'Request_Type\':\''\
              +str(item.Request_Type)+'\',\'Requested_URL\':\''+str(item.Requested_URL)+'\',\'Request_Query\':\''+\
              str(item.Request_Query)+'\',\'Product_Id\':\''+str(item.Product_Id)+'\',\'Other_Request_query:\''+\
              str(item.Other_Request_query)+'\',\'status\':\''+str(item.status)+'\',\'Referer\':'+\
              str(item.Referer)+'\',\'Referer_query\':\''+str(item.Referer_query)+'\',\'Referer_q\':\''+\
              str(item.Referer_q)+'\',\'Referer_q_other\':\''+str(item.Referer_q_other)+'\',\'Bytes_Sent\':\''+\
              str(item.Bytes_Sent)+'\'}'
    print '],\'IP\':\''+str(v.IP)+'\',\'Agent\':\''+str(v.Agent)+'\'}'
f.close()