# LogicEffectOnRealTimeUsage experiment
This project explores the process time required by various programmed tasks. This setup runs a set number of operations in a given execution cycle. Every couple of cycles, the number of executions increases to a limit then resets. The RealTimeusage plot appears similar to a sawtooth wave showing the percentile usage at the minimum and maximum number of operations. 

## Goal
Find the relationship between various software operations and exetuaion time. Operations include comparisons and assignment. More operations may be included later. IO operations are being omitted for now 

## Required components 
- CX2020

## Preliminary Test on 9-28-17
### setup
Observed using TC's Real-Time's RealtimeUsage, the Task's Online plots and the excess counter. 

#### Components in order, left to right
0. CX2020
0. EL7041 (unused)
0. EL9186 (unused)
0. EL9187 (unused)
0. EK9505 (unused)
0. EL2124 (unused)
0. EL1124 (unused)


### Results
Operation time appears to scale linearly with number of mathematical operations. Sawtooth pattern clearly visible. 1000 operations reliably produced no excess counts. At roughly 1700 and greater operations, excesses were numerous and reliable. Relationship appears linear. Odd geometry of plots noticed in Real Time Usage and plcTask plots during and around excesses. 

### Discussion



