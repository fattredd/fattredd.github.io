################
# Useful Funcs #
################
# Please note that I didn't write all of these scripts.
# I mearly assembled them. If you have a problem with
# your script being used/want credit, you can always
# email me at fattredd@gmail.com

import itertools
import sys
import time
import random
import os
import platform

def randInts():
	'''Uses sys.stdout.write() to produce a neverending stream of random
		numbers. Ctrl + C to stop.'''
	while True:
		sys.stdout.write(str(random.randint(0,9)))
		sys.stdout.flush()
		time.sleep(0.1)

def spin():
	'''A spinning icon. Ctrl + C to stop.'''
	for x in itertools.cycle('|\-/'):
		sys.stdout.write('\r' + x)
		sys.stdout.flush()
		time.sleep(0.1)

def phonetic(pword=''):
	'''Returns a string of the pword as phonetic'''
	if pword == '':
		pword = 'br549ZQR'
		print 'pword left blank. Using', pword, 'instead'
	spacer = " "    # character to use between words.
	dij = {'1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Niner', '0':'Zero'}
	alf = {'a':'alpha', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliet', 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 'z':'zulu'}
	pun = {'-': 'dash', '&': 'ampersand', '@': 'at-sign', '.': 'dot', ',': 'comma', '!': 'exclamation', 
		'#': 'pound', ':': 'colon', ';': 'semicolon', '%': 'percent', '*': 'asterisk', '$': 'dollar',
		'^': 'caret', '(': 'left-parens', ')': 'right-parens', '\\': 'backslash', '_': 'underbar',
		'-': 'minus', '+': 'plus', '=': 'equals', '{': 'left brace', '}': 'right brace', '[': 'left bracket',
		']': 'right bracket', '|': 'pipe', '"': 'double-quote', '<': 'less than', '>': 'greater than',
		'?': 'question', '/': 'forward slash', '\'': 'single quote', '~': 'tilde', '`': 'back quote', ' ': 'space' }  
	# print '\nPassword: ' + pword
	s = ''    # create a blank string
	for foo in pword:
		if foo.isdigit():
			s += dij[foo] 
		elif foo.islower():
			s += alf[foo] 
		elif foo.isupper():
			s += alf[foo.lower()].upper()
		else:
			try:
				s += '[' + pun[foo] + ']'
			except KeyError:
				s += '"' + foo + '"'
		s += spacer
	 # print '\nPhonetic: ' + s[:-1]
	return s[:-1]

colors = {'pink': '\033[95m',  #For use with stdout. Always end with color['black'] or 'res'
			'blue': '\033[94m',
			'green': '\033[92m',
			'yellow': '\033[93m',
			'red': '\033[91m',
			'black': '\033[0m',
			'res': '\033[0m'}

def showColors():
	'''Shows all possible colors to use with sys.stdout.write()'''
	i=0
	while i<110:
		sys.stdout.write('\033['+str(i)+'mABCDEFG - \\033['+str(i)+'m\033[0m\n')
		sys.stdout.flush()
		time.sleep(0.1)
		i+=1
	sys.stdout.write(colors['black'])

def otp(text,key,encrypting=1): 
	'''One Time Pad. ('text', listOfNum/range(), True if encrypting)'''
	return "".join([chr((ord(c)-ord('a')+i*(-1)**encrypting)%26 + ord('a'))\
		for c,i in zip(text,key)])

def cdh(d=''):
	'''Change the working directory relative to /home.
	Shortcuts:
		'.books':'jack/txt/books'
		'.txt':'jack/txt'
		'.jack':'jack'
		'.py':'jack/py'
		'.':''
		'/':'..'
		'':'jack'
	'''
	switch = {
		'.books':'jack/txt/books',
		'.txt':'jack/txt',
		'.jack':'jack',
		'.py':'jack/py',
		'.':'',
		'/':'..',
		'':'jack'
	}
	if d in switch.keys():
		d = switch[d]
	if platform.system() == 'Windows':
		path = 'C:\\cygwin64\\home'
		for folder in d.split('/'):
			path += '\\'+folder
		os.chdir(path)
	elif platform.system() == 'Linux':
		path = '/home/' + folder
		os.chdir(path)

def analyze(txt, dict={}):
	'''Analyze the letter distribution in a text. Returns a dict of
			the used letters in the form; dict[\'letter\']=amount
		txt - The string to be analyzed
		dict - The dictionary to add to. Not required.'''
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	for letter in txt:
		if letter.lower() in alphabet:
			if not letter.lower() in dict:
				dict[letter.lower()] = 1
			else:
				dict[letter.lower()] += 1
	return dict

def disp(dict, **kwargs):
	'''Create a graph from a dictionary that associates a key with an amount
		Accepted kwargs:
		\tcolor - default 'r'
		\twidth - default 0.25
		\tylabel - default 'amount'
		\ttitle - default 'Letter Breakdown\''''
	import numpy as np # Used only in disp()
	import matplotlib.pylab as plt # Used only in disp()
	if 'color' in kwargs:
		color = kwargs['color']
	else:
		color = 'r'
	if 'ylabel' in kwargs:
		ylabel = kwargs['ylabel']
	else:
		color = 'Amount'
	if 'width' in kwargs:
		width = int(kwargs['width'])
	else:
		width = 0.25
	if 'title' in kwargs:
		title = kwargs['title']
	else:
		title = 'Letter Breakdown'
	labels = dict.keys()
	data = []
	for num in labels:
		data.append(dict[num])
	N = len(labels)
	ind = np.arange(N)    # the x locations for the groups
	plt.bar(ind, data, width, color=color)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.xticks(ind+width/2., labels)
	plt.yticks(np.arange(0,max(data),max(data)/10))
	plt.show()

def dirAnalyze(dir='.'):
	'''Analyze .txt files in a directory'''
	masterDict={}
	if os.listdir('dir') == []:
		return {}
	for files in os.listdir(dir):
		if files.endswith('.txt'):
			with open(files) as f:
				content = f.read()
			masterDict = analyze(content, masterDict)
	return masterDict