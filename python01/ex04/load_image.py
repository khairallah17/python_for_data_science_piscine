import numpy as np
from PIL import Image


def ft_load(path: str) -> array:
    """
    load specific image file and return as as numpy array
    """
    try:

        image = Image.open(path)
        res = np.asarray(image)

        print(f"The shape of the image is: {res.shape}")
        return res

    except Exception:
        print("error!")
