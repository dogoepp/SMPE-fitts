# Laboratory Notebook for a user pointing experiment

## Project overview

Fitts described 1954 the relationship between the distance to a target, its width, and the time needed to acquire it [[Fitts, 1954](http://www2.psychology.uiowa.edu/faculty/mordkoff/InfoProc/pdfs/Fitts%201954.pdf)]. 
To aquire a target, e.g., to move the mouse cursor and click on a file to select it, Fitts' law describes how the distance between the start point and the target (_A_: amplitude of the movement), and the size of the target (_W_: width of the target) impacts the index of difficulty of the task (_ID_) [[MacKenzie and Buxton, 1992](http://www.billbuxton.com/fitts92.html)]:

> _ID_ = log2(_A_/_W_ + 1)

The time (_MT_: movement time) needed for a user to acquire a target is linearly correlated to _ID_:

> _MT_ = a + b × _ID_

A large part of Human-Computer Interaction research since then builds on top of Fitts' law.

This project aims at finding the values of the _a_ and _b_ parameters. This document contains my attempts to experimentally find _a_ and _b_ parameters.

## General Organization

### data/

This folder contains both raw and processed experimental data that is returned from the experimental software. 
Each file name is named after the following format: `YYYYMMDD_HHMM_<data>` where `<data>` is either:
- `RawData`, i.e. the raw data  as returned from the experimental software. 
- `MeanMT`, i.e. the processed mean movement times as returned from the experimental software. 

### analysis/

This folder contains my R markdown script used to analyze the data collected from the experiment. 

## Experimental Reports

### 2021-11-17

#### Experimental task

I used the implementation of a [pointing experiment from Ergonomics Web at Cornell University](http://ergo.human.cornell.edu/FittsLaw/FittsLaw.html). 
On this Webpage, one can gather data for controlled 1D user pointing experiments. 
1. In the first text field, the experimenter enters the _widths_ of the targets, seperated with ','. 
2. In the second text field, the experimenter enters the _distance_ between targets, also called "_amplitude_", seperated with ','. 
3. In the last text field, the experiment enters the number of trial s·he wants to collect for each combination of _widths_ and _distances_. 

#### Experimental variables

I ran the experiment from the above Webpage with 1, 2 and 4 widths and with 16, 32 and 64 distances, with 6 trials for each combination. 

#### Data collected

The Webpage returned the following results:
- I performed 4 pointing errors
- A Fitts modelling in the form of _MT_ = 1001.293 + 140.589 × log(A/W + 1) with R2 = 0.218
- The [table of mean _MT_](./data/20211117_1527_MeanMT.csv) that I provide in the [data folder](./data/)
- The [table of raw pointing data](./data/20211117_1527_RawData.csv) that I provide in [data folder](./data/)

#### Data analysis

My data analysis is performed and commented in the [pointingAnalysis.Rmd file](./analysis/pointingAnalysis.Rmd) (R markdown file). 
