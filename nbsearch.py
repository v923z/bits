#!/usr/bin/python

import sys
import os
from search_class import NotebookSearch

def print_usage():
	print '\n\tUsage: nbsearch.py folder string [cell type]'
	print '\tcell type can be markdown, heading, raw, or code. Default is code'
	print '\tExample: nbsearch.py ./ search_string raw'
	print '\tExample: nbsearch.py ./ search_string code markdown\n'

if __name__ == "__main__": 
	
	if len(sys.argv) < 3:
		print_usage()
		sys.exit(1)

	folder = sys.argv[1]
	search_string = sys.argv[2]
	if len(sys.argv) == 3:
		cell_type = ['code']
	if len(sys.argv) > 3:
		cell_type = [sys.argv[i] for i in range(3, len(sys.argv))]
	
	for file in [file for file in os.listdir(folder) if file.endswith('.ipynb')]:
		nb = NotebookSearch(file)
		if nb.search_string(search_string, cell_type=cell_type) is True:
			print '%s: found %s'%(file, search_string)
		else:
			print '%s: not found %s'%(file, search_string)

