f = open('input.txt', 'r')
time = f.read()
ff = open("output.txt", "w")
hours = int(time[0])*10 + int(time[1])
mins = int(time[3])*10 + int(time[4])
secs = int(time[6])*10 + int(time[7])
if secs == 0 and mins % 30 == 0:
    if hours == 0 and mins == 0:
        ff.write("23:30:00")
    elif hours == 0:
        ff.write("00:00:00")
    elif mins == 0:
        if hours < 10:
            ff.write("0" + str(hours - 1) + ":30:00" )
        else:
            ff.write(str(hours - 1) + ":30:00")
    else:
        if hours < 10:
            ff.write("0" + str(hours)+"00:00")
        else:
            ff.write(str(hours) + "00:00")
else:
    if hours == 0 and mins < 30:
        ff.write("00:00:00")
    elif hours == 0 and mins >= 30:
        ff.write("00:30:00")
    elif mins >= 30:
        if hours < 10:
            ff.write("0" + str(hours) + ":30:00")
        else:
            ff.write(str(hours) + ":30:00")
    else:
        if hours < 10:
            ff.write("0" + str(hours) + ":00:00")
        else:
            ff.write(str(hours) + ":00:00")
ff.close()
