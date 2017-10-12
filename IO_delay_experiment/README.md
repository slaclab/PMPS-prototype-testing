# IO_delay experiment
This project tests the response rate of the of a Beckhoff system. This setup awaits a high starter signal and responds with a high output signal. Starter signal produced by terminal on Beckhoff system. Data taken via external oscilloscope.

## Goal
Attempt to produce minimum delay for basic IO operations. Measure baseline performance provided from optimal settings.

## Required components 
- EL1124
- EL2124
- EK9505
- EL9186
- EL9187

## Test on 9-26-17


### Setup
Observed using Tektronix TDS 2024 oscilloscope monitoring starter and output signals. 

#### Components in order, left to right
0. CX2020
0. EL7041 (unused)
0. EL9186
0. EL9187
0. EK9505
0. EL2124
0. EL1124

### Results
100 us delay between starter and output with estimated jitter of ~20 us

### Discussion
Was not able to measure reliabilty of jitter. Must learn to perform measurments on math-constructed traces. Tests were first conducted with EL1124 with some dead terminals and later with more better EL1124. EL1124 substitution had no apparent effect on results.

## Update to test 9-26-17 on 10-2-17

### Intro
New osc. allows for precise measurments of delay timeings. Rerun study with better measuring tools for better data. Previous tests averaged several inputs to create traces and may have hidden timing violations from the min/max measurments. This test is run with hi-res acquire settings to prevent averaging.

### Setup
Now using Tektronix 784D oscilloscope in place of Tektronix TDS 2024. Measurments taken over 512 samples.

#### Components in order, left to right
Unchanged

### Results

Measurement | Result
:--------: | ------:
mean | 100.0+/-.1us
st. dev | 25+/-5us
min. | 99.6us
max. | 100.1us

### Discussion
Min and max indicate that the beckhoff is not taking additional/fewer cycles to complete computation. Cycle ount appears to be reliable. Cycle timing has very minor std. dev. of 20ns and mean very near advertised 100us. 

## Rerun of test on 10-3-17

### Intro
Rerun previous setup for full hour while tracking exceed counts. This is intended to detect instances where the beckhoff may use an additional RT cycle to complete computation and IO operations. Typically 2 cycles of 50 us each are used. 

### Setup
Measure using Tektronix 784D oscilloscope. Mean and standard dev. taken over 512 samples taken at the tail end of the 1 hour study. Minima and maxima taken from 1 hour worth of data. Data taken via a 'positive width' measurement on the subtraction of the output from the starter signal. Measurment is taken within vertical bars but the vertical bars are placed with ~2x the positive region's width on each side of the positive region. Input is set to Hi-res

#### Components in order, left to right
Unchanged

### Results

Measurement | Result
:--------: | -------------:
mean | 100.4us
st. dev | 2.29us
min. | 85.9us
max. | 119.4us

### Discussion
Min and max indicate that the beckhoff is not taking additional/fewer cycles to complete computation. Cycle ount appears to be reliable.

