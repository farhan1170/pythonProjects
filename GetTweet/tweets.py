import csv
__author__ = 'f'
count=0
def read_file (file_name, mode):
	file_content = open(file_name,mode).read().lower().replace("\n"," ")
	return file_content.split()
path='/home/f/socialstore/Autoscale'

movie_words = list(set(read_file(path+"/Datasets/Movies/movieMfw.txt","r")))
music_words = list(set(read_file(path+"/Datasets/Music/musicMfw.txt","r")))
game_words = list(set(read_file(path+"/Datasets/Games/gamesMfw.txt","r")))

write_train=open('/home/f/Desktop/train.txt','w')
write_test=open('/home/f/Desktop/test.txt','w')
with open('/home/f/Downloads/twitter_sentiment/training.1600000.processed.noemoticon.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if count<=1000000:
            write_train.write(row['tweet'])
            write_train.write('\n')
        else:
            write_test.write(row['tweet'])
            write_test.write('\n')
        count+=1
        if(count%10000==0):
            print count

write_train.close()
write_test.close()