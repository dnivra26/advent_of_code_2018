import re
import datetime
file = open("input.txt", "r")

lines = file.read().splitlines()

lines.sort()
employee = 0
sleep_minute = 0
wake_up_minute = 0
diary = {}
    
for line in lines:
    shift_begin_match = re.match(r'^\[(.*)] Guard #(.*) begins shift$',line)
    falls_asleep_match = re.match(r'^\[(.*)] falls asleep$',line)
    wakes_up_match = re.match(r'^\[(.*)] wakes up$',line)
    

    if shift_begin_match:
        employee = shift_begin_match.group(2)
    elif falls_asleep_match:
        sleep_time = falls_asleep_match.group(1)
        sleep_minute = datetime.datetime.strptime(sleep_time, "%Y-%m-%d %H:%M").time().minute
    elif wakes_up_match:
        wake_up_time = wakes_up_match.group(1)
        wake_up_minute = datetime.datetime.strptime(wake_up_time, "%Y-%m-%d %H:%M").time().minute
        day = datetime.datetime.strptime(wake_up_time, "%Y-%m-%d %H:%M").date().day
        
        for minute in range(sleep_minute, wake_up_minute):
            if employee not in diary:
                diary[employee] = { minute: 1}
            elif (minute not in diary[employee]):
                diary[employee][minute] = 1
            else:
                diary[employee][minute] = diary[employee][minute] + 1

max_employee_mins = 0
max_employee_id = 0
max_day_mins = 0
max_minute = 0

overall_max_minute = 0
overall_max_employee_id = 0

for emp in diary:
    total_mins = 0
    max_mins = 0
    minu = 0
    for minute in diary[emp]:
        total_mins = total_mins + diary[emp][minute]
        if(diary[emp][minute] > overall_max_minute):
            overall_max_minute = minute
            overall_max_employee_id = emp
        if(diary[emp][minute] > max_mins):
            max_mins = diary[emp][minute]
            minu = minute
      
    if total_mins > max_employee_mins:
        max_employee_mins = total_mins
        max_employee_id = emp
        max_day_mins = max_mins    
        max_minute = minu

print( max_employee_id, max_minute, max_day_mins, int(max_employee_id)*max_minute)

print( "overall", overall_max_employee_id, overall_max_minute , int(overall_max_employee_id) * overall_max_minute)