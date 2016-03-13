# ATM Simulator

## Description

This is an ATM Simulator developed by *Vafeiadis Panagiotis*.
The application simulates the Backend logic of a cash dispensing Automatic Teller Machine (ATM). 
It supports only $20 and $50 notes. The system dispenses only legal combinations of notes. If a request cannot be satisfied due to failure to find a suitable combination of notes, it reports an error condition.

## Install dependencies

If you are on a Mac or Linux machine, you probably already have Python installed. In this project 
we use Python 2.7.10.
We need to make sure though that we install pip and virtualenv for the correct version of Python on your computer. Open a terminal and run the following command:

```
$ sudo easy_install virtualenv
```

We clone the repository :

```
$ git clone https://github.com/PanioVaf/atmsim.git
```

We are creating a virtual enviroment in order to install the dependencies locally.


```
$ cd atmsim/
$ virtualenv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

## How to Run

To command to run the **atmsim** is given below. 
The user has to specify the number of twenty and fifty dollar notes as command line arguments.

```
$ python atmsim --twenty_notes 5 --fifty_notes 20
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


## Design
```
              +-----------------+
              |                 |
           ++ |    ATM MODEL    | <+
           |  |                 |  |
           |  +-----------------+  |
           |                       |
           |                       |
       UPDATES                 MANIPULATES
           |                       |
           |                       |
           |                       |
           v                       |

+------------------+      +------------------+
|                  |      |                  |
|    ATM VIEWER    |      |  ATM CONTROLLER  |
|                  |      |                  |
+------------------+      +------------------+

           +                        ^
           |                        |
      SEES |                        | USES
           |                        |
           |       +--------+       |
           |       |        |       |
           +-----> |  USER  | +-----+
                   |        |
                   +--------+

```





