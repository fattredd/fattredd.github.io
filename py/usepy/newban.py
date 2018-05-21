'''
Compilation of banner.py, master.py, and printBan.py
'''
import sys, pickle, argparse

letterforms = '''\
       |       |       |       |       |       |       | |
  ###  |  ###  |  ###  |   #   |       |  ###  |  ###  |!|
  #  # |  #  # |  #  # |       |       |       |       |"|
  # #  |  # #  |#######|  # #  |#######|  # #  |  # #  |#|
 ##### |#  #  #|#  #   | ##### |   #  #|#  #  #| ##### |$|
###   #|# #  # |### #  |   #   |  # ###| #  # #|#   ###|%|
  ##   | #  #  |  ##   | ###   |#   # #|#    # | ###  #|&|
  ###  |  ###  |   #   |  #    |       |       |       |'|
   ##  |  #    | #     | #     | #     |  #    |   ##  |(|
  ##   |    #  |     # |     # |     # |    #  |  ##   |)|
       | #   # |  # #  |#######|  # #  | #   # |       |*|
       |   #   |   #   | ##### |   #   |   #   |       |+|
       |       |       |  ###  |  ###  |   #   |  #    |,|
       |       |       | ##### |       |       |       |-|
       |       |       |       |  ###  |  ###  |  ###  |.|
      #|     # |    #  |   #   |  #    | #     |#      |/|
  ###  | #   # |#     #|#     #|#     #| #   # |  ###  |0|
   #   |  ##   | # #   |   #   |   #   |   #   | ##### |1|
 ##### |#     #|      #| ##### |#      |#      |#######|2|
 ##### |#     #|      #| ##### |      #|#     #| ##### |3|
#      |#    # |#    # |#    # |#######|     # |     # |4|
#######|#      |#      |###### |      #|#     #| ##### |5|
 ##### |#     #|#      |###### |#     #|#     #| ##### |6|
###### |#    # |    #  |   #   |  #    |  #    |  #    |7|
 ##### |#     #|#     #| ##### |#     #|#     #| ##### |8|
 ##### |#     #|#     #| ######|      #|#     #| ##### |9|
   #   |  ###  |   #   |       |   #   |  ###  |   #   |:|
  ###  |  ###  |       |  ###  |  ###  |   #   |  #    |;|
    #  |   #   |  #    | #     |  #    |   #   |    #  |<|
       |       |#######|       |#######|       |       |=|
  #    |   #   |    #  |     # |    #  |   #   |  #    |>|
 ##### |#     #|      #|   ### |   #   |       |   #   |?|
 ##### |#     #|# ### #|# ### #|# #### |#      | ##### |@|
   #   |  # #  | #   # |#     #|#######|#     #|#     #|A|
###### |#     #|#     #|###### |#     #|#     #|###### |B|
 ##### |#     #|#      |#      |#      |#     #| ##### |C|
###### |#     #|#     #|#     #|#     #|#     #|###### |D|
#######|#      |#      |#####  |#      |#      |#######|E|
#######|#      |#      |#####  |#      |#      |#      |F|
 ##### |#     #|#      |#  ####|#     #|#     #| ##### |G|
#     #|#     #|#     #|#######|#     #|#     #|#     #|H|
  ###  |   #   |   #   |   #   |   #   |   #   |  ###  |I|
      #|      #|      #|      #|#     #|#     #| ##### |J|
#    # |#   #  |#  #   |###    |#  #   |#   #  |#    # |K|
#      |#      |#      |#      |#      |#      |#######|L|
#     #|##   ##|# # # #|#  #  #|#     #|#     #|#     #|M|
#     #|##    #|# #   #|#  #  #|#   # #|#    ##|#     #|N|
#######|#     #|#     #|#     #|#     #|#     #|#######|O|
###### |#     #|#     #|###### |#      |#      |#      |P|
 ##### |#     #|#     #|#     #|#   # #|#    # | #### #|Q|
###### |#     #|#     #|###### |#   #  |#    # |#     #|R|
 ##### |#     #|#      | ##### |      #|#     #| ##### |S|
#######|   #   |   #   |   #   |   #   |   #   |   #   |T|
#     #|#     #|#     #|#     #|#     #|#     #| ##### |U|
#     #|#     #|#     #|#     #| #   # |  # #  |   #   |V|
#     #|#  #  #|#  #  #|#  #  #|#  #  #|#  #  #| ## ## |W|
#     #| #   # |  # #  |   #   |  # #  | #   # |#     #|#|
#     #| #   # |  # #  |   #   |   #   |   #   |   #   |Y|
#######|     # |    #  |   #   |  #    | #     |#######|Z|
 ##### | #     | #     | #     | #     | #     | ##### |[|
#      | #     |  #    |   #   |    #  |     # |      #|\|
 ##### |     # |     # |     # |     # |     # | ##### |]|
   #   |  # #  | #   # |       |       |       |       |^|
       |       |       |       |       |       |#######|_|
       |  ###  |  ###  |   #   |    #  |       |       |`|
       |   ##  |  #  # | #    #| ######| #    #| #    #|a|
       | ##### | #    #| ##### | #    #| #    #| ##### |b|
       |  #### | #    #| #     | #     | #    #|  #### |c|
       | ##### | #    #| #    #| #    #| #    #| ##### |d|
       | ######| #     | ##### | #     | #     | ######|e|
       | ######| #     | ##### | #     | #     | #     |f|
       |  #### | #    #| #     | #  ###| #    #|  #### |g|
       | #    #| #    #| ######| #    #| #    #| #    #|h|
       |    #  |    #  |    #  |    #  |    #  |    #  |i|
       |      #|      #|      #|      #| #    #|  #### |j|
       | #    #| #   # | ####  | #  #  | #   # | #    #|k|
       | #     | #     | #     | #     | #     | ######|l|
       | #    #| ##  ##| # ## #| #    #| #    #| #    #|m|
       | #    #| ##   #| # #  #| #  # #| #   ##| #    #|n|
       |  #### | #    #| #    #| #    #| #    #|  #### |o|
       | ##### | #    #| #    #| ##### | #     | #     |p|
       |  #### | #    #| #    #| #  # #| #   # |  ### #|q|
       | ##### | #    #| #    #| ##### | #   # | #    #|r|
       |  #### | #     |  #### |      #| #    #|  #### |s|
       |  #####|    #  |    #  |    #  |    #  |    #  |t|
       | #    #| #    #| #    #| #    #| #    #|  #### |u|
       | #    #| #    #| #    #| #    #|  #  # |   ##  |v|
       | #    #| #    #| #    #| # ## #| ##  ##| #    #|w|
       | #    #|  #  # |   ##  |   ##  |  #  # | #    #|x|
       |  #   #|   # # |    #  |    #  |    #  |    #  |y|
       | ######|     # |    #  |   #   |  #    | ######|z|
  ###  | #     | #     |##     | #     | #     |  ###  |{|
   #   |   #   |   #   |       |   #   |   #   |   #   |||
  ###  |     # |     # |     ##|     # |     # |  ###  |}|
 ##    |#  #  #|    ## |       |       |       |       |~|
'''.splitlines()
table = {}
for form in letterforms:
	if '|' in form:
		table[form[-2]] = form[:-3].split('|')
