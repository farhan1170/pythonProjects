import csv
fp=open('/home/f/Desktop/xab_d.csv','w')
fn=open('/home/f/Desktop/samp_test_d.csv','w')
fp.write("itemID")
fp.write(',')
fp.write("sentiment")
fp.write(',')
fp.write("SentimentSource")
fp.write(',')
fp.write("SentimentText")
fp.write('\n')

fn.write("itemID")
fn.write(',')
fn.write("sentiment")
fn.write(',')
fn.write("SentimentSource")
fn.write(',')
fn.write("SentimentText")
fn.write('\n')


with open('/home/f/Desktop/xab.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     count=0
     for row in reader:
         itemID=row['ItemID']
         sentiment=row['Sentiment']
         SentimentSource=row['SentimentSource']
         SentimentText="\""+row['SentimentText']+"\""
         fp.write(itemID)
         fp.write(',')
         fp.write(sentiment)
         fp.write(',')
         fp.write(SentimentSource)
         fp.write(',')
         fp.write(SentimentText)
         fp.write('\n')

fp.close()

with open('/home/f/Desktop/samp_test.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     count=0
     for row in reader:
         itemID=row['ItemID']
         sentiment=row['Sentiment']
         SentimentSource=row['SentimentSource']
         SentimentText="\""+row['SentimentText']+"\""
         fn.write(itemID)
         fn.write(',')
         fn.write(sentiment)
         fn.write(',')
         fn.write(SentimentSource)
         fn.write(',')
         fn.write(SentimentText)
         fn.write('\n')

fp.close()




