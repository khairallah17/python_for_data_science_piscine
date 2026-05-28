import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    load specific image file and return as as numpy array
    """
    try:

        image = Image.open(path)
        res = np.asarray(image)

        return res

    except Exception:
        print("error!")
        raise
