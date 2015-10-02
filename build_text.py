file = open('/home/jwss/text.txt', 'w')

for x in range(0,1000):
	file.write("%i\n" %x)

print "done."
