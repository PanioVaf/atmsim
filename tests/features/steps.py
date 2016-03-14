from lettuce import *
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
import atmsim
from atmsim import atm_model

	

@step('ATM has (\d+) notes of twenty dollars')
def have_num_twenty_notes(step, notes_twenty):
	world.notes_twenty = int(notes_twenty)

@step('ATM has (\d+) notes of fifty dollars')
def have_num_fifty_notes(step, notes_fifty):
	world.notes_fifty = int(notes_fifty)

@step('I try to withdraw (\d+) dollars')
def withdraw_amount(step, amount):
	world.amount = int(amount)
	world.transaction = world.model.withdraw(world.amount)

@step('ATM has been initialised with a deposit')
def initial_deposit(step):
	world.model = atmsim.atm_model.Model()
	world.model.set_balance(world.notes_twenty, world.notes_fifty)


@step('I see the message I cannot withdraw this amount')
def cannot_withdraw(step):
	assert world.transaction["status"] == "failure"
		

@step('ATM gives me (\d+) twenty notes and (\d+) fifty notes')
def successful_withdraw(step, notes_twenty, notes_fifty):
	notes_twenty = int(notes_twenty)
	notes_fifty = int(notes_fifty)
	assert world.transaction["twenty_notes"] == notes_twenty
	assert world.transaction["fifty_notes"] == notes_fifty
	assert world.transaction["total"] == (notes_twenty * 20) +(notes_fifty * 50)




