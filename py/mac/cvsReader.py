'''This is a script to read & display the contents of a csv file'''
from csv import reader, writer,Sniffer
file='restock.csv'

with open(file, 'rb') as csvfile:
	spamreader = reader(csvfile, delimiter=',')
	dialect=Sniffer().sniff(csvfile.read(1024))
	csvfile.seek(0)
	reader1 = reader(csvfile, dialect)
	print reader1
	#for row in spamreader:
		#print filter(', '.join(row))