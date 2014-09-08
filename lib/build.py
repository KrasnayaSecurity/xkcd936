#!/usr/bin/python
module = open('words.txt', 'r');
for line in module:
	word = line;
	word = word.replace('\n', '');
	wordList = open('wordList.py', 'a');
	newLine = 'words.append(\''+word+'\');\n';
	wordList.write(newLine);
	wordList.close();
