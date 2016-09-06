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

	fileDecider will return 0 for term '\t' definition
					 return 1 for term '-' definition
					 return 2 for term ':' definition
					 return 3 for term '\n' definition
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
	print(selectorNum)

	if selectorNum ==3:
		with open(filename, 'r') as myfile:
			h = myfile.readlines()		

		assert len(h) % 2 == 0, "need 1-1 term to definition/description ratio for this to work"

		for i in range( int(len(h)/2)):
			index = i * 2
			aDict[h[index].strip() ] = h[index+1].strip()	
			if index > len(h)-1:
				break	

		return aDict	

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
	print(termThenTab("termparagraphTEST.txt", fileDecider("termparagraphTEST.txt")) )
	'''
	with open("termparagraphTEST.txt",'r') as ofo:
		for line in ofo:
			for i in line:
				if i == '\n':
					print("newline")
				else:
					print(i)
	
	with open('termparagraphTEST.txt', 'r') as myfile:
		lalista = myfile.readlines()
	print(len(lalista))
	'''
	#print(termThenTab("termdashTEST.txt", fileDecider("termdashTEST.txt")) )
	#print(termThenTab("colonthendefTEST.txt", fileDecider("colonthendefTEST.txt")) )