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
New osc. allows for precise measurments of delay timeings. Rerun study with better measuring tools for better data.

### Setup
Now using Tektronix 784D oscilloscope in place of Tektronix TDS 2024. Measurments taken over 512 samples.

#### Components in order, left to right
Unchanged

### Results
mean = 100.1us delay, st. dev = 20 ns, min = 99.6us, max = 100.1us. Mean can vary to 99.9us and std to 30ns. 

### Discussion
Min and max indicate that the beckhoff is not taking additional/fewer cycles to complete computation. Cycle ount appears to be reliable. Cycle timing has very minor std. dev. of 20ns and mean very near advertised 100us. 

