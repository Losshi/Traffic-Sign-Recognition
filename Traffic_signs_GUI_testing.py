import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
import tensorflow
from tensorflow import keras
model1 = keras.models.load_model('Model/trafficmodel.hdf5')
model2 = keras.models.load_model('Model/traffic_cnnmodel.hdf5')
classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)', 
            3:'Speed limit (50km/h)', 
            4:'Speed limit (60km/h)', 
            5:'Speed limit (70km/h)', 
            6:'Speed limit (80km/h)', 
            7:'End of speed limit (80km/h)', 
            8:'Speed limit (100km/h)', 
            9:'Speed limit (120km/h)', 
            10:'No passing', 
            11:'No passing for vehicles over 3.5 metric tons', 
            12:'Right-of-way at next intersection', 
            13:'Priority road', 
            14:'Yield', 
            15:'Stop', 
            16:'No vehicles', 
            17:'Vehicles over 3.5 metric tons prohibited', 
            18:'No entry', 
            19:'General caution', 
            20:'Dangerous curve to the left', 
            21:'Dangerous curve to the right', 
            22:'Double curve', 
            23:'Bumpy road', 
            24:'Slippery road', 
            25:'Road narrows on the right', 
            26:'Road work', 
            27:'Traffic signals', 
            28:'Pedestrians', 
            29:'Children crossing', 
            30:'Bicycles crossing', 
            31:'Beware of ice/snow',
            32:'Wild animals crossing', 
            33:'End of all speed and passing limits', 
            34:'Turn right ahead', 
            35:'Turn left ahead', 
            36:'Ahead only', 
            37:'Go straight or right', 
            38:'Go straight or left', 
            39:'Keep right', 
            40:'Keep left', 
            41:'Roundabout mandatory', 
            42:'End of no passing', 
            43:'End of no passing by vehicles over 3.5 metric tons' }
top=tk.Tk()
top.geometry('1920x1080')
top.title('Traffic Sign Recognition')
top.configure(background='#FFDDF4')
label=Label(top,background='#FFDDF4', font=('arial',20,'bold'))
sign_image = Label(top)
def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((32,32))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred1 = model1.predict_classes([image])[0]
    pred2 = model2.predict_classes([image])[0]
    print(pred1," ",pred2)
    if pred1==pred2:
        sign = "Damn sure! This traffic sign says "+classes[pred1+1]
        label.configure(foreground='#1B4D3E', text=sign) 
    else:
        sign = "Not so sure! I think it says "+classes[pred1+1]
        label.configure(foreground='#FF4500', text=sign) 
    print(sign)
    
def show_classify_button(file_path):
    classify_b=Button(top,text="Recognize the Traffic Sign",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#800080', foreground='white',font=('arial',13,'bold'))
    classify_b.place(relx=0.41,rely=0.34)
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded=uploaded.resize((180,180))
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#800080', foreground='white',font=('arial',13,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="TRAFFIC SIGN RECOGNITION",pady=20, font=('arial',30,'bold'))
heading.configure(background='#FFDDF4',foreground='#800080')
heading.pack()
top.mainloop()
