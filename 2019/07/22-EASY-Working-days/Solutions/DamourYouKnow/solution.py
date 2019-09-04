from datetime import date, datetime, timedelta

def working_days(year, days_off, holidays):
    start, end = date(year, 1, 1), date(year, 12, 31)
    f = '%Y-%m-%d'
    holidays = set([datetime.strptime(string, f).date() for string in holidays])
    days = [start + timedelta(days=d) for d in range((end - start).days+1)]
    off = lambda d: (d.weekday()+1) % 7 in days_off or d in holidays
    return [str(day) for day in days if not off(day)]
