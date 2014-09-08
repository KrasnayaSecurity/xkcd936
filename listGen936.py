#!/usr/bin/python
import itertools
from lib.wordList import words
########################################
#   Configuration                      #
########################################
#maxLen = 4

########################################

maxLen = input("What is the maximum number of words that you would like in the string? ")
printFile = raw_input("Print a wordlist to file? (y/n) ")

if printFile == 'n':
	raw_input("Enter an XKCD 936 compliant password to match: ")

for l in range(1,maxLen):
	combo = itertools.permutations(words, l)
	for i in combo:
		if printFile == 'y':
			file = open('phraselist.txt', 'a')
			file.write(''.join(i)+'\n')
			file.close()
		else:
			print "".join(i)+'\n'
