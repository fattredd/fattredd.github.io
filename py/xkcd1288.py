def goodNews(article, **kwargs):
	'''Magically make new stories interesting'''
	substitutions = [
		('witnesses','these dudes I know'),
		('allegedly','kinda probably'),
		('new study','tumblr post'),
		('rebuild','avenge'),
		('space','spaaace'),
		('google glass','virtual boy'),
		('smartphone','pokedex'),
		('electric','atomic'),
		('senator','elf-lord'),
		('car','cat'),
		('election','eating contest'),
		('congressional leaders','river spirits'),
		('homeland security','homestar runner'),
		('could not be reched for comment','is guilty and everyone knows it')]
	debug = kwargs.get('debug', False)
	subs = kwargs.get('subs', None)
	if type(subs) == type([]) or type(subs) == type(()):
		if type(subs[0]) == type(()) or type(subs[0]) == type(()):
			for x in subs[0]:
				substitutions.append(x)
		elif type(subs[0]) == type(''):
			substitutions.append(subs)
	for word, replacement in substitutions:
		article = article.replace(word, replacement)
		if debug:
			print sub[0], 'replaced with', sub[1]
	return article
