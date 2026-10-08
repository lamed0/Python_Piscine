import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array : np.ndarray) -> np.ndarray:
    """Invert every pixel of an image."""
    return (255 - array)

def ft_red(array : np.ndarray) -> np.ndarray:
    """Keep only the red channel of the image."""
    result = array.copy()
    result[:, :, 1] = result[:, :, 1] * 0
    result[:, :, 2] = result[:, :, 2] * 0
    return (result)


def ft_green(array : np.ndarray) -> np.ndarray:
    """This function convert an image to the green color."""
    result = array.copy()
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
    return (result)


def ft_blue(array : np.ndarray) -> np.ndarray:
    """This function convert an image to the blue color."""
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    return (result)

def ft_grey(array : np.ndarray) -> np.ndarray:
    """This function convert an image to the blue color."""
    result = array.astype(float)
    grey = (
        result[:, :, 0] / 3
        + result[:, :, 1] / 3
        + result[:, :, 2] / 3
    )
    result[:, :, 0] = grey
    result[:, :, 1] = grey
    result[:, :, 2] = grey
    return (result.astype(np.uint8))



# import matplotlib.pyplot as plt

# from load_image import ft_load
# from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


# array = ft_load("landscape.jpg")
# print(ft_invert.__doc__)
# images = [
#     ("Original", array),
#     ("Invert", ft_invert(array)),
#     ("Red", ft_red(array)),
#     ("Green", ft_green(array)),
#     ("Blue", ft_blue(array)),
#     ("Grey", ft_grey(array)),
# ]

# plt.figure(figsize=(12, 8))

# for position, (title, image) in enumerate(images, start=1):
#     plt.subplot(2, 3, position)
#     plt.imshow(image)
#     plt.title(title)
#     plt.axis("off")

# plt.tight_layout()
# plt.show()
