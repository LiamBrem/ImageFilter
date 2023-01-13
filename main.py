from PIL import Image, ImageFilter
import os


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

  stringInput += f"{str(len(method_list) + 1)}. Exit"


  #main loop
  while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    optionInput = input(stringInput)
    #make it so that the user can only enter a number
    while not (optionInput.isdigit()):
      optionInput = input("Please enter a number: ")
  
    #make option input corresponds to the correct method of the above class using if statements
    if optionInput == 1:
      img.black_white()
    elif optionInput == 2:
      img.blur()
    elif optionInput == 3:
      img.flip()
    elif optionInput == 4:
      img.rotate()
    elif optionInput == 5:
      img.sharpen()
    elif optionInput == len(method_list) + 1:
      break
    else:
      print("Please enter a number between 1 and " + str(len(method_list) + 1))
  
    print(optionInput)


def optionSequence(fileName):
  #create image editor object
  img = ImageEditor(fileName)
  #make a while loop that lets the user call functions from the class through input to edit the image usin input, also let them stop it and save the image
  while True:
    #get the user input
    user_input = input("What do you want to do?\n1. Edit\n2. Save\n3. Quit\n")

    #if the user input is 1, edit the image
    if user_input == "1":
      img = editSequence(img)

    #if the user input is 2, save the image
    elif user_input == "2":
      img.save("filteredImages/" + fileName + ".png", "PNG")

    #if the user input is 3, quit the program
    elif user_input == "3":
      os.system('cls' if os.name == 'nt' else 'clear')
      break

    #if the user input is anything else, print an error message
    else:
      print("Invalid input, please try again.")

  img.black_white()

  img.save("test")


if __name__ == '__main__':

  correctName = False

  while correctName == False:

    #ask user to input the image file name
    image_file_name = input(
      'Please input the image file name (include .png/.jpg): ')

    #check if the image file exists in uploadImages folder
    if os.path.isfile("uploadImages/" + image_file_name):
      correctName = True
      optionSequence("uploadImages/" + image_file_name)
    else:  #if the image file doesn't exist in uploadImages folder
      print('The image file doesn\'t exist in uploadImages folder')
