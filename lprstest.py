# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from skimage.io import imread 
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import resize
from sklearn.cross_decomposition import cca
#import localization
car_image = imread("car1.jpg", as_grey=True)
print(car_image.shape)
gray_car_image = car_image *255
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(gray_car_image, cmap = 'gray')
threshold = threshold_otsu(gray_car_image)
binary_car_image = gray_car_image > threshold 
ax2.imshow(binary_car_image, cmap = 'gray')
plt.show()



from skimage import measure
from skimage.measure import regionprops 
import matplotlib.patches as ptch

label_image = measure.label(binary_car_image)
fig, (ax1) = plt.subplots(1)
ax1.imshow(gray_car_image, cmap='gray')

for region in regionprops(label_image):
    if region.area < 50:
        continue
    minRow, minCol,maxRow, maxCol = region.bbox
    rectBorder = ptch.Rectangle((minCol,minRow),maxCol-minCol, maxRow-minRow,edgecolor='red',linewidth=2, fill=False)
    ax1.add_patch(rectBorder)
plt.show()
plate_dimensions = (0.08*label_image.shape[0], 0.2*label_image.shape[0], 0.15*label_image.shape[1], 0.4*label_image.shape[1])
min_height,max_height, min_width, max_width = plate_dimensions
plate_objects_cordinates = []
plate_like_objects = []
fig,(ax1)=plt.subplots(1)
ax1.imshow(gray_car_image, cmap='gray')
for region in regionprops(label_image):
    if region.area<50:
        continue
    min_row,min_col,max_row,max_col = region.bbox
    region_height = max_row-min_row
    region_width =  max_col-min_col
    if region_height>=min_height and region_height <= max_height and region_width>=min_width and region_width<=max_width and region_width> region_height:
        plate_like_objects.append(binary_car_image[min_row:max_row, min_col:max_col])
        plate_objects_cordinates.append((min_row,min_col,max_row,max_col))
        rectBorder = ptch.Rectangle((min_col, min_row),max_col-min_col, max_row-min_row, edgecolor='red', linewidth=2, fill=False)
        ax1.add_patch(rectBorder)
        
plt.show()

number_plate = np.invert(caa.plate_like_objects[2])

labelled_plate = measure.label(number_plate)

fig, ax1= plt.subplots(1)
ax1.imshow(number_plate, camp='gray')
character_dimensions = (0.35 * number_plate.shape[0], 0.60*number_plate.shape[0],0.05*number_plate.shape[1],0.15*number_plate.shape[1])
min_height, max_height, min_width, max_width = character_dimensions

characters = []
counters=0
column_list = []
for regions in regionprops(labelled_plate):
    
    y0,x0,y1,x1 = region.bbox
    region_height = y1-y0
    region_width = x1-x0
    
    if region_height > min_height and region_height< max_height and region_width>min_width and region_width<max_width:
        roi = number_plate[y0:y1,x0:x1]
        
        rect_border = ptch.Rectangle((x0,y0),x1-x0,y1-y0,edgecolor='red',linewidth=2,fill=False)
        ax1.add_patch(rect_border)
        
        resized_char = resize(roi,(20,20))
        characters.append(resized_char)
        column_list.append(x0)
        
plt.show() 




