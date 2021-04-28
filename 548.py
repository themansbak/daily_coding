"""
Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?

(hh%12)*30 = angle of hour
(mm%60)%6 = angle of minutes
"""

def convert_hour_to_angle(hour, minute):
    return (hour%12 + (minute/60))*30

def convert_minute_to_angle(minute):
    return (minute%60)*6

def convert_time_to_hhmm(time):
    return (int(time[:2]), int(time[3:]))

def calculate_angle(time):
    hh, mm = convert_time_to_hhmm(time)
    diff = convert_hour_to_angle(hh, mm) - convert_minute_to_angle(mm)
    return min(diff, 360-diff)

time = "23:01"

print(calculate_angle(time))