# Install necessary packages for PDF and image processing
%%capture
!apt-get install poppler-utils
!pip install pdf2image

# Import required libraries
from pdf2image import convert_from_path  # To convert PDFs to images
import requests  # To handle HTTP requests for downloading slides
import matplotlib.pyplot as plt  # For plotting images
import numpy as np  # For numerical computations, like handling matrices
from skimage.io import imread  # To read images from a URL
from skimage.transform import resize  # To resize images

# Define a function to display an image in grayscale
def plot(x):
    fig, ax = plt.subplots()  # Create a new figure and set of axes
    im = ax.imshow(x, cmap='gray')  # Show the image with a grayscale colormap
    ax.axis('off')  # Turn off axis labels
    fig.set_size_inches(5, 5)  # Set the figure size
    plt.show()  # Display the image

# Define a function to extract the Google Slide PDF URL from the standard presentation URL
def get_google_slide(url):
    url_head = "https://docs.google.com/presentation/d/"  # Base URL for Google Slides
    url_body = url.split('/')[5]  # Extract the unique presentation ID from the URL
    page_id = url.split('.')[-1]  # Extract the slide page ID
    return url_head + url_body + "/export/pdf?id=" + url_body + "&pageid=" + page_id  # Construct the PDF export URL

# Define a function to download and convert slides from a Google Slides URL into images
def get_slides(url):
    url = get_google_slide(url)  # Convert the Google Slides URL to a downloadable PDF URL
    r = requests.get(url, allow_redirects=True)  # Send a request to download the PDF
    open('file.pdf', 'wb').write(r.content)  # Save the downloaded PDF locally
    images = convert_from_path('file.pdf', 500)  # Convert the PDF pages to images
    return images  # Return the list of images

# Set the URL of a specific Google Slides deck
Data_Deck = "https://docs.google.com/presentation/d/12NWxIiiMua9mB6Lsj09JiyxC1FHvcO2Mrhf4jkOQeYo/edit#slide=id.g1e604f0493b_0_26"

# Retrieve the images from the deck
image_list = get_slides(Data_Deck)

# Get the number of images in the list
n = len(image_list)

# Display each image and print its shape (dimensions)
for i in range(n):
    plot(image_list[i])  # Display the image using the plot function
    print(np.array(image_list[i]).shape)  # Convert the image to an array and print its dimensions

# Set the target dimensions for resizing the images
h = 512  # Target height
w = 512  # Target width
c = 3  # Number of color channels (RGB)

# Create an empty array to store the resized images
image_array = np.zeros((n, h, w, c))

# Loop over the images to resize them and add them to the array
for i in range(n):
    image = image_list[i]  # Get the current image
    plot(image)  # Display the image
    image = np.array(image)  # Convert the image to an array
    print(image.shape)  # Print the shape of the original image
    image = resize(image, (512, 512))  # Resize the image to 512x512 pixels
    print(image.shape)  # Print the shape after resizing
    image_array[i] = image  # Store the resized image in the array

# Print the shape of one image after resizing
image.shape  # Output: (512, 512, 3), where 3 represents the RGB channels

# Print the shape of the entire image array
image_array.shape  # Output: (12, 512, 512, 3), representing 12 images, each of size 512x512 with 3 color channels

# Load an image from a URL
url = 'https://raw.githubusercontent.com/williamedwardhahn/MathData24/main/boat.png'  # URL of the image
im = imread(url)  # Read the image from the URL
plt.imshow(im)  # Display the image

# Print the shape of the image
im.shape  # Output: (418, 430, 4), where 4 channels could mean an RGBA image (with transparency)

# Resize the image to 512x512 pixels
im = resize(im, (512, 512))
plt.imshow(im)  # Display the resized image

# Print the shape of the resized image
im.shape  # Output: (512, 512, 4), resized with the same 4 channels

# Display the individual color channels (R, G, B, and Alpha if present) in grayscale
plt.imshow(im[:, :, 0], cmap='gray')  # Display the Red channel
plt.imshow(im[:, :, 1], cmap='gray')  # Display the Green channel
plt.imshow(im[:, :, 2], cmap='gray')  # Display the Blue channel
plt.imshow(im[:, :, 3], cmap='gray')  # Display the Alpha (transparency) channel
