# LogicEffectOnRealTimeUsage experiment
This project explores the process time required by various programmed tasks. This setup runs a set number of operations in a given execution cycle. Every couple of cycles, the number of executions increases to a limit then resets. The RealTimeusage plot appears similar to a sawtooth wave showing the percentile usage at the minimum and maximum number of operations. 

## Goal
Find the relationship between various software operations and exetuaion time. Operations include comparisons and assignment. More operations may be included later. IO operations are being omitted for now 

## Required components 
- CX2020

## Preliminary Test on 9-28-17
### setup
Observed using TC's Real-Time's RealtimeUsage, the Task's Online plots and the excess counter. The Beckhoff's real time cycles operated at 20kHz.

#### Components in order, left to right
0. CX2020
0. EL7041 (unused)
0. EL9186 (unused)
0. EL9187 (unused)
0. EK9505 (unused)
0. EL2124 (unused)
0. EL1124 (unused)


### Results
Operation time appears proportional with number of mathematical operations. Sawtooth pattern clearly visible. 1000 operations reliably produced no excess counts. At roughly 1700 and greater operations, excesses were numerous and reliable. Relationship appears linear. Odd geometry of plots noticed in Real Time Usage and plcTask plots during and around excesses. 

### Discussion
The plots indicate a linear relationship between number of logic operations and real time usage indicating that the compile options we used don't feature any form of optimization for repetitive logic tasks. The limits of the logic we can perform should be investigated further. 



## Detailed on 10-13-17
### Intro
This more detailed version of the study is meant to more specifically determine the perfocmance of the beckhoff under different logic loads.

### setup
Observed using TC's oline plots and the excess counter. The Beckhoff's real time cycles operated at 20kHz. For each test, the exceed counter was reset and the study was run for one minute. 

#### Components in order, left to right
0. CX2020
0. EL7041 (unused)
0. EL9186 (unused)
0. EL9187 (unused)
0. EK9505 (unused)
0. EL2124 (unused)
0. EL1124 (unused)

### Results
See images in results folder. Grid spacing is 1us in the y axis and 1s the x axis.
Averages are taken over the last 10 minima/maxima.

| Operations | Average Minimum Time | Average Maximum Time | Exceed Counts
| ----: | -----: | ----: | ----:
| 800 | 16.7 | 4.6 | 0
| 900 | 18.4 | 4.4 | 0
| 1000 | 20.6 | 4.7 | 0
| 1100 | 22.4 | 4.2 | 2
| 1200 | 24.3 | 4.6 | 1
| 1300 | 26.1 | 4.8 | 1
| 1400 | 27.9 | 4.6 | 20
| 1500 | 29.6 | 4.4 | 185
| 1600 | 31.5 | 4.9 | 416
| 2000 | 4.7 | ? | 73842



### Discussion
The plots indicate a linear relationship between number of logic operations and real time usage indicating that the compile options we used don't feature any form of optimization for repetitive logic tasks. The limits of the logic we can perform should be investigated further. 
