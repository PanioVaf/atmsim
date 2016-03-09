# ATM Simulator

## Description

This is an ATM Simulator developed by *Vafeiadis Panagiotis*.
The application simulates the Backend logic of a cash dispensing Automatic Teller Machine (ATM). 
It supports only $20 and $50 notes. The system dispenses only legal combinations of notes. If a request cannot be satisfied due to failure to find a suitable combination of notes, it reports an error condition.

## Instructions - How to Run

The two ways to run the **atmsim** are given below. 
The user has to specify the number of twenty and fifty dollar notes as command line arguments.

```
$ python atmsim --twenty_notes 5 --fifty_notes 20
```
or,

```
$ make run NUM_NOTES_TWENTY=1 NUM_NOTES_FIFTY=2
```

## Show help

The user can show the help usage using the (-h) parameter.

```
$ python atmsim -h

usage: atmsim [-h] --twenty_notes twenty_notes --fifty_notes fifty_notes

This is an ATM simulator

optional arguments:
  -h, --help            show this help message and exit
  --twenty_notes twenty_notes
                        The number of notes with $20 value
  --fifty_notes fifty_notes
                        The number of notes with $50 value
```