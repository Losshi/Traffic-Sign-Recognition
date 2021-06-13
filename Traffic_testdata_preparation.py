import numpy as np
import pandas as pd
import cv2
import os
from random import shuffle

directory="dataset"
subfolder="Test"
parent_folder=os.path.join(directory,subfolder)
dataset=[]

df=pd.read_csv("dataset/Test.csv")
target=df.iloc[:,6]
c=0

images=os.listdir(parent_folder)
for img in images:
    img_path=os.path.join(parent_folder,img)
    try:
        image=cv2.imread(img_path)
        resized_image=cv2.resize(image,(32,32))
        cv2.imshow("Traffic Sign",resized_image)
        cv2.waitKey(1)
        dataset.append([resized_image,target[c]])
        c+=1
    except:
        continue

dataset=np.array(dataset)
shuffle(dataset)
np.save("dataset/Traffic_test_dataset.npy",dataset)

