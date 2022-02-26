import cv2 as cv              #for manipulating images
import numpy as np            #for using nd array
import pandas as pd           #for loading csv file

location="cat"                       #location var storing cat folder
points=pd.read_csv("data_labels.csv")#reading csv file
n=len(points)                        #length of csv file

for i, name in enumerate(points["name"][1:]): #to keep a count of iterations
  img_path = location + "/" + name
  img = cv.imread(img_path)                   #reading image using cv2 lib

  start = (int(points["xmin"][i+1]), int(points["ymax"][i+1])) #initializing start point
  end = (int(points["xmax"][i+1]), int(points["ymin"][i+1]))   #iitializing end point

  color = list(np.random.random(size=3) * 256)                 #creating list of random colors for box

  thickness = [x+1 for x in range(0, n, 1)]                    #variable thickness for box
  print(i)                                                     #printing index no

  #Drawing bouding box
  Annotated_Img = cv.rectangle(img, start, end, color, thickness[i]) #bouding box is rectangle

  fonts = [
           cv.FONT_HERSHEY_COMPLEX,                            #different fonts for different images
           cv.FONT_HERSHEY_TRIPLEX,
           cv.FONT_HERSHEY_COMPLEX_SMALL,
           cv.FONT_HERSHEY_SCRIPT_SIMPLEX,
           cv.FONT_HERSHEY_SCRIPT_COMPLEX,
           cv.FONT_ITALIC,
           cv.FONT_HERSHEY_PLAIN,
           cv.FONT_HERSHEY_DUPLEX,
           cv.QT_FONT_BLACK,
           cv.FONT_HERSHEY_SIMPLEX
           ]


  cv.putText(img= Annotated_Img,                               #printing image name over respective image
             text=points["label"][i + 1],
             org=(100,100),
             fontFace=fonts[i],
             fontScale=thickness[i],
             color=color)

  cv.imshow(name,  Annotated_Img)                              #Displaying image
  cv.waitKey(0)
  cv.destroyAllWindows()
  cv.imwrite("Annotation/"+name+".jpg", Annotated_Img)         #Storing the image