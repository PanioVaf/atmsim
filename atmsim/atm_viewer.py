# -*- coding: utf-8 -*-
# Exc!te HOLIDAYS
# Copyright (C) 2016  - Vafeiadis Panagiotis
# This is free software and you are welcome to redistibute it 
# under certain conditions.

class Viewer(object):

	def show_balance(self, balance_model):
		print ("\nCurrent balance total: $%r twenty:%r  fifty:%r" % balance_model.total_balance())

	def show_welcome(self):
		print ("Welcome to Exc!te BANK\n")

	def ask_amount(self):
		input_amount = raw_input("Enter the amount to withdraw or 'q' to quit: ")
		return input_amount

	def show_invalid_amount_error_message(self):
		print ("Error: The amount should be positive integer")

	def show_transaction_status(self, transaction):
		if transaction["status"] == "success":
			print ("I am withdrawing Total: $%r (%r Twenty notes and %r Fifty notes)" % 
				(transaction["total"], transaction["twenty_notes"], transaction["fifty_notes"]))
		else:
			print ("I cannot withdraw this amount")
	