import commands
import sys

filename = '/home/jwss/text.txt'
locationFilename = '/home/jwss/textLocation.txt'
cutSize = 100


numLines = commands.getstatusoutput('cat %s | wc -l' %filename)[1]

print numLines

locationFile = open (locationFilename, 'r+')

locationData = locationFile.readline()

location = int(locationData) * cutSize

if (location > int(numLines)):
	print ('We have reached the end of the file %s' % locationFilename)
	sys.exit()


file = open (filename, 'r')


for x in range(0, int(numLines)):

	line = file.readline()

	if (x > (int(locationData) * cutSize) and x <= ((int(locationData) * cutSize) + cutSize)):
		print line


file.close()

locationFile.seek(0)

locationFile.write('' + str((int(locationData)+1)))

locationFile.close()
