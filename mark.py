import os
import markdown2

extras = ['fenced-code-blocks', 'metadata', 'wiki-tables']

def convert(file):
	text = ""
	f = open(file, 'rb')
	for l in f:
		text = text + l
	f.close()
	marker = markdown2.markdown(text, extras=extras)
	return marker