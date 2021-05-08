from math import fabs
from math import floor

hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arriving = int(input())
minutes_of_arriving = int(input())
time_of_exam_in_minutes = hour_of_exam * 60 + minutes_of_exam
time_of_arrive_in_minutes = hour_of_arriving * 60 + minutes_of_arriving
deifference = fabs(time_of_exam_in_minutes - time_of_arrive_in_minutes)
if time_of_arrive_in_minutes > time_of_exam_in_minutes:
    print("Late")
elif time_of_exam_in_minutes - 30 <= time_of_arrive_in_minutes <= time_of_exam_in_minutes:
    print("On time")
elif time_of_arrive_in_minutes < time_of_exam_in_minutes - 30:
    print("Early")
if time_of_exam_in_minutes - 60 < time_of_arrive_in_minutes < time_of_exam_in_minutes:
    print(f"{floor(deifference)} minutes before the start")
elif time_of_arrive_in_minutes <= time_of_exam_in_minutes - 60:
    hour = floor(deifference // 60)
    minutes = floor(deifference % 60)
    if minutes <= 9:
        print(f"{hour}:0{minutes} hours before the start")
    else:
        print(f"{hour}:{minutes} hours before the start")
elif time_of_exam_in_minutes < time_of_arrive_in_minutes < time_of_exam_in_minutes + 60:
    print(f"{floor(deifference)} minutes after the start")
elif time_of_arrive_in_minutes >= time_of_exam_in_minutes + 60:
    hour = floor(deifference // 60)
    minutes = floor(deifference % 60)
    if minutes <= 9:
        print(f"{hour}:0{minutes} hours after the start")
    else:
        print(f"{hour}:{minutes} hours after the start")
