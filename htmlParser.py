import os
from bs4 import BeautifulSoup
from datetime import datetime


class getShiftDates:
    def __init__(self):
        page = open("./storedData/full_page.html", "r")
        html = page
        parsed_html = BeautifulSoup(html, "html.parser")


        # <div class="calendarShift">

        # print(parsed_html.body.find_all("div", attrs={"class" : "calendarDay"})) # this is all calander days shown

        allDays = parsed_html.body.find_all("div", attrs={"class" : "calendarDay"})

        self.shifts = []



        for day in allDays:
            workDay = day.find("h3")
            shift = day.find("div", attrs={"class" : "times ellipsis"})
            if shift != None:
                current = workDay.text + " " + shift.text
                self.shifts.append(datetime.strptime(current, '%d %b %Y %H:%M'))
                # print("Shift on", workDay.text, "at", shift.text, "pm")

        pass
    def getShifts(self):
        return self.shifts
    