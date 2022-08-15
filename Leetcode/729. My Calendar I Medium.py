class MyCalendar(object):
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for x, y in self.calendar:
            print(x,y)
            print(self.calendar)
            if x < end and start < y:
                return False
        self.calendar.append([start, end])
        return True