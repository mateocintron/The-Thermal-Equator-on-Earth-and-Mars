import rasterio					# for reading geotiff (*.tif) file#
import numpy as np
from matplotlib import (pyplot, cm)	 # for plotting image data
import scipy.ndimage

# read tif file
dataset = rasterio.open('marsdata.tif')

# record number of data points along x (nrows) and y (ncols) in each datatable stored in dataset
nrows = dataset.height
ncols = dataset.width

# record coordinate bounds of dataset (in degrees)
bounds = dataset.bounds
xmin = bounds.left
xmax = bounds.right
ymin = bounds.bottom
ymax = bounds.top

xmin = 0
xmax = 360
ymin = -90
ymax = 90

xrng = xmax - xmin
yrng = ymax - ymin

xstep = xrng / (ncols - 1)
ystep = yrng / (nrows - 1)

tmin_C=dataset.offsets[0]
tstep_C=dataset.scales[0]

# define midpoints of dataset in both x and y directions (// is divide for integers)
nrowmid = nrows // 2
ncolmid = ncols // 2

# get example xy coordinate location (in degrees) at center of 2-dimensional dataset 
xylocation = dataset.xy(nrowmid, ncolmid)

# record number of datatables in dataset
ndatatables = dataset.indexes
ndatatables = ndatatables[0]

# read first datatable
datatable0 = dataset.read(1)
datatable0 = np.flipud(datatable0)

x = np.linspace(xmin, xmax, ncols)

pyplot.rcParams['figure.dpi'] = 2000

datatable1 = scipy.ndimage.gaussian_filter(datatable0, sigma=0)



datatable2 = scipy.ndimage.gaussian_filter(datatable0, sigma=0)
datatable2slice = slice(2000, 3600)
datatable2[datatable2slice, :] -= 1000

degrees_latitude_max = ymax - ystep * np.argmax(datatable2,axis=0)
# pyplot.plot(x, degrees_latitude_max, label='Max Latitude Top (°)', linewidth=0.3, color='b')

datatable3 = np.flipud(datatable2)
degrees_latitude_max2 = ymin + ystep * np.argmax(datatable3,axis=0)
# pyplot.plot(x, degrees_latitude_max2, label='Max Latitude Bottom (°)', linewidth=0.3, color='g')

degrees_latitude_max_top_average = (degrees_latitude_max + degrees_latitude_max2) / 2
pyplot.plot(x, degrees_latitude_max_top_average, label='Max Latitude Bottom (°)', linewidth=0.2, color='r')


tmp_C_max = tmin_C + tstep_C * np.amax(datatable2,axis=0)
width_of_mars = abs(degrees_latitude_max - degrees_latitude_max2)






datatable4 = scipy.ndimage.gaussian_filter(datatable0, sigma=0)
datatable4slice = slice(0, 2000)
datatable4[datatable4slice, :] -= 1000

degrees_latitude_max3 = ymax - ystep * np.argmax(datatable4,axis=0)
# pyplot.plot(x, degrees_latitude_max3, label='Max Latitude Top (°)', linewidth=0.3, color='b')

datatable5 = np.flipud(datatable4)
degrees_latitude_max4 = ymin + ystep * np.argmax(datatable5,axis=0)
# pyplot.plot(x, degrees_latitude_max4, label='Max Latitude Bottom (°)', linewidth=0.3, color='g')

degrees_latitude_max_bottom_average = (degrees_latitude_max3 + degrees_latitude_max4) / 2
pyplot.plot(x, degrees_latitude_max_bottom_average, label='Max Latitude Bottom (°)', linewidth=0.2, color='r')


tmp_C_max2 = tmin_C + tstep_C * np.amax(datatable4,axis=0)
width_of_mars2 = abs(degrees_latitude_max3 - degrees_latitude_max4)



cmap = cm.get_cmap
pyplot.imshow(datatable0, cmap='white', extent=[xmin,xmax,ymin,ymax])
pyplot.show()








