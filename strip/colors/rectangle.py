import cv2

# Load the image
image_path = 'sample/image1.jpg'  # Replace with the actual image path
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding or other preprocessing techniques if needed
# threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]

# Detect contours in the image
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over the detected contours
for contour in contours:
    # Approximate the contour to a polygon with a certain epsilon value
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # Check if the contour has 4 corners (a rectangle or square)
    if len(approx) == 4:
        # Draw the contour on the original image
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)

        # Get the coordinates of the corners
        corners = [tuple(point[0]) for point in approx]

        # Display the coordinates of the corners
        print('Corners:', corners)

# Display the image with detected rectangles/squares
cv2.imshow('Rectangles and Squares', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
