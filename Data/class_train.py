moviewords=[]
with open('/home/f/socialstore/Autoscale/Datasets/Movies/movieMfw.txt')as f:
    moviewords=f.readlines()

id=1
fw=open('/home/f/Desktop/class_terain.tsv','w')
fw.write('id	sentiment	review')
fw.write('\n')
for word in moviewords:
    fw.write('"'+str(id)+'"')
    fw.write('\t')
    fw.write('movie')
    fw.write('\t')
    fw.write('"'+word[:-1]+'"')
    fw.write('\n')
    id+=1

print '==============================================================='

musicwords=[]
with open('/home/f/socialstore/Autoscale/Datasets/Music/musicMfw.txt','r')as f:
    musicwords=f.readlines()


for word in musicwords:
    fw.write('"'+str(id)+'"')
    fw.write('\t')
    fw.write('music')
    fw.write('\t')
    fw.write('"'+word[:-1]+'"')
    fw.write('\n')
    id+=1

print '==============================================================='

gamewords=[]
with open('/home/f/socialstore/Autoscale/Datasets/Games/gamesMfw.txt','r')as f:
    gamewords=f.readlines()


for word in gamewords:
    fw.write('"'+str(id)+'"')
    fw.write('\t')
    fw.write('game')
    fw.write('\t')
    fw.write('"'+word[:-1]+'"')
    fw.write('\n')
    id+=1
fw.close()