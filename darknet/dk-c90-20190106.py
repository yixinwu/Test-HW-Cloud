from ctypes import *
import math
import random
import os
import cv2
import numpy as np
    
if __name__ == "__main__":
    for (root, dirs, files) in os.walk('/home/test-ml/py3venv/tf-prj/dataset/MAPIR/tst-20190106'):
        if files:
            for f in files:
                if 'intensity' in f:
                    path = os.path.join(root, f) 
                    img = cv2.imread(path)
                    imginfo = img.shape
                    height = imginfo[0]
                    width = imginfo[1]
                    if width > height :
                       img_c90 = np.rot90(img)
                       cv2.imwrite(path, img_c90)
                    print(f,' ', width, '  ', height)
   

