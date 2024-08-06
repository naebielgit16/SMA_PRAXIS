# accessing opencv
import cv2 
import imutils  #instal imutils dulu yaa

# load the image
image = cv2.imread("garuda.jpg")

# check image size
h, w, d =  image.shape
print("image size:", h, w, d)

# # show the image
cv2.imshow("test", image)
cv2.waitKey(0)

# resize the image to 200x200px, ignoring aspect ratio
resized = cv2.resize(image, (108, 117))
cv2.imshow("Mini_Garuda", resized)
cv2.waitKey(0)

# # crop the image
cropped_image = image[110:130,100:125]
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)

# # Rotate the image
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

# Blurr the image
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

# Draw in the image
output = image.copy()
cv2.rectangle(output, (150, 60), (80, 16), (0, 0, 255), )
cv2.imshow("Rectangle", output)
cv2.waitKey(0)


output = image.copy()
cv2.circle(output, (50, 100), 20, (0, 255, 255), -1 )
cv2.imshow("Circle", output)
cv2.waitKey(0)

output = image.copy()
cv2.line(output, (60, 20), (150, 60), (0, 0, 255), 5)
cv2.line(output, (60, 50), (150, 30), (0, 0, 255), 5)
cv2.imshow("Garuda_Silang", output)
cv2.waitKey(0) 


output = image.copy()
cv2.putText(output, "Haloooo Guys", (10, 25), 
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)