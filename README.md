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

The commands to run the **atmsim** is given below. 
The user has to specify the number of twenty and fifty dollar notes as command line arguments.

```
$ source .env/bin/activate
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

The main design pattern is MVC (Model - View - Controller).
For the Viewer Class we are using the command line screen.
For the Controller we are using the keyboard. 
In this design we can replace the ATM VIEWER and CONTROLLER with different classes, for example to support a WEB app.

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

## Testing

### Lettuce Framework

We are using a behavior driven framework named [Lettuce](http://lettuce.it/) for the high level tests.

The common BDD approach basically consists in:
* writing some unit tests
* running these tests
* making these tests fail
* writing code
* making the code pass these tests (green status)

Lettuce provide to the developers the ability of describing features in a natural language, 
by creating one or more scenarios. Each scenario has one possible behaviour of the feature you want to implement. To make the scenarios run python code, it is necessary to define steps.
We are running the behaviour driven tests executing the command below.

```
$ cd tests
$ lettuce
```

### Nose Framework

For the unit tests, we are using the framework [Nose](https://nose.readthedocs.org/en/latest/).
We are running the unit tests executing the command below.

```
$ nosetests tests
```

