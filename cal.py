from django.utils import timezone
import calendar


class Day:
    def __init__(self, number, past):
        self.number = number
        self.past = past

    def __str__(self):
        return str(self.number)


class Calendar(calendar.Calendar):
    def __init__(self, year, month):
        super().__init__(firstweekday=0)
        self.year = year
        self.month = month
        self.days_n = ("월", "화", "수", "목", "금", "토", "일")
        self.months = (
            "1 월",
            "2 월",
            "3 월",
            "4 월",
            "5 월",
            "6 월",
            "7 월",
            "8 월",
            "9 월",
            "10 월",
            "11 월",
            "12 월",
        )

    def get_days(self):
        weeks = self.monthdays2calendar(self.year, self.month)
        days = []
        for week in weeks:
            for day, _ in week:
                now = timezone.now()
                today = now.day
                month = now.month
                past = False
                if month == self.month:
                    if day <= today:
                        past = True
                new_day = Day(day, past)
                days.append(new_day)
        return days

    def get_month(self):
        return self.months[self.month - 1]