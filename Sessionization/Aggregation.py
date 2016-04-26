import csv,sys
__author__ = 'f'

f=open("/home/f/Desktop/Log_Sample/demo.csv",'r')
reader=csv.DictReader(f)
prev=''
for row in reader:




    '''if session!=prev:
        print '-------------------------------------------'
        print 'session ',row['Session']
        print 'ip ' ,row['IP']
        print 'Timestamp ' ,row['Timestamp']
        print 'Request_Type ' ,row['Request_Type']
        print 'Requested_URL ' ,row['Requested_URL']
        print 'Base_URL ' ,row['Base_URL']
        print 'status ' ,row['status']
        print 'Referer ' ,row['Referer']
        print 'Query ' ,row['Query']
        print 'Agent ' ,row['Agent']
        print 'Bytes_Sent ' ,row['Bytes_Sent']
    else:
        print '+++++++++++++++++++++++++++++++'
        print 'Timestamp ' ,row['Timestamp']
        print 'Request_Type ' ,row['Request_Type']
        print 'Requested_URL ' ,row['Requested_URL']
        print 'Base_URL ' ,row['Base_URL']
        print 'status ' ,row['status']
        print 'Referer ' ,row['Referer']
        print 'Query ' ,row['Query']
        print 'Bytes_Sent ' ,row['Bytes_Sent']
    prev=session
'''


f.close()