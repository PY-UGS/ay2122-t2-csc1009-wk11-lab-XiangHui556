# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class clockTime:
    hour = "00"
    minute = "00"
    seconds = "00"
    def setHours(self, hour2):
        print("Set Hours")
        hour = hour2
        
    def setMinutes(self, minute2):
        print("Set Minutes")
        minute = minute2
        
    def setSeconds(self, seconds2):
        print("Set Seconds")
        seconds = seconds2
        
    def setTime(self, hour2, minute2, seconds2):
        print("Set Time")
        hour = hour2
        minute = minute2
        seconds = seconds2
        
    def showTime(self):
        return str(hour)+":"+str(minute)+":"+str(seconds)

time = clockTime()

timestring = input("Please set the time ::00 for seconds :00: for minutes so on: ")
timearr = timestring.split(":")
hour = "00"
minute = "00"
seconds = "00"
try:
    hour = int(timearr[0])
except:
    pass
try:
    minute = int(timearr[1])
except:
    pass
try:
    seconds = int(timearr[2])
except:
    pass
if hour != "00" and minute != "00" and seconds != "00":
    time.setTime(hour, minute, seconds)
else:
    if hour != "00":
        time.setHours(hour)
    if minute != "00":
        time.setMinutes(minute)
    if seconds != "00":
        time.setSeconds(seconds)
print(time.showTime())