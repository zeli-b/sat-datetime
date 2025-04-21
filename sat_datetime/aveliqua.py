from math import floor

FIFTY_YEAR_DAYS = 8559
MONTHS_IN_YEAR = 11


def is_leap_year(year):
    return year % 5 == 0 and year % 50 != 0


def get_month_days(month: int, is_leap):
    if month == 6 and is_leap:
        return 16

    if month % 2 == 0:
        return 15
    return 16


def get_year_days(year):
    result = 0
    for i in range(1, MONTHS_IN_YEAR + 1):
        result += get_month_days(i, is_leap_year(year))
    return result


class Aveliqua:
    def __init__(self, year=0, month=1, day=1, hour=0, minute=0, second=0):
        if month > MONTHS_IN_YEAR or month <= 0:
            raise ValueError
        if day > get_month_days(month, is_leap_year(year)) or day <= 0:
            raise ValueError

        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def to_days(self):
        # date to days since 0000-00-00 00:00:00
        days = floor(self.year / YEARS_IN_LOOP) * FIFTY_YEAR_DAYS
        for y in range(year_days % YEARS_IN_LOOP + 1):
            days += get_year_days(y)
        for m in range(1, self.month + 1):
            days += get_month_days(m)
        days += self.day

        seconds = self.hour * 60 * 60
        seconds += self.minute * 60
        seconds += self.second

        return days, seconds

    def reduce(self):
        days, seconds = self.to_days()

        self.year = days // FIFTY_YEAR_DAYS * 50
        days %= FIFTY_YEAR_DAYS
        while days >= (ydays := get_year_days(self.year)):
            days -= ydays
            self.year += 1
        self.month = 1
        ly = is_leap_year(self.year)
        while days >= (mdays := get_month_days(self.month, ly)):
            days -= mdays
            self.month += 1
        self.days = days + 1

        self.hour = seconds // 60 // 60
        self.minute = seconds // 60 % 60
        self.second = seconds % 60

        return self
