# -*- coding: utf-8 -*-
# Exc!te HOLIDAYS
# Copyright (C) 2016  - Vafeiadis Panagiotis
# This is free software and you are welcome to redistibute it 
# under certain conditions.

import atm_model
import atm_viewer
import atm_controller

def main():	
	model = atm_model.Model()
	viewer = atm_viewer.Viewer()
	controller = atm_controller.Controller(model, viewer)

	(twenty_notes, fifty_notes) = controller.parse_input_arg()

	controller.run(twenty_notes, fifty_notes)

if __name__ == '__main__':
    main()