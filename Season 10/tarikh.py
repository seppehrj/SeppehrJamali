class Date:
    def __init__(self, year, month, day):
        # properties
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}~{self.month}~{self.day}"

year = int(input("Enter the years: "))
month = int(input("Enter the months: "))
day = int(input("Enter the days: "))

date = Date(year, month, day)
print(date)