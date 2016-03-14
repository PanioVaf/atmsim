# -*- coding: utf-8 -*-
# Exc!te HOLIDAYS
# Copyright (C) 2016  - Vafeiadis Panagiotis
# This is free software and you are welcome to redistibute it 
# under certain conditions.

import threading

class Model(object):
	"""This class represents the ATM's current balance.

    This Class is Thread-safe.
  
    """
	def __init__(self):
		self.lock = threading.Lock()
		self.set_balance()

	def set_balance(self, balance_twenty=0, balance_fifty=0):
		self.lock.acquire()
		self.twenty_notes = balance_twenty
		self.fifty_notes = balance_fifty
		self.lock.release()
        
	def balanced_tuple(self, lista):
		"""
		We use this function to pick the balanced combinations of $20 and $50 notes.
		This function is accepting as input a list of tuples where the first element is 
		the number of $20 notes and the second element of the tuple is the number of $50 
		notes. Returns the tuple that has the minimum absolute difference between the number
		of $20 and $50 notes.  
		"""
		if not lista:
			raise ValueError('The list is empty')
		min_tuple_x, min_tuple_y = lista[0] 
		min_abs_diff = abs(min_tuple_x - min_tuple_y)
		for x, y in lista:
			if abs(x - y) <= min_abs_diff:
				min_tuple_x = x
				min_tuple_y = y
				min_abs_diff = abs(x - y)
		return (min_tuple_x, min_tuple_y)

	def withdraw(self, amount):
		""" 
		(20 * notes_20) + (50 * notes_50) = amount

		This function is trying to withdraw the input `amount`.
		
		If the transaction is successful then it returns:
		- "status": "success", 
		- "total": total amount witdrawn, 
		- "twenty_notes": the number of $20 notes, 
		- "fifty_notes": the number of $50 notes
		The total balance is updated accordigly.

		If it is not possible to witdraw the specific amount it returns:
		- "status": "failure" 
		The total balance, the number of $20 and $50 are NOT changed.

		"""				
		self.lock.acquire()

		combinations = []
		range_fifty = min(amount / 50, self.fifty_notes)
		for notes50 in range(1 + range_fifty):
			notes20 = (amount - notes50 * 50) / 20			
			if notes20 >= 0 and notes20 <= self.twenty_notes:
				
				if 20 * notes20 + 50 * notes50 == amount:
					combinations.append((notes20, notes50))
		if not combinations:
			result = self.failed_transaction()
		else:
			notes20, notes50  = self.balanced_tuple(combinations)
			self.twenty_notes -= notes20
			self.fifty_notes -= notes50
			result = self.successful_transaction(amount, notes20, notes50)
		
		self.lock.release()
		return result

	def total_balance(self):
		self.lock.acquire()
		total = (self.twenty_notes * 20) + (self.fifty_notes * 50)
		result = (total, self.twenty_notes, self.fifty_notes)
		self.lock.release()
		return result

	def successful_transaction(self, total, twenty_notes, fifty_notes):
		return {"status": "success", "total": total, "twenty_notes": twenty_notes, "fifty_notes": fifty_notes}

	def failed_transaction(self):
		return {"status": "failure", "total": 0, "twenty_notes": 0, "fifty_notes": 0}

	











