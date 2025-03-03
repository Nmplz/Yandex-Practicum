time = '1h 45m,360s,25m,30m 120s,2h 60s'
lst = time.replace(',', ' ').split()
total_time_in_minutes = 0
for x in lst:
    if 'h' in x:
        total_time_in_minutes += int(x[:-1]) * 60
    elif 'm' in x:
        total_time_in_minutes += int(x[:-1])
    else:
        total_time_in_minutes += int(x[:-1]) / 60

print(int(total_time_in_minutes))