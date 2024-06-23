class CalendarGenerator:
    def __init__(self):
        self.label = "Sun Mon Tue Wed Thu Fri Sat"

    def zeller_algorithm(self, year, month):
        if month < 3:
            month += 12
            year -= 1
        c = year // 100
        y = year - 100 * c
        m = month
        d = 1
        w = (13 * (m + 1) // 5 + y // 4 + c // 4 + d + y - 2 * c) % 7
        return w

    def generate_calendar(self, year, month):
        print(self.label)

        if month in [1, 3, 5, 7, 8, 10, 12]:
            index = 31
        elif month in [4, 6, 9, 11]:
            index = 30
        elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            index = 29
        else:
            index = 28

        w = self.zeller_algorithm(year, month)

        if w == 0:
            row1 = " " * (len(self.label) - 3) + "01"
        else:
            row1 = " " * 4 * (w - 1) + "01"

        date = 2
        l = len(row1)
        while l < (len(self.label) - 1):
            row1 += " " * 2 + f"{date:02d}"
            l += 4
            date += 1
        print(row1)

        i = date 
        while i < (index + 1) :
            if (i + w - 1) % 7 == 0:
                print(f"{i:02d}")
            else:
                print(f"{i:02d}", end="  ")
            i += 1

# Main program
while True:
    year = input("Please input year: ")
    month = input("Please input month: ")
    if year.isdigit() and month.isdigit():
        year = int(year)
        month = int(month)
        calendar = CalendarGenerator()
        calendar.generate_calendar(year, month)
        break
    else:
        print("Invalid value! Please enter an integer.")
