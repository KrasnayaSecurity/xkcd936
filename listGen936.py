#!/usr/bin/python
import itertools
from lib.wordList import words

for l in range(1,4):
	combo = itertools.permutations(words, l);
	for i in combo:
		file = open('phraselist.txt', 'a');
		file.write(''.join(i)+'\n');
		file.close();
