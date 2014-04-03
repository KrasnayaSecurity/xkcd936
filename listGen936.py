#!/usr/bin/python
import itertools
from lib.wordList import words

print words;

for l in range(1,4):
	combo = itertools.permutations(words, l);
	for i in combo:
		print ''.join(i)
