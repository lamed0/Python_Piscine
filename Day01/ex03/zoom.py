from load_image import ft_load, zoom_img
import matplotlib.pyplot as plt
import numpy as np



def main():
    img_loaded = ft_load("animal.jpeg")
    zoomed = zoom_img(img_loaded)
    print("New shape after slicing:", zoomed.shape)
    print(zoomed)
    plt.imshow(zoomed[:, :, 0], cmap="gray")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()
    


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"Error: {error}")