#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv
import codecs

marks = { 
	u'Jeles'	: 5,
	u'Jó'	: 4,
	u'Közepes'	: 3,
	u'Elégséges'	: 2,
	u'Elégtelen'	: 1, 
	u'Elhagyott' : 0
}

def replacecomma(text):
	newText = ''
	for line in text.split('\n'):
		insideQuote = False
		for char in line:
			if char == '"':
				insideQuote = not insideQuote
			else :
				if char == ',' and not insideQuote:
					char = '#'
			newText += char
		newText += '\n'

	return newText
	
def getVal(text):
	pairs = []
	for line in text.split('\n'):
		line = line.split('#')
		if len(line) > 7:
			mark = line[7].split(' ')[0]
			if mark == '' :
				print line[1].split(',')[0][1:] , u'- nincs szerzett érdemjegy'
				pairs.append( (int(line[2]),marks[u'Elhagyott']))
			else:
				pairs.append( (int(line[2]),marks[mark]) )
	return pairs

def calculateKI( kj ):
	szumma = 0
	for subject in kj:
		szumma += subject[0]*subject[1]
	return ( float(szumma) / 30 )

def calculateKKI( kj ):
	felvettkredit = 0
	teljeskredit = 0
	for subject in kj:
		felvettkredit += subject[0]
		if subject[1] > 0 :
			teljeskredit += subject[0]
	return calculateKI(kj) * ( float(teljeskredit) / float(felvettkredit) )

	
def process( path ):
	file = codecs.open(path , "r" , "utf-8")
	file.readline()
	content = file.read()
	content = replacecomma(content)
	#print path
	#print content
	kreditJegy = getVal(content)
	#print kreditJegy
	print u'Kreditindex:', calculateKI ( kreditJegy )
	print u'Korrigált kreditindex:', calculateKKI ( kreditJegy )
	
#print marks

if len(argv) > 1 :
	file = argv[1]
	#print file
	process(file)
else:
	print 'Usage: atlag.py <file>'
	print '\twhere <file> should be the path to a .csv file (or well any file, if it\'s comma-separated and is in the same format...)'
	
