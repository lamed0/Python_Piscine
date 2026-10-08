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