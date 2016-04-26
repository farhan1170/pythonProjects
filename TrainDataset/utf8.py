import os
import sys
import shutil
__author__ = 'f'
def convert():
   encodings = ('windows-1253', 'iso-8859-7', 'macgreek')
   try:
        ftrain = open("/home/f/Desktop/train.txt", 'r').read()
   except Exception:
        sys.exit(1)
   for enc in encodings:
        try:
            data = ftrain.decode(enc)
            break
        except Exception:
            if enc == encodings[-1]:
                sys.exit(1)
            continue

   ftrainwrite = open('/home/f/Desktop/train_utf8.txt', 'w')
   try:
    ftrainwrite.write(data.encode('utf-8'))
   except Exception,e:
    print e
   finally:
        ftrainwrite.close()
   return "/home/f/Desktop/train_utf8.txt"