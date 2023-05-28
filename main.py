"""
This file contains the unit tests. The project was implemented using the TDD (Test Driven Development) approach.
The input takes in a date (month/date/year), time (24 hour format) problem was reported, turnaround time and the
day of the week the problem was reported.

Assumptions:
1. The current year is not a leap year.
2. The weekday entered is consistent with the date entered.
"""

from calculator import DueDateCalculator
import unittest


# Creates the class DueDateCalculatorTests
class DueDateCalculatorTests(unittest.TestCase):

    # This test is for a problem reported during the week, and it is resolved within the same week.
    def test_problem_resolved_same_week(self):
        date_time_issue_resolved = DueDateCalculator.calculate_due_date(self, "05/29/2023", "10:00", 18, 1)
        self.assertEqual(date_time_issue_resolved, ["05/31/2023", "12:00", "Wednesday"])

    # This test is for a problem reported at 14:12 on Tuesday, and it is resolved at 14:12 on Thursday.
    # This test was taken from the example given in the pdf.
    def test_example_given_in_pdf(self):
        date_time_issue_resolved = DueDateCalculator.calculate_due_date(self, "05/30/2023", "14:12", 16, 2)
        self.assertEqual(date_time_issue_resolved, ["06/01/2023", "14:12", "Thursday"])

    # This test is for a problem reported at the end of the month (e.g. May), and it is resolved
    # at the start of the next month (e.g. June).
    def test_problem_reported_at_end_of_month_and_resolved_start_of_next_month(self):
        date_time_issue_resolved = DueDateCalculator.calculate_due_date(self, "05/31/2023", "9:30", 21, 3)
        self.assertEqual(date_time_issue_resolved, ["06/02/2023", "14:30", "Friday"])

    # This test is for a problem reported on 28th February, and it is resolved at the start of the next month.
    def test_problem_reported_on_28th_February_resolved_start_of_next_month(self):
        date_time_issue_resolved = DueDateCalculator.calculate_due_date(self, "02/28/2023", "13:30", 11, 2)
        self.assertEqual(date_time_issue_resolved, ["03/01/2023", "16:30", "Wednesday"])

    # This test is for a problem that is resolved in the next week.
    def test_problem_resolved_next_week(self):
        date_time_issue_resolved = DueDateCalculator.calculate_due_date(self, "06/01/2023", "15:00", 18, 4)
        self.assertEqual(date_time_issue_resolved, ["06/05/2023", "17:00", "Monday"])

    # This test is for a problem that is resolved on the same day.
    def test_problem_resolved_on_same_day(self):
        date_time_issue_resolved = DueDateCalculator.calculate_due_date(self, "06/02/2023", "12:00", 3, 5)
        self.assertEqual(date_time_issue_resolved, ["06/02/2023", "15:00", "Friday"])

    # This test is for a problem reported at 17:00 on Friday, and it is resolved after the weekend.
    def test_problem_reported_at_5pm_on_friday_resolved_after_weekend(self):
        date_time_issue_resolved = DueDateCalculator.calculate_due_date(self, "05/26/2023", "17:00", 24, 5)
        self.assertEqual(date_time_issue_resolved, ["05/31/2023", "17:00", "Wednesday"])

    # This test is for a problem reported before 17:00 on Friday, and it is resolved after the weekend.
    def test_problem_reported_before_5pm_friday_resolved_after_weekend(self):
        date_time_issue_resolved = DueDateCalculator.calculate_due_date(self, "05/26/2023", "16:00", 3, 5)
        self.assertEqual(date_time_issue_resolved, ["05/29/2023", "11:00", "Monday"])

    # This test is for a problem reported on the last working day of the year, and it is resolved next year.
    def test_problem_reported_on_last_working_day_of_year(self):
        date_time_issue_resolved = DueDateCalculator.calculate_due_date(self, "12/29/2023", "10:00", 12, 5)
        self.assertEqual(date_time_issue_resolved, ["01/01/2024", "14:00", "Monday"])

    # This test is for a problem reported at the end of a particular month (e.g. May), and it is resolved after a
    # relatively long duration.
    def test_problem_resolved_after_a_month(self):
        date_time_issue_resolved = DueDateCalculator.calculate_due_date(self, "05/26/2023", "12:23", 250, 5)
        self.assertEqual(date_time_issue_resolved, ["07/10/2023", "14:23", "Monday"])

    # This test is for a problem that has turnaround time in decimal.
    def test_problem_turnaround_in_decimal(self):
        date_time_issue_resolved = DueDateCalculator.calculate_due_date(self, "06/15/2023", "16:00", 3.25, 4)
        self.assertEqual(date_time_issue_resolved, ["06/16/2023", "11:15", "Friday"])

    # This test is for a problem reported outside of the working hours (before work starts).
    def test_problem_reported_before_work_hours(self):
        date_time_issue_resolved = DueDateCalculator.calculate_due_date(self, "05/30/2023", "6:00", 4, 2)
        self.assertEqual(date_time_issue_resolved, "A problem can only be reported during working hours.")

    # This test is for a problem reported outside of the working hours (after work ends).
    def test_problem_reported_after_work_hours(self):
        date_time_issue_resolved = DueDateCalculator.calculate_due_date(self, "06/01/2023", "19:00", 7, 4)
        self.assertEqual(date_time_issue_resolved, "A problem can only be reported during working hours.")

    # This test is for a problem reported on the weekend.
    def test_problem_reported_on_weekend(self):
        date_time_issue_resolved = DueDateCalculator.calculate_due_date(self, "05/27/2023", "11:00", 2, 6)
        self.assertEqual(date_time_issue_resolved, "A problem can only be reported during working hours.")

    # This test is for an invalid input type (weekday is in decimal).
    def test_weekday_in_decimal(self):
        date_time_issue_resolved = DueDateCalculator.calculate_due_date(self, "05/31/2023", "9:00", 6, 3.2)
        self.assertEqual(date_time_issue_resolved, "Weekday should be entered as an integer and should be between 1 and 7 inclusive.")

    # This test is for an invalid weekday (weekday is out of range).
    def test_weekday_out_of_range(self):
        date_time_issue_resolved = DueDateCalculator.calculate_due_date(self, "06/05/2023", "10:00", 3, 8)
        self.assertEqual(date_time_issue_resolved, "Weekday should be entered as an integer and should be between 1 and 7 inclusive.")

if __name__ == '__main__':
    unittest.main()
