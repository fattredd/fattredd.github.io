# shuffle analyzer
def shuffle(deck, piles=5, times=1, disp=False):
	'''
	Hard shuffle your deck
	deck - list of cards
	piles=5 - piles to hard shuffle into
	times=1 - repeat how many times
	disp=False - if True, print result, otherwise return it
	'''
	out = []
	for time in range(times):
		pile = []
		for x in range(piles):
			pile.append([])
		for num, card in enumerate(deck):
			pile[num%piles].append(card)
		out = joinLists(pile)
	if disp:
		ppDeck(out)
	else:
		return out

def joinLists(l):
	'''
	Join a list of lists into a single list.
	'''
	out = []
	for pile in l:
		for card in pile:
			out.append(card)
	return out

def createDeck(**kwargs):
	'''
	Accepts numbers for the following types of cards:
	\t-land
	\t-instant
	\t-sorcery
	\t-creature
	'''
	if 'land' in kwargs:
		land = kwargs['land']
	else:
		land = 0
	if 'instant' in kwargs:
		instant = kwargs['instant']
	else:
		instant = 0
	if 'sorcery' in kwargs:
		sorcery = kwargs['sorcery']
	else:
		sorcery = 0
	if 'creature' in kwargs:
		creature = kwargs['creature']
	else:
		creature = 0
	total = land + instant + sorcery + creature
	deck = []
	for card in range(total):
		out = str(card) + ' - '
		if card < land:
			out += 'land'
		elif card < land + instant:
			out += 'instant'
		elif card < land + instant + sorcery:
			out += 'sorcery'
		elif card < land + instant + sorcery + creature:
			out += 'creature'
		deck.append(str(out))
	return deck

def ppDeck(allEm):
	import sys
	out = '\n'.join(allEm)
	sys.stdout.write(out)
	sys.stdout.flush()
	#print(out)

if __name__ == '__main__':
	import sys, argparse
	parser = argparse.ArgumentParser(description='Grab them cards')
	parser.add_argument('land', metavar='LANDS', type=int)
	parser.add_argument('instant', metavar='INSTANT', type=int)
	parser.add_argument('sorcery', metavar='SORCERY', type=int)
	parser.add_argument('creature', metavar='CREATURE', type=int)
	parser.add_argument('piles', type=int, metavar='PILES')
	parser.add_argument('times', type=int, metavar='TIMES')
	parser.set_defaults(land=0,instant=0,sorcery=0,creature=0,
						piles=5,times=1)
	args = parser.parse_args()
	deck = createDeck(land=args.land,instant=args.instant,
					sorcery=args.sorcery, creature=args.creature)
	sys.stdout.write('''\n\
	**************
	** Original **
	**************\n\n''')
	sys.stdout.flush()
	ppDeck(deck)
	deck2 = shuffle(deck, args.piles, args.times)
	sys.stdout.write('''\n\n\
	**************
	** Shuffled **
	**************
	Into %s piles, and shuffled %s times\n\n
	'''%(args.piles,args.times))
	sys.stdout.flush()
	ppDeck(deck2)