import os
import pydicom



from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img

from PIL import Image

import numpy as np

import threading
import argparse

import tempfile
from pathlib import Path
import glob



#def image_properties(image_path):
#    img = Image.open(image_path)
#    img_name = img.filename
#    img_format = img.format
#    img_mode = img.mode
#    img_size = img.size
#    img_palette = img.palette
#    img_info = img.info
#    img.close()

#    result = {"name" : img_name, "format" : img_format, "mode" : img_mode, "size" : img_size,"palette" : img_palette, "info" : img_info}
#    return result



def get_names(image_path):
    names = []
    for root, dirnames, filenames in os.walk(image_path):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext in ['.dcm','.png']:
                names.append(filename)
    
    return names

def clear_tmp():
    # directory containing the files to be deleted
    dir_path = "./tmp"
    # pattern for file names to be deleted
    file_pattern = "*.dcm"
    file_pattern1 = "*.png"
    # get a list of file paths using the glob module
    file_paths = glob.glob(os.path.join(dir_path, file_pattern))
    file_paths1 = glob.glob(os.path.join(dir_path, file_pattern1))
    # loop over each file path and delete the file
    for file_path in file_paths:
        os.remove(file_path)
    for file_path in file_paths1:
        os.remove(file_path)


def convert_dcm_jpg(image_path,name):
    final_images = []
    im = pydicom.dcmread(image_path + "/" + name)
    
    #Iterate by array
    i = 0
    a = len(im.pixel_array)
    for i in range(0,a):
        im_item = im.pixel_array[i].astype(float)

        rescaled_image = (np.maximum(im_item,0)/im_item.max())*255 # float pixels
        final_image = np.uint8(rescaled_image) # integers pixels
        #final_image = Image.fromarray((x * 255).astype(np.uint8))
        final_image =  Image.fromarray(final_image)      
        final_images.append(final_image)
        i +=1

    return final_images

def dcm_to_png():
    names = get_names('Database')
    for name in names:
        image = convert_dcm_jpg(name)
        image.save(name+'.png')
        print(f"++++++++++++++++++!!!!!!{image}")
     
    








 