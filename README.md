# DueDateCalculator

This repository contains the code for the implementation of a due date calculator in an issue tracking system (ITS). The due date calculator is provided with the following inputs: date the problem was reported, time the problem was reported, day the problem was reported and the turnaround time. The calculator outputs the due date for the problem to be resolved. The code takes into consideration the following rules: 

 1. Working hours are from 9 AM to 5 PM (Monday to Friday)
 2. The turnaround time is in working hours. For example, if the problem reporting time is at 16:00 on Monday and the turnaround time is 2 hours, then the problem due date is at 10:00 on Tuesday.  
 3. A problem can only be reported during working hours.

The code was written using Test Driven Development (TDD). The calculator_tests.py consists of all the unit tests written for the due date calculator. The tests can be run with the following command: python3 calculator_tests.py

The calculator.py has the due date calculator implementation. For further testing of the due date calculator, the calculator.py file can be run with the following command: python3 calculator.py date time turnaround weekday

The date format should be mm/dd/year, and the time should be in the 24 hour format.

For example, the command can be "python3 calculator.py 05/31/2023 15:00 2 3". The output should be 05/31/2023 17:00 Wednesday. 

The code makes the following assumptions:
1. The current year is not a leap year.
2. The weekday entered is consistent with the date entered.
3. The weekday is only entered as an integer.

Lastly, this project was completed without using any external libraries for date and time.

