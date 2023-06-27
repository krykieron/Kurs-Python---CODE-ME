from datetime import datetime
from calendar import monthrange, monthcalendar

class Watch():
    def get_current_time(self):
        now = datetime.now()
        return now.strftime("%H:%M")


class Calendar():
    def __init__(self):
        now = datetime.now()
        self.year = now.year
        self.month = now.month

    def get_current_date(self):
        now = datetime.now()
        return now.strftime("%d / %m / %Y")


    def get_month_days(self):
        return monthrange(self.year, self.month)[1]

    def show_calendar_weeks(self):
        weeks = monthcalendar(self.year, self.month)

        for i in ['Mo', "Tu", "We", "Th", "Fr", "St", "Su"]:
            print(i, end="\t")
        print()
        print('-----------------------------')

        for week in weeks:
            for day in week:
                print(day, end='\t')
            print()


class WatchCalendar(Watch, Calendar):
    def show_current_datetime_info(self):
        print(f"Current TIME: {super().get_current_time()}")
        print(f"Current DATE: { super().get_current_date()}")
        print(f"Current month has {super().get_month_days()} days")

        super().show_calendar_weeks()


watch_calendar = WatchCalendar()
watch_calendar.show_current_datetime_info()

# my_watch = Watch()
# my_watch.get_current_time()
# my_calendar = Calendar()
# my_calendar.show_calendar_weeks()
# my_calendar.get_month_days()
