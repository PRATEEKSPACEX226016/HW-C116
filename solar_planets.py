import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Mercury", (110, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Venus", (190, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Earth", (290, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Mars", (390, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Jupiter", (560, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Saturn", (800, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Uranus", (970, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Neptune", (1110, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))

cv2.imshow("output", img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg", img)
