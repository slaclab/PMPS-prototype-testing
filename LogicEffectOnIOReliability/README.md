# Logic's Effect on IO Reliablity experiment
This project is a pairing of LogicEffectOnRealTimeUsage and IO_Delay_experiment. The goal of this study is to determine what effect programmed logic has on the reliability of IO operatinos.

## Goal
Attempt to produce minimum delay for basic IO operations while running an increasing quantity of logic operations. 


## Required components 
- EL1124
- EL2124
- EK9505
- EL9186
- EL9187

## Test on 10-3-17

### Setup
Observed using Tektronix TDS 784D oscilloscope monitoring starter and output signals. Run with a maximum of 600 operations (ulimit)
delay of 50. Monitor delay using by subtraction response signal from initiation signal and measuring positive width of the resulting shape. Minima and maxima statistics accrue over time. Run for 15 minutes. 

#### Components in order, left to right
0. CX2020
0. EL7041 (unused)
0. EL9186
0. EL9187
0. EK9505
0. EL2124
0. EL1124

### Results
7 Exceed counts
112.5 us Maximum delay

### Discussion
With sufficiently few operations, the required number of cycles does not exceed 2 (each being ~ 50us). Interestingly, Exceed counts can appear without stretching the maximum delay. 

