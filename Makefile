NUM_NOTES_TWENTY?=10
NUM_NOTES_FIFTY?=20

help:
	python atmsim -h

init:
	pip install -r requirements.txt

run:
	python atmsim --twenty_notes ${NUM_NOTES_TWENTY} --fifty_notes ${NUM_NOTES_FIFTY}

test:
	nosetests tests