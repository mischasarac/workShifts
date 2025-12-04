from workRequest import getWorkHTML
from htmlParser import getShifts
from calendarInteractions import addShiftsToCalendar
from validateNewShifts import validateNewShifts


if __name__ == "__main__":
    pageHTML = getWorkHTML()

    upComingShifts = getShifts(pageHTML)

    newShifts = validateNewShifts(upComingShifts)

    # print(newShifts)

    if not newShifts:
        print("No new shifts to append")
    else:
        print("adding shifts")
        addShiftsToCalendar(upComingShifts)
