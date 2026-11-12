from load_image import ft_load, zoom_img
import numpy as np
import matplotlib.pyplot as plt


def main():
    img = ft_load("animal.jpeg")
    zoomed = zoom_img(img)
    print("The shape of image is:", zoomed.shape)
    print(zoomed)
    row = len(zoomed)
    col = len(zoomed[0])

    transposed = [[0 for i in range(row)] for i in range(col)]
    for a in range(row):
        for b in range(col):
            transposed[b][a] = zoomed[a][b]
    rotated = np.array(transposed)
    print("New shape after Transpose:", rotated.shape)
    print(rotated[:, :, 0])
    plt.imshow(rotated[:, :, 0], cmap="gray")
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"Error: {error}")
