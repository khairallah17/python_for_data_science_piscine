import numpy as np
from PIL import Image


def ft_rotate(img):

    try:

        # rotated_img = [[img[j][i] for j in range(len(img))] for i in range(len(img[0]))]

        rotated_img = np.zeros(
            (img.shape[1], img.shape[0], img.shape[2]), dtype=img.dtype
        )
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                rotated_img[j][i] = img[i][j]

        rotated = Image.fromarray(rotated_img)
        rotated.save("rotated.jpeg")

    except Exception as e:
        print(e)
        print("error!")
