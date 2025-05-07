import numpy as np
import matplotlib.pyplot as plt

# Create a small 3x3 RGB image
img = np.zeros((4, 4, 3), dtype=np.uint8)  # Initialize with all zeros (black)

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


# --- Color Definitions ---
red   = [255, 0, 0]
green = [0, 255, 0]
blue  = [0, 0, 255]
white = [255, 255, 255]
black = [0, 0, 0]
magenta = [255, 0, 255]
cyan = [0, 255, 255]
yellow = [255, 255, 0]

# --- Manipulating Pixels ---

# First Row
img[top_left]     = red       # Top-left pixel to red
img[top_middle]   = black    # Top-middle pixel to green
img[top_right]    = black     # Top-right pixel to blue

# Second Row
img[middle_left]  = black    # Middle-left pixel to yellow
img[middle_middle]= green   # Center pixel to magenta
img[middle_right] = black    # Middle-right pixel to cyan

# Third Row
img[bottom_left]  = black    # Bottom-left pixel to white
img[bottom_middle]= black   # Gray
img[bottom_right] = blue    # Bottom-right pixel to black

img[far_bottom_left]=black
img[far_bottom_middle]=black
img[far_bottom_right]=black
img[far_bottom_far_right]=white

# --- Display the Image ---
plt.imshow(img)
plt.title("Manipulated 3x3 RGB Image")
# plt.axis('off')  # Hide axes
plt.show()

# --- Explanation ---
print("Explanation:")
print("- `img[row, column] = [R, G, B]` sets the color of the pixel at the specified row and column.")
print("- `R`, `G`, and `B` are the red, green, and blue color components, ranging from 0 to 255.")
print("- The pixel locations (top_left, middle_middle, etc.) are defined as tuples (row, column) for clarity.")
print("- You can change the colors and pixel locations to experiment with different patterns.")