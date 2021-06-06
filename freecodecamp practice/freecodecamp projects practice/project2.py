def add_time(start, duration, start_week_day=None):
    if start.split(' ')[1] == "PM":
        start_hour = int(start.split(':')[0]) + 12
        start = str(start_hour) + ":" + start.split(':')[1]

    total_time_hour = int(start.split(' ')[0].split(':')[0]) + int(duration.split(':')[0])
    total_time_minute = int(start.split(' ')[0].split(':')[1]) + int(duration.split(':')[1])
    total_time_days = 0
    time_postfix = start.split(' ')[1]
    if total_time_minute >= 60:
        total_time_hour += 1
        total_time_minute = total_time_minute % 60
    if total_time_hour >= 24:
        total_time_days = total_time_hour // 24
        total_time_hour = total_time_hour % 24

    if total_time_hour >= 12:
        if total_time_hour >= 13:
            total_time_hour = total_time_hour % 12
        time_postfix = "PM"
    else:
        if total_time_hour < 1:
            total_time_hour =12
        time_postfix = "AM"
    new_days =""
    if total_time_days > 0:
        if total_time_days == 1:
            new_days =" (next day)"
        else:
            new_days = f" ({total_time_days} days later)"
    week_days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    new_week_day=""
    if start_week_day is not None:
        new_week_day = ", " + week_days[(week_days.index(start_week_day.lower()) + total_time_days) % len(week_days)].capitalize()

    new_time = str(total_time_hour) + ":" + str(total_time_minute).rjust(2, "0") + " " + time_postfix + new_week_day + new_days

    return new_time


print(add_time("11:59 PM", "24:05"))
