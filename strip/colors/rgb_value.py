

import cv2

def values(image_path):


# Load the image
    #image_path = 'sample/image3.jpg'  # Replace with the actual image path
    image = cv2.imread(image_path)

    # Define the coordinates of the points
    coordinates = [(155, 65), (155, 165), (155, 265), (155, 365), (155, 465),
                (155, 555), (155, 655), (155, 755), (155, 855), (155, 950)]

    # Dictionary to store the RGB values
    colors = {}

    # Get the RGB values at each coordinate
    for i, (x, y) in enumerate(coordinates, start=1):
        # Get the BGR values at the given coordinate
        b, g, r = image[y, x]

        # Store the RGB values in the dictionary
        colors[f'Point {i}'] = (r, g, b)

    return(colors) 
# Print the RGB values



'''

import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Retrieve the RGB values at the clicked point
        b, g, r = image[y, x]

        # Display the coordinates and RGB values
        print(f'Clicked at (x={x}, y={y})')
        print(f'RGB: ({r}, {g}, {b})')

        # Display a small circle at the clicked point
        cv2.circle(image, (x, y), 3, (0, 255, 0), -1)
        cv2.imshow('Image', image)

# Load the image
image_path = 'sample/image5.jpg'  # Replace with the actual image path
image = cv2.imread(image_path)

# Create a named window and set the mouse callback
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', click_event)

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''