import os

# path to 7zip exe
path_to_7zip = r'"C:\Program Files\7-Zip\7zG.exe" '

# get current working file (sb.txt or intro.txt)
working_file = notepad.getCurrentFilename()

# get current working folder
working_folder = os.path.normpath(os.path.join(working_file,'../'))

# get the path to the current file
path_to_sb_txt = "\"" + working_folder + "\\sb.txt" + "\""

# get path to intro.txt file
path_to_intro_txt = "\"" + working_folder + "\\intro.txt" + "\""

# path to pic directory
pic_dir = "\"" + working_folder + "\\pic" + "\""

# name of .zip file
output_file = "\"" + working_folder + "\\sb.zip" + "\""

# built command string
commandstring = path_to_7zip + "a " + output_file + " " + path_to_sb_txt + " " + path_to_intro_txt + " " + pic_dir + "\\*"

#run command
console.run(commandstring)