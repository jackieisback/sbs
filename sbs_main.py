import os
import datetime

# parts that need to be adapted
snapshot_dir = r"C:\Users\XXX\Pictures"
path_to_irfanview = r'"C:\Program Files (x86)\IrfanView\i_view32.exe" '

# global variables
img_ctr = 0
currentnumber = 1

def getFilesInDir(dir):
  # get all files in directory
  files_in_folder = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
  # return only files with .png ending
  return [i for i in files_in_folder if i.endswith(".png")]

def moveAndConvertImages():
  global snapshot_dir
  global path_to_irfanview
  global img_ctr
  once = 1

  # get the path to the current file
  path_to_sb_txt = notepad.getCurrentFilename()

  # pic directory
  pic_dir = os.path.normpath(os.path.join(path_to_sb_txt,'../')) + "\\pic"
  
  # get creation date of file
  cr_t = os.path.getctime(path_to_sb_txt)

  # get all .png files in snapshout folder
  rel_files = getFilesInDir(snapshot_dir)

  img_ctr = 1
  for idx, file in enumerate(rel_files):
    # get full path to file
    fullpath = snapshot_dir + "\\" + file
    # find files which are created after the sb.txt creation date
    if os.path.getctime(fullpath) > cr_t:
    
      if once == 1:
        # calculate how many zeros before the number in the converted files are needed
        zeros = len(str(len(rel_files)-idx))
        # this needs only to be done once
        once = 0
      
      # add "" to filestring
      filestring = "\"" + fullpath + "\""
      # how many zeros are needed before number
      num_zeros = zeros - len(str(img_ctr))
      name = "img-" + num_zeros * "0" + str(img_ctr) + ".jpg"
      # built command string
      # commandstring = path_to_irfanview + filestring + r' /resize_long=350 /aspectratio /convert=D:\test\irfan\pic' + "\\" + name + "\""
      commandstring = path_to_irfanview + filestring + r' /resize_long=350 /aspectratio /convert=' + pic_dir + "\\" + name + "\""
      console.run(commandstring)
      img_ctr += 1
  # decrease image counter at end of function, since it was increased by one but this value was never used
  img_ctr -= 1
  
# create the image string
def builtImageString(name, currentnumber, endnumber, ending):
  zeros = ''

  # get the length of numbers
  length_number = len(str(currentnumber))
  length_endnumber = len(str(endnumber))
  
  # calculate the difference
  diff = length_endnumber-length_number
  
  # calculate the number of zeros
  while diff > 0:
    zeros += '0'
    diff -= 1
  
  return '[' + name + '-' + zeros + str(currentnumber) + ending + ']'

# build image string and replaces it with the current line
def addimagestring(number, lineNumber):
  global currentnumber
  global img_ctr
  name = "img"
  complete_string = ""
  
  for idx in range(0, number):
  
    # built image string
    image_string = builtImageString(name, currentnumber, img_ctr, '.jpg')
    # append to complete string
    complete_string = complete_string + image_string
    # increase index
    currentnumber += 1
  
  # instert text at current position
  #editor.addText(image_string)
  editor.replaceLine(lineNumber, complete_string)
  

def editContent(contents, lineNumber, totalLines):
        if "Min." in contents:
          editor.replaceLine(lineNumber, "<b>" + contents.rstrip("\r\n") + "</b>")
          #addtimes(contents) TODO
          return 1
        elif "Sek." in contents:
          editor.replaceLine(lineNumber, "<b>" + contents.rstrip("\r\n") + "</b>")
          #addtimes(contents) TODO
          return 1
        elif "][" in contents:
          editor.replaceLine(lineNumber, "<b>" + contents.rstrip("\r\n") + "</b>")
        elif "#" in contents:
          addimagestring(int(contents[1:]), lineNumber)


# move and convert images from image folder to pic folder
moveAndConvertImages()
    
# loop over every line
# - do the conversion
# - replace special image tags (#3) with image
editor.forEachLine(editContent)