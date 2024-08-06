# import the necessary packages
import argparse
import imutils
import cv2
# construct the argument parser and parse the argument
# load the input image (whose path was supplied via command line
# argument) and display the image to our screen
image = cv2.imread("daunhitam.png")
cv2.imshow("Image", image)
cv2.waitKey(0)

blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

# convert the image to grayscale
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)


# threshold the image by setting all pixel values less than 225
# to 255 (white; foreground) and all pixel values >= 225 to 255
# (black; background), thereby segmenting the image
# thresh = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY_INV)[1]
# cv2.imshow("Thresh", thresh)
# cv2.waitKey(0)
# find contours (i.e., outlines) of the foreground objects in the
# thresholded image
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = blurred.copy()


# loop over the contours
# for c in cnts:
# 	# draw each contour on the output image with a 3px thick purple
# 	# outline, then display the output contours one at a time

cv2.drawContours(output, cnts, -1, (240, 0, 159), 3)
cv2.imshow("Contours", output)
cv2.waitKey(0)
	 

# draw the total number of contours found in purple
text = "I found {} objects!".format(len(cnts))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)

