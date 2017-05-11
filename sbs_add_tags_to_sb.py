
def addtimes(contents):
		#init global variables
		global sek
		global min
		global f_type
		global index;
		#split line where "Min." or "Sek." was found
		split_array = contents.split()
		#get size of the line
		size = len(split_array)
		
		#check if type (DVD, VHS, etc.) is already in list
		if f_type.count(split_array[0]) == 0:
			#if not add it to the array
			f_type.append(split_array[0])
			min.append(0)
			sek.append(0)
			
		#get the index of the type
		index = f_type.index(split_array[0])
			
		#forelaste index is the field with xx:xx Min. or xx Sek.
		#split this line again
		min_sek_split = split_array[size-2].split(":")
		
		#check if it was a line with Min. or Sek. and sum up the time
		if len(min_sek_split) > 1:
			min[index] = min[index] + int(min_sek_split[0])
			sek[index] = sek[index] + int(min_sek_split[1])
		else:
			sek[index] = sek[index] + int(min_sek_split[0])
		
		#sek = sek + int(split_array[size-2])

def testContents(contents, lineNumber, totalLines):
        if "Min." in contents:
				editor.replaceLine(lineNumber, "<b>" + contents.rstrip("\r\n") + "</b>")
				addtimes(contents)
				return 1
        elif "Sek." in contents:
				editor.replaceLine(lineNumber, "<b>" + contents.rstrip("\r\n") + "</b>")
				addtimes(contents)
				return 1
        elif "][" in contents:
				editor.replaceLine(lineNumber, "<b>" + contents.rstrip("\r\n") + "</b>")
        #if contents.strip() == "rubbish":
                # editor.deleteLine(lineNumber)
                # As we've deleted the line, the "next" line to process
                # is actually the current line, so we return 0 to advance zero lines
                # and hence stay on the same line
                #return 0

        #elif contents.strip() == "something old":
                #editor.replaceLine(lineNumber, "something new")

        #elif contents.strip() == "little something":
                #editor.replaceLine(lineNumber, "BIG\nSOMETHING"
                # Here we return 2, as we've inserted a newline,
                # and we don't want to test the "SOMETHING" line again
                #return 2

        # if you wanted, you could optionally return 1 here, to move the next line
        # but that's the default, so you don't need to bother.


#int global variables
sek = []
min = []
m =[]
s = []
f_type = []
index = 0
i =0

# test every line
editor.forEachLine(testContents)

# get minutes and seconds
#m = min + sek/60
#s = sek % 60

for i in range(0,len(f_type),1):
	m.append(0)
	s.append(0)
	m[i] = min[i] +sek[i]/60
	s[i] = sek[i]%60
	
console.show()

for x in xrange(0, len(f_type)):
	console.write(str(f_type[x]) + " " + str(m[x]) + ":" + str(s[x]) + " Min.")
	
	
# import re
# pattern = re.compile(r'^\[(\d{2}):(\d{2}):(\d{2})\]\[(\d{2}):(\d{2}):(\d{2})\]$)
# pattern.search('string')

# re.search(pat, 'string')