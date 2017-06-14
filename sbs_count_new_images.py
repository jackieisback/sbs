import os

snapshot_dir = r"C:\Users\XXX\Pictures"

def getFilesInDir(dir):
  # get all files in directory
  files_in_folder = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
  # return only files with .png ending
  return [i for i in files_in_folder if i.endswith(".png")]

# get all .png files in snapshout folder
rel_files = getFilesInDir(snapshot_dir)

#reset counter
counter = 0

# first call?
if 'time_last_element' not in locals():
  time_last_element = 0

# get number of new elements
for idx, file in enumerate(rel_files):
  # get full path to file
  fullpath = snapshot_dir + "\\" + file
  # check how many pictures were created after the previous call
  if os.path.getctime(fullpath) > time_last_element:
    counter = counter + 1

# get the time of the last element
time_last_element = os.path.getctime(snapshot_dir + "\\" + rel_files[-1])

# add text to cursor position
editor.addText("#" + str(counter))
