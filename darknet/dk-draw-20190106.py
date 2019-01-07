from ctypes import *
import math
import random
import os
import cv2
import numpy as np


def find_truth_file_path(filename):
    fn=filename.replace('intensity.png','labels.txt')
    fn=fn.rstrip()
    for (root, dirs, files) in os.walk('/home/test-ml/py3venv/tf-prj/dataset/MAPIR/tst-20190106'):
        if files:
            for f in files:
                if f == fn: r = os.path.join(root, f)
    return r


if __name__ == "__main__":
   # main item:
   pic_dir = '/home/test-ml/py3venv/tf-prj/dataset/MAPIR/tst-20190106'
   refr = 'refrigerator'
   sink = 'sink'
   stove = 'stove'
   bed = 'bed'
   chair = 'chair'
   toilet = 'toilet' 
   diningtable = 'table'   

   fh = open('./res-0106')
   # find the filepath
   for line in fh.readlines():
       if 'IMG_' in line:
           filename = line.rstrip()
           for (root, dirs, files) in os.walk(pic_dir):
               if files:
                   for f in files:
                       if f == filename: 
                           filepath = os.path.join(root, f) 
                           print(filepath)
                           img=cv2.imread(filepath)
       # find the location
       if '[(' in line: 
           strlist = line.split(',')
           t = 0
           for value in strlist:
               if (refr in value)or(sink in value)or(bed in value)or(chair in value)or(toilet in value)or(diningtable in value): 
                   item_name = value[4:-1] +' ' + strlist[t+1][0:5] 
                   #item_value = strlist[t+1][0:5]
                   item_location_x = int(float(strlist[t+2][2:7]))
                   item_location_y = int(float(strlist[t+3][0:6]))
                   item_location_w = int(float(strlist[t+4][0:6]))
                   item_location_h = int(float(strlist[t+5][0:6]))
                   t = t+6   
                   cv2.circle(img,(item_location_x, item_location_y), 3, (0,0,255), 3)
                   cv2.putText(img, item_name, (item_location_x,item_location_y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                   tagetfile = filepath + 'new.jpg'   
                   cv2.imwrite(tagetfile, img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
   

   fh.close()


