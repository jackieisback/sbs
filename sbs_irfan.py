import os
import datetime

snapshot_dir = r"C:\Users\Alex\Pictures"
path_to_irfanview = r'"C:\Program Files (x86)\IrfanView\i_view32.exe" '
once = 1

def getFilesInDir(dir):
  # get all files in directory
  files_in_folder = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
  # return only files with .png ending
  return [i for i in files_in_folder if i.endswith(".png")]

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
    
#console.run(r'"C:\Program Files\IrfanView\i_view64.exe" "D:\test\irfan\vacation_tool.png" "D:\test\irfan\vc2.png" /resize_long=300 /aspectratio /convert=D:\test\irfan\$N-01.jpg"')
