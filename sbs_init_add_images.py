# global variables
startnumber = 1
name = ''
endnumber = 0
currentnumber = startnumber

def getInputs(name, endnumber):
  # last number of image row
  endnumber = int(notepad.prompt('Enter last number', ''))
  # get image name (before the numbers)
  name = notepad.prompt('Enter image pre-name', '')
  return (name, endnumber)

# get name and endnumber
name, endnumber = getInputs(name, endnumber)