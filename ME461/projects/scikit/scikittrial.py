import skimage as ski
import numpy as np
import matplotlib.pyplot as plt

camera = ski.data.camera()
print(type(camera))
print(camera.shape)
print(camera.size)
print(camera.min(), camera.max())
print(camera.mean())
print(camera[10, 20])

mask = camera < 87 #masking of true false

values, bins = np.histogram(camera, bins=np.arange(0, 256))
# plt.plot(bins[:-1], values)
# plt.show()
#Threshholding
thresholdedlow = camera > 100
thresholdedhigh = camera < 187
#and operation high and low threshold
thresholded = thresholdedlow & thresholdedhigh


#display image
ski.io.imshow(thresholded)
ski.io.show()
