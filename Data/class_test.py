moviewords=[]
with open('/home/f/Desktop/reviews/reviewsmovies.txt','r')as f:
    moviewords=f.readlines()

count=1
id=1

fw=open('/home/f/Desktop/class_test.tsv','w')
fw.write('id\treview')
fw.write('\n')

for word in moviewords:
    data='"'+word[:-1]+'"'
    if data!='""':
        fw.write('"'+str(id)+'"')
        fw.write('\t')


        fw.write(data)
        print word[:-1]
        fw.write('\n')
        id+=1
        count+=1

print 'mov==============================================================='

musicwords=[]
with open('/home/f/Desktop/reviews/reviewsmusic.txt','r')as f:
    musicwords=f.readlines()


for word in musicwords:
    data='"'+word[:-1]+'"'
    if data!='""':
        fw.write('"'+str(id)+'"')
        fw.write('\t')


        fw.write(data)
        print word[:-1]
        fw.write('\n')
        id+=1
        count+=1

print 'mus==============================================================='
count=1
gamewords=[]
with open('/home/f/Desktop/reviews/GameReviews.txt','r')as f:
    gamewords=f.readlines()

for word in gamewords:
    data='"'+word[:-1]+'"'
    if data!='""':
        fw.write('"'+str(id)+'"')
        fw.write('\t')


        fw.write(data)
        print word[:-1]
        fw.write('\n')
        id+=1
        count+=1

fw.close()
