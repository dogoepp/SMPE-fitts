# Laboratory Notebook for a user pointing experiment

## Project overview

Fitts described 1954 the relationship between the distance to a target, its width, and the time needed to acquire it [[Fitts, 1954](http://www2.psychology.uiowa.edu/faculty/mordkoff/InfoProc/pdfs/Fitts%201954.pdf)]. 
To aquire a target, e.g., to move the mouse cursor and click on a file to select it, Fitts' law describes how the distance between the start point and the target (_A_: amplitude of the movement), and the size of the target (_W_: width of the target) impacts the index of difficulty of the task (_ID_) [[MacKenzie and Buxton, 1992](http://www.billbuxton.com/fitts92.html)]:

> _ID_ = log2(_A_/_W_ + 1)

The time (_MT_: movement time) needed for a user to acquire a target is linearly correlated to _ID_:

> MT = a + b × _ID_

This project aims at finding the values of the _a_ and _b_ parameters. This document contains my attempts to experimentally find _a_ and _b_ parameters.

## General Organization

### analysis/

### data/

## Experimental Reports

### 2021-11-17

I used the implementation of a pointing experiment from [http://ergo.human.cornell.edu/FittsLaw/FittsLaw.html](http://ergo.human.cornell.edu/FittsLaw/FittsLaw.html). 
On this Webpage, one can gather data for controlled user (1D) pointing experiments. 
1. In the first text field, the experimenter enters the _widths_ of the targets, seperated with ','. 
2. In the second text field, the experimenter enters the _distance_ between targets, called "_amplitude_", seperated with ','. 
3. In the last text field, the experiment enters the number of trial s·he wants to collect for each combination of _widths_ and _distance_. 
