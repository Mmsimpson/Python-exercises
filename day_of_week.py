day = int(raw_input('Day (0-6)?) ')) 
day_of_week = ['Sunday','Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday']
print day_of_week[day]

if 1 <= day <=  5:
    print "Go to work."
else: 
    print "Sleep in."
