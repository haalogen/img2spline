#-*- coding: utf-8 -*-
"""Makes an interpolation (spline) from raster image (JPG, PNG)"""

import sys
import time
from PIL import Image
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.interpolate import RectBivariateSpline, griddata

def main():
    
    if len(sys.argv) != 2:
        print """
Usage: python img2spline.py [path_to_img] \n"""
        sys.exit(-1)
        
    else:
        path_to_img = sys.argv[1]
    
    
    img = Image.open(path_to_img).convert('L') # RGB -> [0..255]
    print "Image was opened and converted to grayscale."
    img.show()
    
    width, height = img.size
    
    data = np.array(list(img.getdata()), dtype=int)
    data = data.reshape((height, width))
    print "Data was extracted."
    
#    Start plotting original surface of image
    fig = plt.figure()
#    ax = fig.add_subplot(111, projection='3d')
    ax = fig.add_subplot(111)
    ax.invert_yaxis()
    x = range(0, width)
    y = range(0, height)
#    rev_y = range(height-1, -1, -1) # reverse y
    
    X, Y = np.meshgrid(x, y)
    print Y
    
    
    r_stride = 1 + width / 20 
    c_stride = 1 + height / 20
#    ax.plot_surface(X, Y, data, rstride=r_stride, cstride=c_stride)
    mappable = ax.pcolor(X, Y, data)
    plt.colorbar(mappable)
    ax.set_title("Original grayscale image")
    ax.set_xlabel('Width (px)')
    ax.set_ylabel('Height (px)')
    plt.draw()
#    Finish plotting original surface of image
    
    
#    2D Interpolation here
    spline = RectBivariateSpline(x, y, data)
    
    print spline.get_coeffs()
    
    
    
    
    plt.show()





if __name__ == '__main__':
    main()

