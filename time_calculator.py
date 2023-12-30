def add_time(start, duration,day = None):
    start_split = start.split()
    start_time = start_split[0]
    AM_PM = start_split[1]
    start_time_split = start_time.split(':')
    duration_split = duration.split(':')
    days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    if (
        not start_time_split[0].isdigit() or
        not start_time_split[1].isdigit() or
        not duration_split[0].isdigit() or
        not duration_split[1].isdigit() or
        len(duration_split) != 2 or
        len(start_time_split) != 2 or
        AM_PM not in ['AM', 'PM']
    ):
        return "Error: the input format should be in the format '11:30 AM/PM, 2:32, Monday (optional)'"

    start_hour = int(start_time_split[0])
    start_minute = int(start_time_split[1])
    duration_hour = int(duration_split[0])
    duration_minute = int(duration_split[1])

    hour_output = start_hour + duration_hour
    minute_output = duration_minute + start_minute
    if minute_output >= 60:
        hour_output = start_hour + duration_hour + minute_output//60
        minute_output = minute_output % 60
        
    if hour_output>=12 and AM_PM == 'AM' :
        n = hour_output//24
        if (hour_output % 24)>=12:
            hour_output = (hour_output % 24) - 12
            AM_PM_output = 'PM'
        else:
            hour_output = hour_output % 24
            AM_PM_output = 'AM'

    if hour_output<12 and AM_PM == 'AM' :
        n = 0
        AM_PM_output = AM_PM

    if hour_output>=12 and AM_PM == 'PM' :
        n = hour_output//24
        if (hour_output % 24)>=12:
            hour_output = (hour_output % 24) - 12
            AM_PM_output = 'AM'
        else:
            hour_output = hour_output % 24
            AM_PM_output = 'PM'

    if hour_output<12 and AM_PM == 'PM' :
        n = 0
        AM_PM_output = AM_PM

    if n==0 :
        number_days = ''
    if n==1:
        number_days = "(next day)"
    if n not in [0,1]:
        number_days = " ("+str(n)+ " days later)"
    
    if day is not None:
        if not isinstance(day, str):
            print('the day is not valid')
        else:
            day = day.capitalize()
            if day in days_list :
                day_position = days_list.index(day)
                day_output_position = (day_position + n)% len(days_list)
                day_output = days_list[day_output_position]
                return str(hour_output)+':'+ str(minute_output)+""+ AM_PM_output +', '+ day_output + number_days
            else:
                print('the day is not valid')

    return str(hour_output)+':'+ str(minute_output)+""+ AM_PM_output +',' + number_days




    return new_time
