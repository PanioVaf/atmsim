# -*- coding: utf-8 -*-

from .context import atmsim
from atmsim import atm_model
from atmsim import atm_controller
from atmsim import atm_viewer
from nose.tools import assert_raises
import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    def test_check_amount(self):
    	notes_twenty  = 5
    	notes_fifty = 6
    	model = atmsim.atm_model.Model()
    	model.set_balance(notes_twenty, notes_fifty)
    	transaction = model.withdraw(180)
    	assert transaction["status"] == "success"
    	assert transaction["twenty_notes"] == 4
    	assert transaction["fifty_notes"] == 2
    
    def test_check_amount_invalid(self):
    	notes_twenty = 2
    	notes_fifty = 3
    	model = atmsim.atm_model.Model()
    	model.set_balance(notes_twenty, notes_fifty)
    	transaction = model.withdraw(500)
    	assert transaction["status"] == "failure"

    def test_check_negative_amount(self):
    	notes_twenty = 2
    	notes_fifty = 3
    	amount = -120
    	model = atmsim.atm_model.Model()
    	viewer = atmsim.atm_viewer.Viewer()
    	controller = atmsim.atm_controller.Controller(model, viewer)
    	isValid = controller.isValidAmount(amount)
    	assert isValid == False

    def test_check_valid_note(self):
    	notes_twenty = 2
    	notes_fifty = 3
    	notes_twenty_neg = -5
    	model = atmsim.atm_model.Model()
    	viewer = atmsim.atm_viewer.Viewer()
    	controller = atmsim.atm_controller.Controller(model, viewer)
    	assert controller.validate_num_notes(notes_twenty) == notes_twenty
    	assert controller.validate_num_notes(notes_fifty) == notes_fifty


    def test_user_quitting(self):
    	model = atmsim.atm_model.Model()
    	viewer = atmsim.atm_viewer.Viewer()
    	controller = atmsim.atm_controller.Controller(model, viewer)
    	str_quit = ['q', '  q', 'Q', 'Q ', ' q ']
    	for strr in str_quit:
    		assert controller.userWantsQuit(strr) == True

    def test_total_balance(self):
    	model = atmsim.atm_model.Model()
    	twenty_notes = [0, 3, 5]
    	fifty_notes = [0, 2, 5]
    	res = [(0,0,0), (100,0,2), (250,0,5), 
    	(60,3,0), (160,3,2), (310,3,5),
    	(100,5,0), (200,5,2),(350,5,5)]
    	i = 0
       	for note20 in twenty_notes:
    		for note50 in fifty_notes:
    			model.set_balance(note20, note50)
    			assert model.total_balance() == res[i]
    			i+=1


if __name__ == '__main__':
    unittest.main()
