import cv2

# Specify the location of the image you want to classify
img = cv2.imread('images/plane.jpg')

# Get original height and width
print(f"Original Dimensions : {img.shape}")

# resize image by specifying custom width and height
resized = cv2.resize(img, (32, 32))

print(f"Resized Dimensions : {resized.shape}")
# Specify the loaction where you want to save the resized image and the name of the new image
cv2.imwrite('scaled_images/resized_plane.jpg', resized)