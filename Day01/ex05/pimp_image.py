import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Converts the color of the image received."""
    result = 255 - array
    plt.imshow(result)
    plt.show()
    return (result)


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keep only the red channel of the image."""
    result = array.copy()
    result[:, :, 1] = result[:, :, 1] * 0
    result[:, :, 2] = result[:, :, 2] * 0
    plt.imshow(result)
    plt.show()
    return (result)


def ft_green(array: np.ndarray) -> np.ndarray:
    """This function convert an image to the green color."""
    result = array.copy()
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
    plt.imshow(result)
    plt.show()
    return (result)


def ft_blue(array: np.ndarray) -> np.ndarray:
    """This function convert an image to the blue color."""
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    plt.imshow(result)
    plt.show()
    return (result)


def ft_grey(array: np.ndarray) -> np.ndarray:
    """This function convert an image to the grey color."""
    result = array.copy()
    result[:, :, 0] = result[:, :, 0] / 1
    result[:, :, 1] = result[:, :, 0]
    result[:, :, 2] = result[:, :, 0]
    plt.imshow(result)
    plt.show()
    return result
