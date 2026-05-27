import numpy as np
from PIL import Image


def ft_invert(img):
    """
    invert image colors
    """
    try:

        img_arr = np.array(img)
        colors_arr = img_arr[:, :, :3]
        inverted_col_arr = 255 - colors_arr

        inverted_img = Image.fromarray(inverted_col_arr)
        inverted_img.save("iverted.jpg")

    except Exception:
        print("error!")


def ft_red(img):
    """
    apply red filter to image
    """
    try:

        img_arr = np.copy(img)
        img_arr[:, :, 1] = 0
        img_arr[:, :, 2] = 0

        inverted_img = Image.fromarray(img_arr.astype(np.uint8))
        inverted_img.save("red.jpg")

    except Exception:
        print("error!")


def ft_green(img):
    """
    apply green filter to image
    """
    try:

        img_arr = np.copy(img)
        img_arr[:, :, 0] = 0
        img_arr[:, :, 2] = 0

        inverted_img = Image.fromarray(img_arr.astype(np.uint8))
        inverted_img.save("green.jpg")

    except Exception:
        print("error!")


def ft_blue(img):
    """
    apply blue filter to image
    """
    try:

        img_arr = np.array(img)
        img_arr[:, :, 0] = 0
        img_arr[:, :, 1] = 0

        inverted_img = Image.fromarray(img_arr)
        inverted_img.save("blue.jpg")

    except Exception:
        print("error!")


def ft_grey(img):
    """
    apply gray filter to image
    """
    try:

        img_arr = np.array(img).astype(np.float32)

        gray = (
            0.299 * img_arr[:, :, 0]
            + 0.587 * img_arr[:, :, 1]
            + 0.114 * img_arr[:, :, 2]
        )
        print(gray)
        gray = np.clip(gray, 0, 255).astype(np.uint8)

        inverted_img = Image.fromarray(gray, mode="L")
        inverted_img.save("grey.jpg")

    except Exception as e:
        print(e)
        print("error!")
