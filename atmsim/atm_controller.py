# -*- coding: utf-8 -*-
# Exc!te HOLIDAYS
# Copyright (C) 2016  - Vafeiadis Panagiotis
# This is free software and you are welcome to redistibute it 
# under certain conditions.

import argparse

class Controller(object):

	def __init__(self, model, viewer):
		self.model = model
		self.viewer = viewer

	def run(self, init_balance_twenty_notes, init_balance_fifty_notes):
		model = self.model
		viewer = self.viewer

		model.set_balance(init_balance_twenty_notes, init_balance_fifty_notes)
		viewer.show_welcome()

		while True:
			input_amount = viewer.ask_amount()
			if self.userWantsQuit(input_amount):
				return 

			if not self.isValidAmount(input_amount):
				viewer.show_invalid_amount_error_message()
			else:
				amount = int(input_amount)
				transaction = model.withdraw(amount)
				viewer.show_transaction_status(transaction)
				viewer.show_balance(model)

	def userWantsQuit(self, user_input):
		return user_input.strip(' ').lower() == 'q'

	def isValidAmount(self, s):
	    try: 
	        amount = int(s)
	        return (amount >= 0)
	    except ValueError:
	        return False

	def parse_input_arg(self):
		parser = argparse.ArgumentParser(description='This is an ATM simulator')
		parser.add_argument('--twenty_notes', metavar='twenty_notes', type=self.validate_num_notes, 
			help='The number of notes with $20 value', required=True)
		parser.add_argument('--fifty_notes', metavar='fifty_notes', type=self.validate_num_notes, 
			help='The number of notes with $50 value', required=True)
		args = parser.parse_args()
		return (args.twenty_notes, args.fifty_notes)

	def validate_num_notes(self, value):
		ivalue = int(value)	
		if ivalue < 0:
			raise argparse.ArgumentTypeError("%s is an invalid number of notes" % value)
		return ivalue



