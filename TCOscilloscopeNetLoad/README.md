# TCOscilloscopeNetLoad experiment
This project explores the load introduced by monitoring the system when monitoring the system via twincat's oscilloscope. The TwinCAT project cycles a large array of integers at varying rates while providing the 5V trigger and response inputs and outputs common to the other tests. The integegers can be monitored via the TwinCAT scope and the trigger/response setup can be connected to the oscilloscope to watch for irregular PLC cycle counts. 

## Goal
Find the relationship between the number of live variables monitored, and the performance of the PLC and monitoring PC. 

## Required components 
0. CX2020
0. EL9186
0. EL9187 
0. EK9505
0. EL2124
0. EL1124

## Test on 10-4-17
### setup
To test this relationship, different numbers of variables were monitored for ~10 seconds. During this time, the PLC task's performance and network usage were montorored via the online tab and Windows Task manager respectively.

#### Components in order, left to right
0. CX2020
0. EL7041 (unused)
0. EL9186
0. EL9187
0. EK9505
0. EL2124 
0. EL1124


### Results
Qty. Variables Monitored | Network traffic (MBPS+/-1)  | CPU time (us+/15) | Total time (us+/-5)
------------------------ | ----------------------- | ------------- | ---------------
0 | 120kbps | 11.0 | 12.2 
1 | 4.2 | 12.2 | 12.9 
2 | 6.2 | 12.6 | 13.1 
3 | 8.2 | 12.6 | 13.0 
4 | 10.2 | 12.8 | 13.3 
5 | 12.2 | 13.0 | 13.5 
6 | 14.3 | 13.2 | 13.6 
7 | 16.4 | 13.4 | 13.8 
8 | 18.4 | 13.6 | 14.0
9 | 20.4 | 13.7 | 14.2
10 | 22.4 | 13.4 | 14.4 
20 | 42.7 | 16.8 | 17.4 
30 | 63.0 | 18.8 | 19.5 
40 | 82.6 | 19.5 | 20.0 


### Discussion
![Network/Beckhoff load plots](https://raw.githubusercontent.com/slaclab/PMPS-prototype-testing/master/TCOscilloscopeNetLoad/netload_plots.png)

|  | Cost per variable | Flat cost
-- | ----------------- | ---------
Network Load (Mbps) | 2.03+/-.01 | 1.9+/-.2
Beckhoff CPU time (us) | .21+/-.01 | 11.8+/-.2
Beckhoff Total time (us) | .21+/-.01 | 12.4+/-.2

### Conclusion
Monitoring a beckhoff system's variables via the TwinCAT oscilloscope may be viable for for a small number of variables or more if sampled at a lesser rate. This setup will not be capable of monitoring the entirety of multiple Beckhoff programs at the maximum beckhoff rate of 20khz.




