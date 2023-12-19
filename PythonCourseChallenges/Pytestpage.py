
from datetime import datetime, timedelta
from pytz import timezone


opening = datetime(2010, 1, 1, 9, 0, 0)  # 9AM
closing = datetime(2010, 1, 1, 17, 0, 0)  # 5PM

def weOpen(timeChecked, place):
    print("Time now is: " + str(timeChecked.time()) + " in " + str(place))
    print("That means we're open!")

def weClosed(timeChecked, place): 
    print("Time now is :" + str(timeChecked.time()) + " in " + str(place))
    print("That means we're closed!")

def checkCity(timeChecked, place): 
    if opening.time()< timeChecked.time() < closing.time() and timeChecked.isoweekday() in range(1,6):
        weOpen(timeChecked, place) 
    else:
        weClosed(timeChecked, place)

def checkTime():

    timeNow = datetime.now()
    NY = datetime.now(timezone('America/New_York'))
    Portland = datetime.now(timezone('America/Tijuana'))
    London = datetime.now(timezone('Europe/London'))

    checkCity(NY, "New York")
    checkCity(Portland, "Portland")
    checkCity(London, "London")


checkTime()

