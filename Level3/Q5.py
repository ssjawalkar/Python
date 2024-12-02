class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        total_minutes = total_minutes % 60
        return Time(total_hours, total_minutes)

    def displayTime(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

    def displayMinutes(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"Total minutes: {total_minutes}")


time1 = Time(2, 50)
time2 = Time(1, 20)

time1.displayTime() 
time2.displayTime()  

added_time = time1.addTime(time2)
added_time.displayTime()

added_time.displayMinutes() 
