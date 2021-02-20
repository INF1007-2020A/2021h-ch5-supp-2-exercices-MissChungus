#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	for char in text:
		if char.isalnum() == False:
			text = text.replace(char, '')
	return len(text)

def get_word_length_histogram(text):
	for char in text:
		if char.isalnum() == False and char != ' ':
			text = text.replace(char, '')
	words = text.split()
	max = 0
	for word in words:
		if len(word) > max:
			max = len(word)
	histogram = [0 for length in range(max + 1)]
	for word in words:
		histogram[len(word)] += 1
	return histogram

def format_histogram(histogram):
	ROW_CHAR = "*"
	format = ''
	for i in range(1, len(histogram)):
		if i > 9:
			format += str(i) + ' ' + ROW_CHAR*histogram[i] + '\n'
		else:
			format += ' ' + str(i) + ' ' + ROW_CHAR * histogram[i] + '\n'

	return format

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	maximum = max(histogram)
	valeur = maximum
	compteur = 0
	forme = ''
	del histogram[0]
	while compteur < maximum:
		for i in range(len(histogram)):
			if histogram[i] + compteur == maximum:
				forme += BLOCK_CHAR
				histogram[i] -= 1
			else:
				forme += ' '
		compteur += 1
		valeur -= 1
		forme += '\n'
	forme += LINE_CHAR*(len(histogram)+1)
	return forme


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
