from tkinter import *
from PIL import Image
from Score_Format import *

#  Formats Images to proper size
center_image = Image.open(r'D:\\MostCommonScore\\Images\\football.png')
cenimg_width, cenimg_height = center_image.size
newW = 200
newH = 200
new_center_image = center_image.resize((newW, newH), Image.LANCZOS)
new_center_image.save("center_image.png")

