"""
This file contains the due date calculator implementation.
"""

import sys

# Creates the DueDateCalculator class.
class DueDateCalculator:

    # Declare constants/variables
    # The variable "working_days / non_working_days" corresponds to the following: 1 (Monday), 2 (Tuesday),
    # 3 (Wednesday), 4 (Thursday), 5 (Friday), 6 (Saturday), 7 (Sunday).
    # The variable "calendar" is a dictionary that separates the months that have 31 days, 30 days and 28 days.
    starting_work_time = "9:00"
    ending_work_time = "17:00"
    total_working_hours_in_day = 8
    working_days = [1, 2, 3, 4, 5]
    non_working_days = [6, 7]
    calendar = {31: ["1", "3", "5", "7", "8", "10", "12"], 30: ["4", "6", "9", "11"], 28: "2"}

    # Empty Constructor
    def __init__(self):
        pass

    # This method calculates the date/time the reported problem is to be resolved.
    def calculate_due_date(self, date, time, turnaround_hours, weekday):

        # The date ("month / date / year") and time ("hours : minutes") are split into individual components
        # (month, day, year, hour, minutes). The strings are converted to integers.
        month_problem_reported = int(date.split("/")[0])
        day_problem_reported = int(date.split("/")[1])
        year_problem_reported = int(date.split("/")[2])
        problem_reported_at_time_hour = int(time.split(":")[0])
        problem_reported_in_minutes = int(time.split(":")[1])
        time_work_ends = int(DueDateCalculator.ending_work_time.split(":")[0])
        time_work_starts = int(DueDateCalculator.starting_work_time.split(":")[0])

        # The minutes are converted to the equivalent hours.
        # This gives an accurate calculation of the problem reporting time in hours.
        convert_minutes_to_hours = problem_reported_in_minutes / 60
        problem_reported_at_time_hour += convert_minutes_to_hours
        problem_reporting_time = problem_reported_at_time_hour
        time_to_submission = turnaround_hours

        # A method call is made to check whether the problem reporting time is valid.
        is_reporting_time_input_valid = DueDateCalculator.reporting_time_validation_check(self, problem_reporting_time,
                                                                                          time_work_ends,
                                                                                          time_work_starts, weekday)

        # A method call is made to check whether the weekday is entered as an integer.
        is_weekday_input_valid = DueDateCalculator.weekday_validation_check(self, weekday)

        # If the reporting time input entered is not valid, it returns a message stating the error.
        if not is_reporting_time_input_valid:
            return "A problem can only be reported during working hours."

        # If the weekday input entered is not valid, it returns a message stating the error.
        if not is_weekday_input_valid:
            return "Weekday should be between 1 and 7 inclusive."

        while turnaround_hours > 0:

            # This calculates the remaining working hours of the day, and reduces the turnaround time by that amount.
            remaining_hours = time_work_ends - problem_reported_at_time_hour
            turnaround_hours -= remaining_hours
            problem_reported_at_time_hour = time_work_starts

            # The day count and the weekday count are incremented if the problem cannot be solved on the same day.
            # For example, the problem reporting time is 16:00, and the turnaround is 2 hours. This will go on to the next day.
            # If the weekday exceeds 7 (Sunday), it is reset to 1 (Monday).
            if (
                    remaining_hours == DueDateCalculator.total_working_hours_in_day and problem_reporting_time != time_work_starts) or (
                    remaining_hours == DueDateCalculator.total_working_hours_in_day and problem_reported_at_time_hour == time_work_starts and turnaround_hours > 0):
                day_problem_reported += 1
                weekday += 1
                if weekday > 7:
                    weekday = 1

            # Since Saturday and Sunday are non working days, the turnaround is increased by 8 hours.
            # When the turnaround is reduced in the next iteration, it does not have any effect.
            # It just cancels the 8 hours added inside this condition and increments the date to skip the weekend.
            if weekday == 6 or weekday == 7:
                turnaround_hours += 8

            # This limits the number of days in a month to 31, 30 and 28. If the particular month has reached its days
            # limit, then the day is reset to 1, and the month is incremented. If the months exceed 12, then the month is
            # also reset to 1 and the year is incremented.
            if (day_problem_reported > 31) or (
                    day_problem_reported > 30 and str(month_problem_reported) in DueDateCalculator.calendar[30]) or (
                    day_problem_reported > 28 and str(month_problem_reported) in DueDateCalculator.calendar[28]):
                day_problem_reported = 1
                month_problem_reported += 1
                if month_problem_reported > 12:
                    year_problem_reported += 1
                    month_problem_reported = 1

        # This calculates the number of days until the deadline for resolving the issue.
        # For all turnaround hours that are not multiples of 8, the days will be in decimal.
        # The decimal portion is multiplied by 8 to get the number of extra hours required.
        # For example (3.625 - 3 = 0.625, 0.625 * 8 = 5), 3.625 days is equivalent to 3 days and 5 hours.
        # Since each day has 8 working hours, 3 days and 5 hours is equivalent to 29 hours.
        days_to_submission = time_to_submission / DueDateCalculator.total_working_hours_in_day
        convert_days_float_to_int = time_to_submission // DueDateCalculator.total_working_hours_in_day
        extra_hours = (days_to_submission - convert_days_float_to_int) * DueDateCalculator.total_working_hours_in_day

        # For all turnaround hours that are multiples of 8, there will be no extra hours.
        # If the problem is reported at 9, and there are no extra hours, then the time to resolve the problem
        # is 9 + 8 = 17.
        if extra_hours == 0 and problem_reporting_time == time_work_starts:
            submission_time = problem_reporting_time + DueDateCalculator.total_working_hours_in_day
        else:

            # If the (problem reporting time + extra_hours) is greater than the time work ends (17:00), then the problem
            # will be resolved on the next day. The difference between time work ends and the problem reporting time gives us the
            # the number of hours that can be at most spent on the problem on that day.
            # The "(time_to_submission - (time_work_ends - problem_reporting_time))" expression gets the remaining hours to
            # resolve the problem and adds those to the time work starts. If the turnaround hours are a decent amount time,
            # a while loop keeps reducing down the submission time until it is inside the working hours.
            if (problem_reporting_time + extra_hours) > time_work_ends:
                submission_time = (time_to_submission - (time_work_ends - problem_reporting_time)) + time_work_starts
                while submission_time > time_work_ends:
                    submission_time = (submission_time - time_work_ends) + time_work_starts

            # If (problem reporting time + extra_hours) is less than equal to the time work ends (17:00), it means the
            # problem can be resolved that day, and the due date time is obtained.
            else:
                submission_time = problem_reporting_time + extra_hours

        # This method call formats the date and time the problem was resolved, and it returns a list.
        submission_information = DueDateCalculator.format_date_and_time(self, month_problem_reported,
                                                                        day_problem_reported, year_problem_reported,
                                                                        submission_time, weekday)
        return submission_information

    # This method formats the date and time the problem is resolved. It returns a list.
    def format_date_and_time(self, month, day, year, submit_time, week_day):

        # This calculates the minutes from the hour representation.
        # For example (14.2 - 14 = 0.2 , 0.2 * 60 = 12), 14.2 hours is equivalent to 14 hours 12 minutes.
        submit_time_in_hour = int(submit_time)
        minutes = (submit_time - int(submit_time)) * 60

        # The month, day and submission time (hours, minutes) are represented as 2 digits each. They are converted back
        # to strings. String concatenation is used to get them in the appropriate format (month / date / year), (hours : minutes).
        date_submission = str("{:02d}".format(month)) + "/" + str("{:02d}".format(day)) + "/" + str(year)
        time_submission = str("{:02d}".format(submit_time_in_hour)) + ":" + str("{:02d}".format(int(round(minutes, 1))))

        # This method gets the day of the week the problem is resolved.
        weekday = DueDateCalculator.day_of_the_week(self, week_day)

        return [date_submission, time_submission, weekday]

    # This method gets the day of the week the issue was resolved.
    def day_of_the_week(self, week_day):
        if week_day == 1:
            issue_resolved_day = "Monday"
        elif week_day == 2:
            issue_resolved_day = "Tuesday"
        elif week_day == 3:
            issue_resolved_day = "Wednesday"
        elif week_day == 4:
            issue_resolved_day = "Thursday"
        elif week_day == 5:
            issue_resolved_day = "Friday"
        else:
            issue_resolved_day = "Not a working day"
        return issue_resolved_day

    # This method checks if the problem reporting time is valid and returns a boolean value.
    # The problem reporting time is invalid if the day of the week is a non working day (Saturday, Sunday).
    # The problem reporting time is invalid if it is outside of the normal working hours (9:00 to 17:00).
    def reporting_time_validation_check(self, time_problem_reported, work_end_time, work_start_time, day_of_week):
        input_valid = True
        if (day_of_week in DueDateCalculator.non_working_days) or (time_problem_reported < work_start_time) or (
                time_problem_reported > work_end_time):
            input_valid = False
        return input_valid

    # This method checks if the weekday entered is within the appropriate range.
    def weekday_validation_check(self, day_of_week):
        weekday_input_valid = True
        if day_of_week < 1 or day_of_week > 7:
            weekday_input_valid = False
        return weekday_input_valid
    
def main():
    date = sys.argv[1]
    time = sys.argv[2]
    turnaround_hours = float(sys.argv[3])
    weekday = int(sys.argv[4])
    return DueDateCalculator.calculate_due_date(DueDateCalculator, date, time, turnaround_hours, weekday)

if __name__ == "__main__":
    print(main())
