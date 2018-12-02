# python3 make_id_finish6.py  -m 'w' -t 'ID.txt'
## -*- coding: utf-8 -*-


try:
    import cPickle as pickle
except ImportError:
    import pickle

import argparse

import numpy as np
import copy
import time
import cv2
import imutils
import os
import fnmatch
import os
from fnmatch import fnmatch






dictionary=[]
out=[]


# read from file
root = '/home/ivliev/TF/baseno'
pattern = "*.jpg"

path, subdirs, files = os.walk(root).next()
out=np.zeros(len(subdirs))

i=0

for path, subdirs, files in os.walk(root):
    k=0
    for name in subdirs:
		#if fnmatch(name, pattern):
		#print name #(os.path.join(path, name))
        for path2, subdirs2, files2 in os.walk(os.path.join(path, name)):
            for name2 in files2:
                #if fnmatch(name2, pattern):
                dir_name2=(os.path.join(path2, name2))
                #read image
                #image = cv2.imread('barcode_01.jpg')
                image = cv2.imread(dir_name2)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                ret,th1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
                th3_base = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                            cv2.THRESH_BINARY,11,7)

                im2, cnts, hierarchy  = cv2.findContours(th1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


                c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
                x,y,w,h = cv2.boundingRect(c)
                get= gray[y:y+h, x:x+w]
                get_resize=cv2.resize(get, (20,20))
                get_array=np.array(get_resize)

                print dir_name2
                dictionary.append([[],[],[]])
                out=np.zeros(len(subdirs))
                out[k]=1
                dictionary[i][0]=name
                dictionary[i][1]=get_array #np.array((dir_name2))
                dictionary[i][2]=out
                # print dictionary[i][1].size 
                i+=1

        k+=1



#with open("dictionary.pkl","wb") as f:
f=open("dictionary.pkl","wb")
for i in range(len(dictionary)):
	pickle.dump(dictionary[i], f)
f.close()




d = open("dictionary.txt", "w")
for i in range(len(dictionary)):
	s=str(dictionary[i])
	d.write(s+ '\n')
	#d.write('\n')
d.close()
