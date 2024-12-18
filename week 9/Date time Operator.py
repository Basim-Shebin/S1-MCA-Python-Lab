import datetime

class Time:
    def __init__(self):
        time_entry = input('Enter a time in hh:mm:ss format: ')
        self.__hours, self.__minutes, self.__seconds = map(int, time_entry.split(':'))

    def __str__(self):
        return f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}"

    def __add__(self, other):
        # Convert both times to seconds
        self_seconds = self.__hours * 3600 + self.__minutes * 60 + self.__seconds
        other_seconds = other.__hours * 3600 + other.__minutes * 60 + other.__seconds
        total_seconds = self_seconds + other_seconds

        # Convert back to hours, minutes, seconds
        return convert(total_seconds)

def convert(seconds):
    # Normalize the seconds to a 24-hour format
    seconds = seconds % (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hours, minutes, seconds)

# Creating two Time objects
t1 = Time()
t2 = Time()

# Adding the two Time objects and printing the result
print("Sum of times: ", t1 + t2)
