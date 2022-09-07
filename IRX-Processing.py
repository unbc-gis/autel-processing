# Directory to search for images
dir = 'Change me'

from PIL import Image
import piexif
import numpy as np
import os


for dir_path, dir_names, file_names in os.walk(dir):
    print(dir_path)
    for file in file_names:
        # Process files only with extension .TIFF
        if file.endswith(".TIFF"):
            path = os.path.join(dir_path, file)
            print(path)
            
            # .TIFF files do not have GPS coords retreive them from MAX .jpg file
            jpg_path = path[:-13] + "MAX_" + path[-9:-4] + "JPG"
            jpg_img = Image.open(jpg_path)
            
            im = Image.open(os.path.join(dir_path, file))
            imarray = np.array(im) # Convert image to numpy array
            
            # TODO this currently makes assumption all temperatures are above 0 degrees C
            celsius = imarray - 2722 # Convert image data from Kelven to Celcius 
            c_im = Image.fromarray(celsius.astype(np.uint16) * 64) # Expand data to fill uint16
            c_im.save(os.path.join(dir_path, file)[:-4] + 'tif', exif=jpg_img._getexif()) # Save modified tiff with jpg's exif
