import os

filename = "lab.conf"

f = open (filename, "r")
l = f.readlines()
f.close()

def removeFinalEnter (txt):
	if len(txt) != 0 and txt[-1] == "\n":
		return removeFinalEnter (txt[:-1])
	return txt
def removeEnter (lst):
	for i in range (len (lst)):
		lst[i] = removeFinalEnter (lst[i])
	return lst
l = removeEnter (l)

def splitShitFinal (txt):
	return txt.split('[', 1 )[0]
def splitShit (lst):
	for i in range (len (lst)):
		lst[i] = splitShitFinal (lst[i])
	return lst
l = splitShit (l)

def removeEquals (lst):
	newLst = []
	for i in lst:
		exists = False
		for j in newLst:
			if i == j:
				exists = True
		if not exists and i != "":
			newLst = newLst + [i]
	return newLst
l = removeEquals (l)

for i in l:
	startup = i + ".startup"
	try:
		f = open (startup, "r")
	except:
		f = open (startup, "a")
		print "CREATED: " + startup
	finally:
		f.close()
	if not os.path.exists(i):
		os.makedirs(i)
		print print "CREATED: " + i + "/"
