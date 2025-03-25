from bs4 import BeautifulSoup
from datetime import datetime


def getShifts(html):
    # page = open("../storedData/full_page.html", "r")
    # html = page
    parsed_html = BeautifulSoup(html, "html.parser")


    # <div class="calendarShift">

    # print(parsed_html.body.find_all("div", attrs={"class" : "calendarDay"})) # this is all calander days shown

    allDays = parsed_html.body.find_all("div", attrs={"class" : "calendarDay"})

    shifts = []


    now = datetime.utcnow()

    for day in allDays:
        workDay = day.find("h3")
        shift = day.find("div", attrs={"class" : "times ellipsis"})
        if shift != None:
            current = workDay.text + " " + shift.text
            date = datetime.strptime(current, '%d %b %Y %H:%M')
            if(date >= now):
                shifts.append(date)
            # print("Shift on", workDay.text, "at", shift.text, "pm")

    return shifts
    