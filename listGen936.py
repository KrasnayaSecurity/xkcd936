#!/usr/bin/python
import itertools
from lib.wordList import words
import time
import sys

maxLen = input("What is the maximum number of words that you would like in the string? ")
printFile = 'a'
password = 'a'
while (printFile != 'y') and (printFile != 'n'):
	printFile = raw_input("Print a wordlist to file? (y/n) ")

if printFile == 'n':
	password = raw_input("Enter an XKCD 936 compliant password to match: ")

start = time.time()
for l in range(1,maxLen+1):
	combo = itertools.permutations(words, l)
	for i in combo:
		if printFile == 'y':
			file = open('phraselist.txt', 'a')
			file.write(''.join(i)+'\n')
			file.close()
		else:
			word = "".join(i)
			if password == word:
				print "The password \""+ word +"\" was found.  Elapsed time: "+ str(time.time() - start)
				sys.exit()
