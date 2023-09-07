import pygame as pg
import numpy as np
from PIL import Image, ImageOps
from math import sin,cos,pi

pic = Image.open("eye.jpg")
pic_width,pic_height=pic.size

def resize_to_grayscale_numpy(image, target_width, target_height):
    resized_image = image.resize((target_width, target_height))
    resized_image=resized_image.rotate(90)
    grayscale_image = resized_image.convert('L')
    image_array = np.array(grayscale_image)
    return image_array

width,height=600,600
window = pg.display.set_mode((width,height))

def run():
    pg.display.update()
    # window.fill("BLACK")
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            return False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_ESCAPE:
                pg.quit()
                return False
    return True

r=(width/2)*0.98
points=100
da=(pi*2)/points

def liner(start,end):
    sp=place(start,r)
    ep=place(end,r)
    pg.draw.line(window,"BLUE", sp,ep)

def place(a,r):return r*cos(a*da)+(width/2),r*sin(a*da)+(height/2)
picar = resize_to_grayscale_numpy(pic, 600,600)

pixel=pg.PixelArray(window)

for i in range(width):
        for j in range(height):
            pixel[i][j]=tuple(np.ones(3)*picar[i][j])

while run():
    pg.draw.circle(window,"GREEN", (width/2,height/2), r, 1)
    for i in range(points):pg.draw.circle(window,"WHITE", place(i,r), 3)

    liner(0,30)




