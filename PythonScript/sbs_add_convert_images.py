# The lines up to and including sys.stderr should always come first
# Then any errors that occur later get reported to the console
# If you'd prefer to report errors to a file, you can do that instead here.
import os
import re

# parts that need to be adapted
snapshot_dir = r"C:\Users\Jackie500\Pictures"
path_to_irfanview = r'"D:\01_Tools\NConvert\nconvert.exe" '

numInts = 4
useMovieFolderForImages = 1

def getFilesInDir(dir, picType):
    # get all files in directory
    files_in_folder = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
    # return only files with .png ending
    return [i for i in files_in_folder if i.endswith(picType)]

def getPicDir():
    # get the path to the current file
    path_to_sb_txt = notepad.getCurrentFilename()

    # pic directory
    pic_dir = os.path.normpath(os.path.join(path_to_sb_txt,'../')) + "\\pic"

    return pic_dir

def getLatestNumberInPicFolder():
    latestNumber = ""

    # pic directory
    pic_dir = getPicDir()

    rel_files = getFilesInDir(pic_dir, ".jpg")

    if rel_files:
        latestNumber = re.findall(r'\d+', rel_files[-1])
    else:
        latestNumber = ["0000"]

    return latestNumber[0]

def buildImageString(latestNumber, numZeros):
    zeros = ""
    while numZeros > 0:
        zeros += '0'
        numZeros -= 1

    latestNumber += 1

    return '[' + 'img' + '-' + zeros + str(latestNumber) + '.jpg' + ']'


def getImageString():
    latestNumber = ""

    # get latest number in pic folder
    latestNumber = getLatestNumberInPicFolder()
    # caluclate number of zeros
    numZeros = numInts - len(str(int(latestNumber)+1))
    # build image string
    ImageString = buildImageString(int(latestNumber), numZeros)

    return ImageString

def createImage(file, ImageString):
    # get full path to file
    fullpath = snapshot_dir + "\\" + file
    # add "" to filestring
    filestring = "\"" + fullpath + "\""

    # pic directory
    pic_dir = getPicDir()

    # get current filename
    filename = os.path.basename(notepad.getCurrentFilename())

    if "sb.txt" in filename:
        resize = "-resize 390 0 "
    else:
        resize = "-resize 500 0 "

    #commandstring = path_to_irfanview + filestring + resize + r' /aspectratio /convert=' + pic_dir + "\\" + ImageString[1:-1] + "\""
    commandstring = path_to_irfanview + "-out jpeg " + "-o " + "\"" + pic_dir + "\\" + ImageString[1:-1] + "\"" + " -ratio " + resize + filestring
	
    console.run(commandstring)

def moveFile(file, snapshot_dir):
    if useMovieFolderForImages == 1:
        # get the name of the movie folder
        path = os.path.normpath(notepad.getCurrentFilename())
        newFolder = snapshot_dir + "\\" + path.split(os.sep)[-2] + "\\"
    else:
    # use default folder called move
        newFolder = snapshot_dir + "\\move\\"

    # check if new folder already exists
    isExist = os.path.exists(newFolder)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(newFolder)

    filestring = snapshot_dir + "\\" + file
    newFilestring = newFolder + file
    os.rename(filestring, newFilestring)


# get new raw images
newImages = getFilesInDir(snapshot_dir, ".png")
# loop over raw images
for idx, file in enumerate(newImages):
    # create image string
    ImageString = getImageString()
    # add image string in editor
    editor.addText(ImageString)
    # create image file
    createImage(file, ImageString)
    # move file
    moveFile(file, snapshot_dir)
	