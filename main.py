from PIL import Image, ImageFilter
import os
import time
import random

firstIteration = True

class ImageEditor:

  def __init__(self, file_path):
    self.file_path = file_path
    self.image = Image.open(self.file_path)

    #resizes the images
    self.width = self.image.width
    self.height = self.image.height
    self.mwidth = self.width // 1000
    self.mheight = self.height // 1000
    if self.mwidth > self.mheight:
      self.scale = self.mwidth
    else:
      self.scale = self.mheight
    if self.scale != 0:
      self.image = self.image.resize(
        (self.width // self.scale, self.height // self.scale))

  #make a function that sharpens the image
  def sharpen(self):
    self.image = self.image.filter(ImageFilter.SHARPEN)

  #make a function that flips the image
  def flip(self):
    self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)

  #make a function that rotates the image
  def rotate(self):
    self.image = self.image.rotate(90, expand=True)

  #make a function that blurs the image
  def blur(self):
    self.image = self.image.filter(ImageFilter.BLUR)

  #make a function that makes the image black and white
  def black_white(self):
    self.image = self.image.convert("L")

  #make a function that contours the image
  def contours(self):
    self.image = self.image.filter(ImageFilter.CONTOUR)

  def edgeEnchance(self):
    self.image = self.image.filter(ImageFilter.EDGE_ENHANCE_MORE)

  def emboss(self):
    self.image = self.image.filter(ImageFilter.EMBOSS)

  def smooth(self):
    self.image = self.image.filter(ImageFilter.SMOOTH)

  def randomizer(self):    
    pixels = self.image.getdata()
    new_pixels = []
    for p in pixels:
      new_pixels.append(p)

    location = 0
  # Continues until it has looped through all pixels
    while location < len(new_pixels):
      # Gets the current color of the pixel at location
      p = new_pixels[location]
      # Splits color into red, green and blue components
      r = p[0]
      g = p[1]
      b = p[2]

      changeBy = 50

      newr = random.randint(r-changeBy,r+changeBy)
      newg = random.randint(g-changeBy,g+changeBy)
      newb = random.randint(b-changeBy,b+changeBy)

      new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
      location += 1


    newImage = Image.new("RGB", self.image.size)
    newImage.putdata(new_pixels)
    
      
    self.image = newImage
  
  #make a save function that saves the new image to filteredImages file
  def save(self, name):
    self.image.save("filteredImages/" + name + ".png", "PNG")


def editSequence(img):

  # this a list of all the names of the methods in the above class
  method_list = [
    method for method in dir(ImageEditor)
    if method.startswith('__') is False and method != 'save'
  ]

  #use method list and format it to get user input for what option they want to do
  stringInput = ""
  for i in range(len(method_list)):
    stringInput += (str(i + 1) + ". " + method_list[i] + "\n")

  stringInput += f"\n{str(len(method_list) + 1)}. Save\n"
  stringInput += f"{str(len(method_list) + 2)}. Exit\n"

  #main loop
  while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    optionInput = input(stringInput)

    #make option input corresponds to the correct method of the above class using if statements
    if optionInput == "1":
      img.black_white()
    elif optionInput == "2":
      img.blur()
    elif optionInput == "3":
      img.contours()
    elif optionInput == "4":
      img.edgeEnchance()
    elif optionInput == "5":
      img.emboss()
    elif optionInput == "6":
      img.flip()
    elif optionInput == "7":
      img.randomizer()
    elif optionInput == "8":
      img.rotate()
    elif optionInput == "9":
      img.sharpen()
    elif optionInput == "10":
      img.smooth()
    elif int(optionInput) == len(method_list) + 1:
      os.system('cls' if os.name == 'nt' else 'clear')
      nameInput = input(
        "What is the name of the file you want to save? (dont include .jpg/.png): "
      )
      img.save(nameInput)
      optionSequence()

    elif int(optionInput) == len(method_list) + 2:
      break
    else:
      print("Please enter a number between 1 and " + str(len(method_list) + 2))
      time.sleep(3)


def optionSequence():
  #this clears the terminal
  os.system('cls' if os.name == 'nt' else 'clear')

  global firstIteration
  if firstIteration is True:
    firstIteration = False
    fileName = new()      
    img = ImageEditor(fileName) 

  #make a while loop that lets the user call functions from the class through input to edit the image usin input, also let them stop it and save the image
  while True:
    #get the user input
    user_input = input("What do you want to do?\n1. Edit\n2. Quit\n3. New\n")

    #if the user input is 1, edit the image
    if user_input == "1":

      ###WE HAVE TO MAKE IT SO THAT THE EDIT SEQUENCE RETURNS THE IMAGE OBJECT, GET RID OF SAVE IN EDIT IMAGE AND ADD IT TO THIS MENU
      img = editSequence(img)

    #if the user input is 3, quit the program
    elif user_input == "2":
      os.system('cls' if os.name == 'nt' else 'clear')
      break

    elif user_input == "3":
      fileName = new()
      
      img = ImageEditor(fileName)

    #if the user input is anything else, print an error message
    else:
      print("Invalid input, please try again.")



def new():
  correctName = False

  while correctName == False:

    #ask user to input the image file name
    image_file_name = input(
      'Please input the image file name (include .png/.jpg): ')

    #check if the image file exists in uploadImages folder
    if os.path.isfile("uploadImages/" + image_file_name):
      return "uploadImages/" + image_file_name
    else:  #if the image file doesn't exist in uploadImages folder
      print('The image file doesn\'t exist in uploadImages folder')


if __name__ == '__main__':
  optionSequence()
