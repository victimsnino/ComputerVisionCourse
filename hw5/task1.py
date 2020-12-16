import math
import numpy as np
from PIL import Image
from PIL.ExifTags import TAGS

img = Image.open('GOPR01170000.jpg')
exif_as_dict = {TAGS.get(k) : v for (k,v) in img._getexif().items()}

cx = math.floor(exif_as_dict['ExifImageWidth']/2)
cy = math.floor(exif_as_dict['ExifImageHeight']/2)

dpi_x = exif_as_dict['XResolution']
dpi_y = exif_as_dict['XResolution']

dpi_x_to_mm = dpi_x * 25.4
dpi_y_to_mm = dpi_y * 25.4

focal = 24 # hardcode
focal_x = focal*dpi_x_to_mm
focal_y = focal*dpi_y_to_mm

print(np.matrix([[focal_x, 0, cx], [0, focal_y, cy], [0,0,1]]))