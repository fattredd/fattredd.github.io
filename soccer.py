import json,urllib2
resp=urllib2.urlopen('http://worldcup.sfg.io/matches').read()
for jogo in json.loads(resp.decode('utf-8')):
	if jogo['status'] == 'completed' or jogo['status'] == 'in progress':
		if jogo['status']=='in progress':
			print '\nRight now:'
		print jogo['home_team']['country'], jogo['home_team']['goals'], 'x', jogo['away_team']['goals'], jogo['away_team']['country']
