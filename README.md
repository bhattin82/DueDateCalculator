# DueDateCalculator

This repository contains the code for the due date calculator. The calculator_tests.py consists of all the unit tests written for the due date calculator. The tests can be run by the following command: python3 calculator_tests.py

The calculator.py has the due date calculator implementation. For more testing of the due date calculator, the calculator.py can be run with the following command: python3 calculator.py date time turnaround weekday

The date format should be mm/dd/year, and the time should be in the 24 hour format.

For example, the command can be "python3 calculator.py 05/31/2023 15:00 2 3"

The code makes the following assumptions:
1. The current year is not a leap year.
2. The weekday entered is consistent with the date entered.
3. The weekday is only entered as an integer.

