import numpy as np
from PIL import Image
from scipy.ndimage import zoom


def zoom_img(img, zoom_factor: float = 2.0):
    """
    takes an image and zoom it
    """

    try:

        zoomed_array = zoom(img, (zoom_factor, zoom_factor, 1))
        zoomed_array = np.clip(zoomed_array, 0, 255).astype(np.uint8)

        orig_h, orig_w = img.shape[:2]
        new_h, new_w = zoomed_array.shape[:2]

        top = (new_h - orig_h) // 2
        left = (new_w - orig_w) // 2

        cropped = zoomed_array[top: top + orig_h, left: left + orig_w]

        result = Image.fromarray(cropped)
        result.save("result.jpeg")

    except Exception:
        print("error!")
