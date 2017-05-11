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

# built image string
image_string = builtImageString(name, currentnumber, endnumber, '.jpg')

# instert text at current position
editor.addText(image_string)

# increase index
currentnumber += 1