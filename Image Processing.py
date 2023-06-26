from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from PIL import Image, ImageTk
import cv2 as cv
import numpy as np

class GUI (Frame):
    img = None
    img_is_found = False
    def __init__(self, master=None):
        Frame.__init__(self, master)
        
        self.label1 = Label(width=200,height=200)
        self.label = Label(width=300,height=300)
        self.label2 = Label(text="Original image", font=('Times',15))
        self.label3 = Label(text="Result Image", font=('Times',15))
        self.label4 = Label(text="Image Processing", font=('Times',24))
        self.file = Button(width=13, text="Upload image", command=self.choose)
        self.blur1 =Button(width=13, text='Blur', command=self.blur)
        self.negative_trans = Button(width=13, text='Negative Trans', command=self.negativeTrans)
        self.flip_image_verti = Button(width=13, text='flip vertically', command=self.flip_verti)
        self.flip_image_hori = Button(width=13, text='flip horizontally', command=self.flip_hori)
        self.rotate_image = Button(width=13, text='rotate', command=self.rotate)
        self.scaling_image = Button(width=13, text='scaling', command=self.scaling)
        self.sharp_image = Button(width=13, text='sharpen', command=self.sharpen)
        self.grayscale_image = Button(width=13, text='grayscale', command=self.grayscale)
        self.denoise_image = Button(width=13, text='denoise', command=self.denoise)
        self.reset_image = Button(width=13, text='reset', command=self.reset)
        
    
        
        self.place()
        self.label1.place(x=500, y=150)
        self.label2.place(x=540, y=370)
        self.label3.place(x=850, y=370)
        self.label4.place(x=640, y=30)
        self.label.place(x=750, y= 100)
        self.file.place(x = 140, y = 140)
        self.blur1.place(x = 140, y = 180)    
        self.negative_trans.place(x = 140, y = 220)    
        self.flip_image_verti.place(x = 140, y = 260)
        self.flip_image_hori.place(x = 140, y = 300)
        self.rotate_image.place(x = 140, y = 340)
        self.scaling_image.place(x = 1300, y = 140)
        self.sharp_image.place(x = 1300, y = 180)
        self.grayscale_image.place(x = 1300, y = 220)
        self.denoise_image.place(x = 1300, y = 260)
        self.reset_image.place(x = 1300, y = 300)
       


    def choose(self):
        f_types = [('Jpeg Files', '*.jpeg'),('PNG Files','*.png'),('Jpg Files', '*.jpg')]
        ifile = filedialog. askopenfile(parent=self, filetypes=f_types, title='choose file',mode='rb')
        if ifile:
            self.path = Image.open(ifile)
            self.path = self.path.resize((200,200))
            self.image2 = ImageTk.PhotoImage(self.path)
            self.label1.configure(image=self.image2)
            self.label.configure(image=self.image2)
            self.label1.image = self.image2
            self.label.image = self.image2
            self.img = np.array(self.path)
            self.img = self.img
            self.img_is_found = True
    
    def blur(self):
        if self.img_is_found:
            img_after = blur_img(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
   
    def negativeTrans(self):
        if self.img_is_found:
            img_after = negative_trans(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
    
    def flip_verti(self):
        if self.img_is_found:
            img_after = flip_verti(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
    
    def flip_hori(self):
        if self.img_is_found:
            img_after = flip_hori(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
    
    def rotate(self):
        if self.img_is_found:
            img_after = rotate_trans(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
   
    def scaling(self):
        if self.img_is_found:
            img_after = scaling_trans(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
    
    
    def sharpen(self):
        if self.img_is_found:
            img_after = sharpen_image(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
    
    def grayscale(self):
        if self.img_is_found:
            img_after = grayscale_image(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
    
    def denoise(self):
        if self.img_is_found:
            img_after = denoise_image(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
    
    def reset(self):
        if self.img_is_found:
            img_after = reset_img(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after

    def save1(self):
        if self.img_is_found:
             a = Image.open(self.img)
             c = Image.fromarray(a)
             d = ImageTk.PhotoImage(c)
             f_types = [('Jpeg Files', '*.jpeg'),('PNG Files','*.png'),('Jpg Files', '*.jpg')] 
             filename = filedialog.asksaveasfile(mode = 'w',filetypes = f_types, defaultextension = f_types)
             if not filename:
                return
             c.save(filename)
             

def reset_img(img):
    
    reset = img

    return reset

def negative_trans(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    colored_negative = abs(255-img)
  
        
    return colored_negative
    

def blur_img(img):  
    kernelSizes = [ (15, 15)]
    for (kX, kY) in kernelSizes:
     blurred = cv.blur(img, (kX, kY))
     return blurred       

def flip_verti(img):
    img = cv.flip(img,0)
    
    return img

def flip_hori(img):
    img = cv.flip(img,1)
    
    return img

def rotate_trans(img):
    
    rows, cols, _ = img.shape

    D = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
    dsa = cv.warpAffine(img,D,(cols,rows))
    return dsa

def scaling_trans(img):
    res = cv.resize (img,None, fx = 2, fy = 1, interpolation=cv. INTER_CUBIC)
    return res

def sharpen_image(img):
    kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
    image_sharp = cv.filter2D(src=img, ddepth=-1, kernel=kernel)
    return image_sharp

def grayscale_image(img):
    grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return grayscale

def denoise_image(img):
    dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    return dst

def save_file(img):
    img = Image.t(img, cv.COLOR_BGR2RGB)
    
    return img

root = Tk() 
root.title("Image Processing")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+8" % (w, h))


gui = GUI(root)
gui.mainloop() 