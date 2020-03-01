#!/usr/bin/python

from PIL import Image
from os import listdir
from os.path import isfile, join

found = 0

onlyfiles = [f for f in listdir('./pics') if isfile(join('./pics', f))]

keyword = raw_input('Enter a keyword for picture: ')

for picture in onlyfiles:
	if keyword in picture:
		print "./pics/" + picture
