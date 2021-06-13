import numpy as np
import cv2
import os
from random import shuffle

directory="dataset"
subfolder="Train"
parent_folder=os.path.join(directory,subfolder)
folders = os.listdir(parent_folder)
dataset=[]

for folder in folders:
    folder_path=os.path.join(parent_folder,folder)
    target=int(folder)
    images=os.listdir(folder_path)
    for img in images:
        img_path=os.path.join(folder_path,img)
        try:
            image=cv2.imread(img_path)
            resized_image=cv2.resize(image,(32,32))
            cv2.imshow("Traffic Sign",resized_image)
            cv2.waitKey(1)
            dataset.append([resized_image,target])
        except:
            continue

dataset=np.array(dataset)
shuffle(dataset)
np.save("dataset/Traffic_train_dataset.npy",dataset)
    
