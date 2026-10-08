from PIL import Image, UnidentifiedImageError
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """Load a JPG/JPEG image and return its pixels in RGB format."""
    if not isinstance(path, str):
        raise AssertionError("The path must be a string.")

    try:
        image = Image.open(path)
        if image.format not in {"JPEG", "JPG"}:
            raise AssertionError("The image must be in JPG or JPEG format.")
        rgb_image = image.convert("RGB")
        pixels = np.array(rgb_image)
        image_format = image.format
    except FileNotFoundError as error:
        raise AssertionError("Image file not found.") from error
    except UnidentifiedImageError as error:
        raise AssertionError("The file is not a valid image.") from error
    except OSError as error:
        raise AssertionError(f"Unable to open image: {error}") from error

    print("The shape of image is:", pixels.shape)
    print(pixels)
    return pixels


def zoom_img(img: np.ndarray) -> np.ndarray:
    """Return the exercise's 400-by-400 grayscale crop."""
    if img.shape[0] < 500 or img.shape[1] < 850:
        raise AssertionError("The image is too small for the requested crop.")
    return img[100:500, 450:850, 0:1]
