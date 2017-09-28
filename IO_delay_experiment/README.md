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
### Components in order, left to right
0. CX2020
0. EL7041 (unused)
0. EL9186
0. EL9187
0. EK9505
0. EL2124
0. EL1124

### Setup
Observed using Tektronix TDS 2024 oscilloscope monitoring starter and output signals. 

### Observed
100 us delay between starter and output with estimated jitter of ~20 us 

### Notes
Was not able to measure reliabilty of jitter. Must learn to perform measurments on math-constructed traces. Tests were first conducted with EL1124 with some dead terminals and later with more better EL1124. EL1124 had no effect on results. 
