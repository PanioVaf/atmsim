# Exc!te HOLIDAYS
# Copyright (C) 2016  - Vafeiadis Panagiotis
# This is free software and you are welcome to redistibute it 
# under certain conditions.


import argparse

 



def check_num_notes(value):
	ivalue = int(value)	
	if ivalue < 0:
		raise argparse.ArgumentTypeError("%s is an invalid number of notes" % value)
	return ivalue

def main():
	parser = argparse.ArgumentParser(description='This is an ATM simulator')
	parser.add_argument('--twenty_notes', metavar='twenty_notes', type=check_num_notes, 
		help='The number of notes with $20 value', required=True)
	parser.add_argument('--fifty_notes', metavar='fifty_notes', type=check_num_notes, 
		help='The number of notes with $50 value', required=True)
	args = parser.parse_args()
	print args.twenty_notes
	print args.fifty_notes


if __name__ == '__main__':
    main()

