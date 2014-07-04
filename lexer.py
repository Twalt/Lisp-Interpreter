#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
def lexer():
	Symbols = ['\\', ';', ':', '(', ')', '\'', '\"', ' ', '[', ']', '+', '.', '/', '*', '-']
	file = open('input.txt')
	lines = file.readlines()
	file.close
	letter = []
	for l in lines:
		k = list(l)
		for x in k:
			letter.append(x)
	words = []
	word = ""
	for le in letter:
		if le not in Symbols:
			word += le
		else:
			if le != ' ':
				words.append(word)
				word = le
				words.append(word)
				word = ""
			else:
				words.append(word)
				word = ""
	if word != "":
		words.append(word)
	for w in words:
		print(w)
		
lexer()