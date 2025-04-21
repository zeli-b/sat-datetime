from math import floor

FIFTY_YEAR_DAYS = 8559
MONTHS_IN_YEAR_SOLAR = 11
SIX_HUNDRED_YEAR_DAYS = 102708
LUNAR_YEARS_IN_LOOP = 600
YEARS_IN_LOOP = 50


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
    for i in range(1, MONTHS_IN_YEAR_SOLAR + 1):
        result += get_month_days(i, is_leap_year(year))
    return result


class Aveliqua:
    def __init__(self, year=0, month=1, day=1, hour=0, minute=0, second=0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

        self.reduce()
    
    def to_days(self):
        # date to days since 0000-00-00 00:00:00
        days = floor(self.year / YEARS_IN_LOOP) * FIFTY_YEAR_DAYS
        for y in range(year_days % YEARS_IN_LOOP):
            days += get_year_days(y)
        for m in range(1, self.month):
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


def get_lunar_year_days(year):
    result = 0
    for i in get_months_in_lunar_year(year):
        result += get_lunar_month_days(i, year)
    return result


def get_lunar_month_days(month):
    if month == 5.5:
        return 17
    if month % 2 == 0:
        return 18
    return 17


def is_minor_leap_year(year):
    return year % 2 == 0 and year % 100 != 0


def is_major_leap_year(year):
    return year % 3 == 0 and year % 120 != 0


def get_months_in_lunar_year(year):
    months = list(range(1, 9+1))

    if is_minor_leap_year(year):
        months.insert(6, 5.5)
    if is_major_leap_year(year):
        months.append(10)

    return months


class LunarAveliqua:
    def __init__(self, year=0, month=1, day=1, hour=0, minute=0, second=0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

        self.reduce()

    def to_days(self):
        days = floor(self.year / LUNAR_YEARS_IN_LOOP) * SIX_HUNDRED_YEAR_DAYS
        for y in range(year_days % LUNAR_YEARS_IN_LOOP):
            days += get_lunar_year_days(y)
        months = get_months_in_lunar_year(this.year)
        while (m := months.pop(0)) != this.month:
            days += get_lunar_month_days(m)
        days += self.day

        seconds = self.hour * 60 * 60
        seconds += self.minute * 60
        seconds += self.second

        return days, seconds

    def reduce(self):
        days, seconds = self.to_days()

        self.year = days // SIX_HUNDRED_YEAR_DAYS * 600
        days %= SIX_HUNDRED_YEAR_DAYS
        while days >= (ydays := get_lunar_year_days(self.year)):
            days -= ydays
            self.year += 1
        months = get_months_in_lunar_year(this.year)
        self.month = months.pop(0)
        while days >= (mdays := get_lunar_month_days(self.month)):
            days -= mdays
            self.month = months.pop(0)
        self.days = days + 1

        self.hour = seconds // 60 // 60
        self.minute = seconds // 60 % 60
        self.second = seconds % 60

        return self
