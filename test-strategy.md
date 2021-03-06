This document will describe the test case selection strategy used to select the test cases for our weatherforcast.py program.
The aim of the test case selection strategy (tcss) is to maximise statement coverage with the minimum number of tests.
A series of white box test strategies will be implemented with the help of a control flow graph (cfg) to achieve this.
The test strategies used will be path coverage and modified condition coverage. Path coverage is chosen due to how it encompasses statement
coverage and branch coverage. Path coverage aims to cover every single path that an execution process can take. In this way it maximises how much
of the code is tested. The weakness of path coverage is that it doesnt handle boolean AND or OR statements very well. To make up for this
issue, modified condition/decision coverage(mcdc) is implemented. It aims to cover every possible decision which will have an effect
on the final outcome of the boolean expression.



By individually checking if each option works, we only cover half the possibles. This is because by enabling one option, we set everything option to false in our 
test cases. Although this results in less path coverage, it does not effect the testing of the functional correctness because each options functionality is independent of the others.


MCDC is used to test the location functionality, as only one location identifier can be accepted at a time.

For the for loop, we use loop coverage, where we enter the loop 0 times, 1 time, and many times, to see if the behaviour changes. However, we cannot not enter the loop,
because it causes an error to be thrown. The for loop requires the range to be greater than 1. 