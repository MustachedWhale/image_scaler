import cv2

image = cv2.imread("C:\\Users\\jonat\\Documents\\Art Prints\\test\\8x8in.jpg")

new_width = 3600
new_height = 3600

resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

cv2.imwrite("C:\\Users\\jonat\\Documents\\Art Prints\\test\\12x12in.jpg", resized_image)