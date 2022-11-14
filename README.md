# M2R Pointing experiment

This small project aims at teaching 2nd year master students how to improve their experimental methodology.

The [journal](./journal.md) contains all information and experimental reports.

## General Organization

### data/

This folder contains both raw and processed experimental data that is returned from the experimental software. 
Each file name is named after the following format: `YYYYMMDD_HHMM_<data>` where `<data>` is either:
- `RawData`, i.e. the raw data  as returned from the experimental software. 
- `MeanMT`, i.e. the processed mean movement times as returned from the experimental software. 

### analysis/

This folder contains my R markdown script used to analyze the data collected from the experiment.