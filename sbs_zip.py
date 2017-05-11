import os

# path to 7zip exe
path_to_7zip = r'"C:\Program Files\7-Zip\7zG.exe" '

# get the path to the current file
path_to_sb_txt = notepad.getCurrentFilename()

# get path to intro.txt file
path_to_intro_txt = "\"" + os.path.normpath(os.path.join(path_to_sb_txt,'../')) + "\\intro.txt" + "\""

# path to pic directory
pic_dir = "\"" + os.path.normpath(os.path.join(path_to_sb_txt,'../')) + "\\pic" + "\""

# name of .zip file
output_file = "\"" + os.path.normpath(os.path.join(path_to_sb_txt,'../')) + "\\sb.zip" + "\""

path_to_sb_txt = "\"" + path_to_sb_txt + "\""
# built command string
commandstring = path_to_7zip + "a " + output_file + " " + path_to_sb_txt + " " + path_to_intro_txt + " " + pic_dir + "\\*"

#run command
console.run(commandstring)
