import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    loads an image file return its content as an array of RGB format.

    Args:
        path (str): path of the file to load.

    Returns:
        np.ndarray: numpy array represents the RGB format of the image.
    """
    try:

        image = Image.open(path)
        res = np.asarray(image)

        print(f"The shape of the image is: {res.shape}")
        return res

    except Exception:
        print("error!")
        return np.array([])
