# PMPS-prototype-testing
Repository for performance tests on beckhoff systems. Tests are intended to provide information about the limits and response rates of the beckhoff systems under various loads.

## Repository organization
Individual tests are sectioned off into separate directories. Each contains the TwinCAT project(s) required for running the necessary tests as well as a README.md detailing test usage and results. 

## Documenting results 
Each test directory's README.md will have at minimum:
```
# IO_delay experiment
Short intro

## Goal/Question
Objective of experiment

## Required components 
bulleted list

## Test with date, name optional
### Components in order, left to right
ordered list of beckhoff components

### Setup
Non-beckhoff setup including measuring tools. 

### Observed
Observed results

### Notes
Additional observations.

### Results
Short answer to goal/question
```

