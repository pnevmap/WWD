from skimage import io, measure
from skimage.exposure import histogram
import skimage.color as color
import matplotlib.pyplot as plt
import numpy as np

shapes_image = io.imread('shapes.jpg')

grayscale_image = color.rgb2gray(shapes_image)
red_channel = shapes_image[:, :, 0]

# io.imshow(shapes_image)
# io.show()
# io.imshow(grayscale_image)
# io.show()
# io.imshow(red_channel)
# io.show()

binary_image = grayscale_image >.85

label_image = measure.label(binary_image, background=1, connectivity=2)
# io.imshow(label_image)
regions = measure.regionprops(label_image)

def histogram_median(hist, hist_centers):
    data = []
    for center, frequency in zip(hist_centers, hist):
        data.extend([center] * frequency)
    return np.median(data)


def histogram_by_shape(region):
    bbox = region.bbox
    hist, hist_centers = histogram(red_channel[bbox[0]:bbox[2], bbox[1]:bbox[3]])
    median = histogram_median(hist, hist_centers)

    fig, axes = plt.subplots(1, 2, figsize=(8, 3))
    axes[0].imshow(shapes_image[bbox[0]:bbox[2], bbox[1]:bbox[3]], cmap=plt.cm.gray)
    axes[0].set_axis_off()
    axes[1].plot(hist_centers, hist, lw=2)
    axes[1].set_title('histogram of red values')
    axes[1].axvline(x=100, color='r', linestyle='--')
    axes[1].axvline(x=median, color='g', linestyle='--', label=f'Median = {median}')
    plt.show()
    if median < 100:
        high_requency_image[bbox[0]:bbox[2], bbox[1]:bbox[3]] = [255]

def filter_by_density(region):
    print(region.area_bbox, region.area, region.area_convex, region.area_bbox/region.area)



high_requency_image = shapes_image.copy()
for region in regions:
    filter_by_density(region)

io.imshow(high_requency_image, cmap=plt.cm.gray)
io.show()

