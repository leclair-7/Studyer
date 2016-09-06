'''
This file reader function decides how the class notes are
to be put into a file

To Implement:
	- make this work on the line level instead of the file level
	- modularity

this is to generate flash cards, 

steps
	1 detect whichone
			-term '\t' def
			-term '-' def
			-term '\n' def (like a title with paragraph under it)
			-term ':' def
						
	2 what to do ith each
'''

def fileDecider(filename):
	'''
	fileDecider will return 0 for
					 return 1 for
					 return 2 for
	'''
	with open(filename,'r') as ofo:
		for line in ofo:
			for i in line:
				if i == '\t':
					#term tab file mode
					return 0
					pass
				elif i == '-':
					#term then dash file read mode
					return 1
					pass
				elif i == ':':
					return 2
					pass
				elif i=='\n':
					#term with paragraph under it 
					return 3
				else:
					continue
			print(line)
			
def termThenTab(filename, selectorNum):
	'''
	@param num
	'''
	aDict = {}
	notesDelimiter = '\t'

	if selectorNum == 0:
		notesDelimiter = '\t'
	elif selectorNum == 1:
		notesDelimiter = '-'
	elif selectorNum == 2:
		notesDelimiter = ':'
	elif selectorNum == 3:
		notesDelimiter = '\n'
	
	with open(filename,'r') as ofo:
		for line in ofo:
			if line == '\n':
				continue
			else:
				tabpos = line.find( notesDelimiter )
				aDict[line[:tabpos] ] = line[tabpos + 1:].strip()				
	return aDict

if __name__=='__main__':
	#print( fileDecider( "tabspaced.txt") )
	#print( fileDecider( "termdash.txt") )
	#print( fileDecider( "termparagraph.txt"))
	#s1 = "and	then......then..."
	
	#print(termThenTab("tabspaced.txt", fileDecider("tabspaced.txt")) )
	
	#this one doesn't work
	#print(termThenTab("termparagraph.txt", fileDecider("termparagraph.txt")) )
	
	with open("termparagraph.txt",'r') as ofo:
		for line in ofo:
			for i in line:
				if i == '\n':
					print("!")

	#print(termThenTab("termdash.txt", fileDecider("termdash.txt")) )
	#print(termThenTab("colonthendef.txt", fileDecider("colonthendef.txt")) )