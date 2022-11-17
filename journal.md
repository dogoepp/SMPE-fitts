# Laboratory Notebook for a user pointing experiment

## Project overview

Fitts described 1954 the relationship between the distance to a target, its width, and the time needed to acquire it [[Fitts, 1954](http://www2.psychology.uiowa.edu/faculty/mordkoff/InfoProc/pdfs/Fitts%201954.pdf)]. 
To aquire a target, e.g., to move the mouse cursor and click on a file to select it, Fitts' law describes how the distance between the start point and the target (_A_: amplitude of the movement), and the size of the target (_W_: width of the target) impacts the index of difficulty of the task (_ID_) [[MacKenzie and Buxton, 1992](http://www.billbuxton.com/fitts92.html)]:

> _ID_ = log2(_A_/_W_ + 1)

The time (_MT_: movement time) needed for a user to acquire a target is linearly correlated to _ID_:

> _MT_ = a + b × _ID_

A large part of Human-Computer Interaction research since then builds on top of Fitts' law.

This project aims at finding the values of the _a_ and _b_ parameters. This document contains my attempts to experimentally find _a_ and _b_ parameters.

## Experimental task

I used the implementation of a [pointing experiment from Ergonomics Web at Cornell University](http://ergo.human.cornell.edu/FittsLaw/FittsLaw.html).
On this Webpage, one can gather data for controlled 1D user pointing experiments.
1. In the first text field, the experimenter enters the _widths_ of the targets, separated with ','.
2. In the second text field, the experimenter enters the _distance_ between targets, also called "_amplitude_", separated with ','.
3. In the last text field, the experiment enters the number of trial s·he wants to collect for each combination of _widths_ and _distances_.

## Interrogations

Having performed a few initial experiments, we observe that having different screens and touchpads, Dorian and Clément might face different difficulty or easiness to perform the actions, as our devices might give us more or less pointing, or viewing accuracy.

We have also seen that the software does not compute the same regression coefficients as the ones we obtain from the tables.
It might be caused by the removing of errors in one of the dataset (the software does not show give that data).
The question of how we account for errors can be of importance, because if we simply remove them, then the subject is incentivised
to maximise speed over accuracy. On the opposite side, how to make the number/amplitude of errors have an impact?

For the following experiments, we choose to ask these questions:

- Can we reproduce Fitts' law with the parameters we chose?
- How do the different experiment parameters influence the coefficients of the linear regression of Fitts' law?
- Is Fitt's law stable over different experiments, all other (controlled) parameters kept the same?
- Is the linear model well suited?

## Parameters of influence

This experiment is about human-computer interaction. It might therefore be affected by several human factors, including:

- tiredness (also muscular fatigue, if too many experiences are run, the experimenter will probably experience some of it) and focus
- comfort with computers
- practice with the input method of choice (here mouse, touch pad or graphic tablet)
- practice with similar activities (for instance forst person shoot games)
- person's posture
- cursor shape on the screen
- is the person handicapped ?
- latency and accuracy of the system, from physical input to screen
- left-handedness or belonging to certain social class or ethnic group could also have an impact
- duration of the experience (number of trials per set, and number of different sets)
- the software used measures distances in pixels so the task might differ depending on the computer (screen) and (input) peripherals used (including whether they are absolute or relative).

We noticed also that during a set of measurements with same width and distance, there is a phenomenon aking to muscular learning. It means that we might measure the maximal speed at which a given person, at a given time, can repeatedly alternatively point at two fixed items. This approach does not measure the time to point at any random target. In that perspective, we should discard the first one or more observations of each set of measurements, as the person has to re-learn a movement.

Since we are dealing with humans, the behavior for extremely small/large or close/far areas of pointing might have an impact on performance. We however chose not to cover this aspect.

We could consider to run several experiments with different numbers of trials, to check whether it has an impact on performance.

## Choice of experiment parameters

Here are the parameters we choose to act upon:

- left-handedness (since the original experiment by Fitts was done with right-handed people)
- duration of the experience (number of trials per set, and number of different sets)
- enough different indices of difficulty so that the linear regression makes sense (used to be four)

We perform the experiments as two white males, MOSIG students (high education). One of us (Dorian) has been using the graphic tablet for about a month and the other (Clément) only once before.

Ideally we should use the same computer for the experiments, but the current setting does not allow us to do so. This is therefore an uncontrolled parameter.

The actual parameters are generated with 

- Widths: 5 values taken from a uniform repartition over [15, 250]
- Amplitudes: 5 values taken from a uniform repartition over [128, 1024]
- Trials fixed to 6
- Number of repetitions of the experiment: 2 per person
- Input device : Graphic tablet (for Dorian only) and Track pad

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

#### Dorian's first experiment

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

### 2022-11-14

We devised the experiment parameters described in the [Choice of experiment parameters](#choice-of-experiment-parameters) section above. These were realised in the file `exp_parameters/2022-11-14_experiences.csv` which we generated with `exp_parameters/parameters.py`.14_experiences

The related data is gathered in `raw_data` in the files dated today. For each individual, the experiments are performed in the order found in the csv file above.

There was an issue with the data of the first experiment, by Dorian. Due to an error in saving it, the data was lost. Dorian re-ran that experiment, but out of order. The resulting experiment summary file is `exp_parameters/2022-11-14_experiences_corrected.csv`, which also removes the experiments that Clément could not do (not having the graphic tablet at the time) and add file names.

### 2022-11-17

Due to software issues, Dorian pursued some analysis with Rstudio, whereas the former work had been done with Emacs + OrgMode + Babel + ... The related analysis and discussion is in `analysis/pointingAnalysis.Rmd` and has been also [converted to html](analysis/pointingAnalysis.html) for easy visualisation.