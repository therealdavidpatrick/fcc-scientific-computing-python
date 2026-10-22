def add_time(start, duration, starting_day = None):
    start_hour, rest = start.split(":")
    start_minute, period = rest.split(" ")

    start_hour = int(start_hour)
    start_minute = int(start_minute)

    duration_hour, duration_minute = duration.split(":")

    duration_hour = int(duration_hour)
    duration_minute = int(duration_minute)

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    if period == "PM" and start_hour != 12:
        start_hour += 12
    
    if period == "AM" and start_hour == 12:
        start_hour -= 12

    start_total_minutes = (start_hour * 60) + start_minute

    duration_total_minutes = (duration_hour * 60) + duration_minute

    new_total_minutes = start_total_minutes + duration_total_minutes

    days_later = new_total_minutes // 1440
    remaining_minutes = new_total_minutes % 1440

    new_hour = remaining_minutes // 60 
    new_minute = remaining_minutes % 60

    if new_hour >= 12:
        new_period = "PM"
    else: 
        new_period = "AM"
    
    if new_hour > 12:
        new_hour -= 12

    if new_hour == 0:
        new_hour += 12

    new_time = f'{new_hour}:{new_minute:02d} {new_period}'

    if starting_day is not None:
        days_index = weekdays.index(starting_day.capitalize())
        new_day_index = (days_index + days_later) % 7
        new_weekday = weekdays[new_day_index]
        new_time = new_time + ", " + new_weekday

    if days_later == 0:
        pass

    elif days_later == 1:
        new_time = new_time + " (next day)"
    
    else: 
        new_time = new_time + " (" + str(days_later) + " days later)"

    return new_time

print(add_time('3:30 PM', '2:12'))
print(add_time('11:55 AM', '3:12'))
print(add_time('2:59 AM', '24:00'))
print(add_time('11:59 PM', '24:05'))
print(add_time('8:16 PM', '466:02'))
print(add_time('3:30 PM', '2:12', 'Monday'))
print(add_time('2:59 AM', '24:00', 'saturDay'))
print(add_time('11:59 PM', '24:05', 'Wednesday'))
print(add_time('8:16 PM', '466:02', 'tuesday'))
