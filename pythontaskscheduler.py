"""
Python Task Scheduler
8/12/2020
"""
import os, datetime, time

# handles timing and execution
def schedule(directory, hour, minute, second, days, project):
    # changes directory 
    try:
        os.chdir(os.path.dirname(directory))
    except FileNotFoundError:
        print("Cant find directory " + os.path.dirname(directory))
        raise
    # sees if the time is true or not
    now = datetime.datetime.now()
    # checks what the day is 
    today = now.weekday()

    # checks for requirments    
    istodaytheday = day(today, days)
    starth = hour
    startm = minute
    starts = second
    programstart = now.replace(hour = starth, minute = startm, second = starts)

    if (now == programstart and istodaytheday):
        print("Starting " + project + " at " + now)
        os.system("py " + directory)
        time.sleep(1)

# checks if today is the day 
def day(day, days):
        days = days.upper()
        daysch = []
        daych = []
        
        for i in days:
            daysch.append(i)

        for i in daysch:
            if i == 'M':
                daych.append(0)
            if i == 'T':
                daych.append(1)
            if i == 'W':
                daych.append(2)
            if i == 'R':
                daych.append(3)
            if i == 'F':
                daych.append(4)
            if i == 'S':
                daych.append(5)
            if i == 'U':
                daych.append(6)

        for i in daych:
            if i == day:
                return True

        return False
                
