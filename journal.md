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

## Experimental task

I used the implementation of a [pointing experiment from Ergonomics Web at Cornell University](http://ergo.human.cornell.edu/FittsLaw/FittsLaw.html).
On this Webpage, one can gather data for controlled 1D user pointing experiments.
1. In the first text field, the experimenter enters the _widths_ of the targets, seperated with ','.
2. In the second text field, the experimenter enters the _distance_ between targets, also called "_amplitude_", seperated with ','.
3. In the last text field, the experiment enters the number of trial s·he wants to collect for each combination of _widths_ and _distances_.

We observe that having different screens and touchpads, Dorian and Clément might face different difficulty or easiness to perform the actions, as our devices might give us more or less pointing, or viewing accuracy.

## Experimental Reports

### 2021-11-17

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

### 2022-11-10

#### Dorian's first epxeriment

Using the same software for data acquisition as before. Documentation on the experiment software: https://ergo.human.cornell.edu/FittsLaw/FittsLawInstructions.html

First attempt, Dorian, with trackpad of his own computer, on in files

- 20221110_1510_Dorian_RawData.csv
- 20221110_1510_Dorian_MeanMT.csv

The software also gives us:

Error: 7
MT = 650.777 + 112.811 x log(A/W + 1)
RSquare = 0.762

Notably, two observations in the first file have an unusually low Movement Time of 1 and 0 milliseconds.

Observing that we have only four different index of difficulty, it tells us little about the "actual" shape of the curve we would like to run experimants with more IDs.

#### Dorian's second experiment

This time, with graphic tablet, same computer

We observe that throughout the experiment, ove the ten iterations we can reach an almost automatic movement, but when transitioning to the next task, it starts slower. We should see how movement time evolves during a given sub-experiment with fixed set of targets.

Time of observation: 16:19

Widths: 16,32,64,128,256

Amplitudes: 128,256,512,1024

Trials: 10

#### Clement's second experiment

This time, with graphic tablet, Dorian's computer. He is novice with graphic tablet

Time of observation: 16:31

Widths: 16,32,64,128,256

Amplitudes: 128,256,512,1024

Trials: 10
