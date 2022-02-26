# import the library opencv
import cv2
import glob

file_list = glob.glob('Original/*.jpg')  # Returns a list of file names with only jpg extension
print(file_list)                         # Prints the list containing file names

my_list = []                  # Empty list to store images from the folder.
path = "Original/*.jpg"       
for file in glob.glob(path):  # Iterate through each file in the list using for
    print(file)               # just stop here to see all file names printed
    a = cv2.imread(file)      # now, we can read each file since we have the full path
    my_list.append(a)         # Create a list of images (not just file names but full images)

path = "Original/*.jpg" # select the path
img_number = 1          # initialize a var to start an iterator for image number.

for file in glob.glob(path):
    a = cv2.imread(file)                  # now, we can read each file since we have the full path
                                          # process each image - change color from BGR to RGB.
    c=cv2.cvtColor(a, cv2.COLOR_BGR2GRAY) # Change color space from BGR to RGB
    cv2.imwrite("/Gray_Scale/t1" + str(img_number) + ".jpg", c) #Storing the image
    img_number += 1
    cv2.imshow('Color image', c)         # Display each image for 1 second
    cv2.waitKey(1000)                     
    cv2.destroyAllWindows()
