#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Formats the name of a file of downloaded research paper / book.

Created on 2023-06-20 00:21:11

@author: Shailendra K Rathor

Usage:
Enable execution permission (i.e., $ chmod +x format_filename.py,  on linux terminal). Add the file path to environment variable PATH. Rename
the intended file using the following command following the instructions
$ format_filename.py file_to_rename.pdf

Or put this file in the same directory where the file to rename is kept.
$ ./format_filename.py file_to_rename.pdf
or
$ python format_filename.py file_to_rename.pdf

"""


import os
import sys
import shutil

# Path to main library
library_dir = os.path.expanduser('~/')+'main_library/'
os.makedirs(library_dir, exist_ok=True)

# Path to save research articles
article_dir = library_dir + 'articles/'
os.makedirs(article_dir, exist_ok=True)

# Path to save books
book_dir = library_dir + 'books/'
os.makedirs(book_dir, exist_ok=True)

input_file = sys.argv[1]
if os.path.isfile(input_file):
	print(f"File exists...")
else: 
	print(f"File {input_file} does not exist. Exiting... ")
	sys.exit()

print(f"Is it an ARTICLE (Y|n)")
doc_type = input()

if doc_type == "Y" or doc_type == "":
	print(f"Enter first AUTHOR name:")
	a = input()
	
	print(f"SINGLE author? (N|y)")
	n = input()

	print(f"Enter YEAR of publication:")
	y = input()

	print(f"Enter name of JOURNAL:")
	j = input()

	print(f"Enter TITLE of the paper:")
	lines = []
	while True:
		line = input()
		if line:
			lines.append(line)
		else:
			break
	#  print(lines)
	t = ' '.join(lines)

	s = t.lower()
	words = s.split(' ')
	word_list = [word.title() for word in words]
	title = '_'.join(word_list)

	if n == "N" or n == "":
		final_list = [a, "etal", y, j]
	elif n == "y":
		final_list = [a, y, j]

	final_name = '_'.join(final_list)

	output_file =  final_name + '-' + title + '.pdf'
	shutil.copy2(input_file, output_file)

	os.rename(input_file, article_dir + output_file)
	# ~ os.link(input_file, output_file) # Creates hard link
	
	print(f"File renamed to {output_file}, and one copy is put in {article_dir}")


elif doc_type == "n":
	print(f"Enter first AUTHOR name:")
	a = input()

	print(f"Enter TITLE of the book:")
	lines = []
	while True:
		line = input()
		if line:
			lines.append(line)
		else:
			break
	#  print(lines)
	t = ' '.join(lines)

	s = t.lower()
	words = s.split(' ')
	word_list = [word.title() for word in words]
	title = '_'.join(word_list)

	final_list = [a, title]

	final_name = '-'.join(final_list)

	output_file =  final_name+'.pdf'
	shutil.copy2(input_file, output_file)

	os.rename(input_file, book_dir + output_file)
	# ~ output_file = library_dir + "/books/" + final_name+'.pdf'
	# ~ os.link(input_file, output_file) # Creates hard link

	print(f"File renamed to {final_name+'.pdf'}, and one copy is put in {book_dir}")