ROWS = len(table.values()[0])

def horizontal(word):
	out = ''
	for row in range(ROWS):
		for c in word:
			out += table[c][row]
		out += '\n'
	return out

def vertical(word):
	out = ''
	for c in word:
		for row in zip(*table[c]):
			out += ' '.join(reversed(row))
		out += '\n'
	return out

def listPickle(banner):
	bannerL = banner.replace('\r','').split('\n')
	out = []
	for line in bannerL:
		pickledLine = []
		currentChar = ' '
		buffL = [currentChar,0]
		for char in line:
			if char == currentChar:
				buffL[1] += 1
			else:
				pickledLine.append((buffL[0],buffL[1]))
				currentChar = char
				buffL = [currentChar, 1]
		pickledLine.append((buffL[0],buffL[1]))
		out.append(pickledLine)
	return out

def pBan(data):
	out = ''
	for line in data:
		for char, count in line:
			out += char*count
		out += '\n'
	return out

def pLoad(fname):
	f = open(fname)
	out = pickle.loads(f.read())
	f.close()
	return out

if __name__ == '__main__':
 	parser = argparse.ArgumentParser(description =
 		'Do a bunch of banner stuff')
 	parser.add_argument('--text', type=str,
 			metavar='(default source)', dest='text',
 			option_strings=['-t','--text'])
 	parser.add_argument('--filein', type=str,
 			metavar='(alternate source)', dest='filein',
 			option_strings=['-fi','--filein'])
 	parser.add_argument('--fileout', type=argparse.FileType('w'),
 			option_strings=['-fo','--fileout'], dest='fileout',
 			metavar='default=stdout', default=sys.stdout)
 	parser.add_argument('--inputType', type=str,
 			metavar='{r,p}', dest='inputType',
 			default='r', choices=['r','p'],
 			option_strings=['-i','--input'])
	parser.add_argument('--outputType', type=str,
			metavar='{r,b,l,p}', dest='outputType',
 			default='b', choices=['r','l','b','p'], 
 			option_strings=['-o','--output'])
	parser.add_argument('--pprint', type=bool,
			dest='pp', default=False, const=True, nargs='?',
			option_strings=['-pp','-p','--pprint'])
	args = parser.parse_args()
	if args.filein:
		f = open(args.filein)
		text = f.read()
		f.close()
	elif args.text:
		text = args.text
	else:
		text = ''
		out = 'For more help use\n$ python %s -h\n\n'%sys.argv[0]
		sys.stdout.write(out)
	if not text == '':
		if args.outputType == 'r':
			if args.inputType == 'r':
				out = text
			elif args.inputType == 'p':
				data = pickle.loads(text)
				out = pBan(data)
		elif args.outputType == 'b':
			if args.inputType == 'p':
				data = pickle.loads(text)
				out = pBan(data)
			elif args.inputType == 'r':
				out = horizontal(text)
		elif args.outputType == 'p':
			if args.inputType == 'p':
				out = text
			elif args.inputType == 'r':
				data = horizontal(text)
				out = pickle.dumps(listPickle(data))
		elif args.outputType == 'l':
			if args.inputType == 'p':
				out = pickle.loads(text)
			elif args.inputType == 'r':
				out = listPickle(horizontal(text))
			else:
				out = text
		if args.pp:
			from pprint import pprint
			pprint(out)
		else:
			args.fileout.write(str(out))
			args.fileout.write('\n')
			args.fileout.close()