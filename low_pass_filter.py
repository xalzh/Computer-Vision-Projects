from PIL import Image
import numpy as np
from IPython.display import display


def LPF(image, size=3, rgb=True, **kwargs):
    im = Image.open(image)
    im = np.array(im)
    im_filter = np.full((size, size), 1 / (size ** 2))
    y_size = im.shape[0]
    x_size = im.shape[1]
    color_size = im.shape[2]
    tm = np.pad(im, [(int(size / 2), int(size / 2)), (int(size / 2), int(size / 2)), (0, 0)], mode='mean')
    if rgb:
        for i in range(color_size):
            for j in range(y_size):
                for k in range(x_size):
                    im_sum = 0
                    for x in range(size):
                        for y in range(size):
                            im_sum += tm[j + y][k + x][i] * im_filter[y][x]
                    im[j][k][i] = im_sum
    return im
