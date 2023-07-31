from PIL import Image
import os

# print(os.path.abspath(__file__))

# img = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)) ,'screenshot.png'))
# img.show()


imagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)) ,'screenshot.png')


myImage = Image.open(imagePath)
myImage.show()


# crop image
myBox = (0,0,400,400)
myNewImage = myImage.crop(myBox)
myNewImage.show()


# Convert image mode 
newImage = myImage.convert('L')
newImage.show()
