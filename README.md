# ATM Simulator

## Description

This is an ATM Simulator developed by *Vafeiadis Panagiotis*.
The application simulates the Backend logic of a cash dispensing Automatic Teller Machine (ATM). 
It supports only $20 and $50 notes. The system dispenses only legal combinations of notes. If a request cannot be satisfied due to failure to find a suitable combination of notes, it reports an error condition.

## Instructions - How to Run

The two ways to run the atmsim are given below. 
The user has to specify the number of twenty and fifty dollar notes as command line arguments.

```
python atmsim --twenty_notes 5 --fifty_notes 20
```
or,

```
make run NUM_NOTES_TWENTY=1 NUM_NOTES_FIFTY=2
```

