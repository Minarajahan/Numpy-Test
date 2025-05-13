import numpy as np
import matplotlib.pyplot as plt

# Create a small 3x3 RGB image
img = np.zeros((5, 5, 3), dtype=np.uint8)  # Initialize with all zeros (black)

# --- Pixel Locations ---
# (row, column)
top_left     = (0, 0)
top_middle   = (0, 1)
top_right    = (0, 2)
middle_left  = (1, 0)
middle_middle= (1, 1)
middle_right = (1, 2)
bottom_left  = (2, 0)
bottom_middle= (2, 1)
bottom_right = (2, 2)
far_bottom_left=(3,0)
far_bottom_middle=(3,1)
far_bottom_right=(3,2)
far_bottom_far_right=(3,3)


black = [0, 0, 0]
white = [255, 255, 255]

# --- Pixel-by-pixel assignment (your original style) ---
img[0, 0] = black
img[0, 1] = white
img[0, 2] = black
img[0, 3] = white
img[0, 4] = black

img[1, 0] = white
img[1, 1] = black
img[1, 2] = white
img[1, 3] = black
img[1, 4] = white

img[2, 0] = black
img[2, 1] = white
img[2, 2] = black
img[2, 3] = white
img[2, 4] = black

img[3, 0] = white
img[3, 1] = black
img[3, 2] = white
img[3, 3] = black
img[3, 4] = white

img[4, 0] = black
img[4, 1] = white
img[4, 2] = black
img[4, 3] = white
img[4, 4] = black
# --- Display the Image ---
plt.imshow(img)
plt.title("Manipulated 5x5 RGB Image")
# plt.axis('off')  # Hide axes
plt.show()

# --- Explanation ---
print("Explanation:")
print("- `img[row, column] = [R, G, B]` sets the color of the pixel at the specified row and column.")
print("- `R`, `G`, and `B` are the red, green, and blue color components, ranging from 0 to 255.")
print("- The pixel locations (top_left, middle_middle, etc.) are defined as tuples (row, column) for clarity.")
print("- You can change the colors and pixel locations to experiment with different patterns.")