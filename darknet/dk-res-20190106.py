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


def read_truth_items_num(filepath):
    fh1 = open(filepath)
    for line1 in fh1.readlines():
        if (line1.startswith('#') == 0): 
             item_num = 1
             fh1.close()
             return int(line1.rstrip())
    return 0


def read_truth_items(filepath):
    return 0 


def read_res_item():
    return 0

if __name__ == "__main__":
   fh = open('./res-0106')
   for line in fh.readlines():
       if 'intensity' in line:
           r = find_truth_file_path(line)   
           r2 = read_truth_items_num(r)
           print(r.rstrip(), r2)
       if '[(b' in line: 
           strlist = line.split(',')
           for value in strlist:
               if '(b' in value : print(value)
   fh.close()







#for (root, dirs, files) in os.walk('/home/test-ml/py3venv/tf-prj/dataset/MAPIR/tst-20190106'):
        
     #if files:
     #       for f in files:
     #           if 'intensity' in f:
     #               path = os.path.join(root, f) 
     #               img = cv2.imread(path)
     #               imginfo = img.shape
   

