from PIL import Image, ImageFilter
import os


class ImageEditor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.image = Image.open(self.file_path)

        self.width = self.image.width
        self.height = self.image.height
        self.mwidth = self.width // 1000
        self.mheight = self.height // 1000
        if self.mwidth > self.mheight:
          self.scale = self.mwidth
        else:
          self.scale = self.mheight
        if self.scale != 0:
          self.image = self.image.resize( (self.width // self.scale, self.height // self.scale) )
          
  img = img.resize( (width // scale, height // scale) )

    #make a function that sharpens the image
    def sharpening(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
      
    #make a function that flips the image
    def flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)

    #make a function that rotates the image
    def rotate(self):
        self.image = self.image.rotate(90, expand=True)  

    #make a save function that saves the new image to filteredImages file      
    def save(self, name):
        self.image.save("filteredImages/" + name + ".png", "PNG")
        

def editSequence(fileName):
  #create image editor object 
  img = ImageEditor(fileName)

  img.save("test")
  

if __name__ == '__main__':

  correctName = False
    
  while correctName == False:
    
  #ask user to input the image file name
    image_file_name = input('Please input the image file name (include .png/.jpg): ')
  
    #check if the image file exists in uploadImages folder
    if os.path.isfile("uploadImages/" + image_file_name):
      correctName = True
      editSequence("uploadImages/" + image_file_name)
    else: #if the image file doesn't exist in uploadImages folder
      print('The image file doesn\'t exist in uploadImages folder')
      