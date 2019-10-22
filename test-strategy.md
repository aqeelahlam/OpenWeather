This document will describe the test case selection strategy used to select the test cases for our weatherforcast.py program.
The aim of the test case selection strategy (tcss) is to maximise statement coverage with the minimum number of tests.
A series of white box test strategies will be implemented with the help of a control flow graph (cfg) to achieve this.
The test strategies used will be path coverage and modified condition coverage. Path coverage is chosen due to how it encompasses statement
coverage and branch coverage. Path coverage aims to cover every single path that an execution process can take. In this way it maximises how much
of the code is tested. The weakness of path coverage is that it doesnt handle boolean AND or OR statements very well. To make up for this
issue, modified condition/decision coverage(mcdc) is implemented. It aims to cover every possible decision which will have an effect
on the final outcome of the boolean expression.

Test Case | Test Strategy
----------|---------------
Test 1 | Path coverage. By taking all the options to be true, we test what the output is if all options are provided.