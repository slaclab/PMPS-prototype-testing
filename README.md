# PMPS Prototype Tests
L2S-I's PMPS system must be able to respond rapidly to a variety of complex states and inputs. In order to design a system that meets these high demands,s We will need accurate knowledge of our current hardware's performance to determine it's suitability for L2S-I.

To investigate, we will run tests on prototypes of the future hardware to measure it's performance under the load we expect it to endure. This repository collects the source code for the experiments. The folders in the main directory are each devoted to a single experiment. They contain the source code required to perform the experiment, documentation of the experiment and notes.

Thus far, the experiments focus on Beckhoff components, development with the TwinCAT 3 development environment, and Renishaw BISS-C Encoders. 

## Repository organization
Individual tests are sectioned off into separate directories. Each contains the TwinCAT project(s) required for running the necessary tests as well as a README.md detailing test usage and results. Additional files may be included for documenting results

## Documenting results 
Each test directory's README.md will have at minimum:
```markdown

# Experiment Title
Short intro

## Goal/Question
Objective of experiment

## Required components 
bulleted list

## Test with date, name optional

### Intro (optional)
Describe goal of specific test or any variations in this test if necessary.

### Setup
Setup including measuring tools. 

#### PLC Components in order, left to right
ordered list of beckhoff components

### Results
Observed results, data

### Discussion
Analysis, conclusions, and notes.

```
