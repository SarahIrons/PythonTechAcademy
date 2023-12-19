##DATETIME CHALLENGE
##The Portland-based company you work for just opened two new branches. One is in New York City, the other in London. They need a very simple program to find out if the branches are open or closed. The hours of both branches are 9:00 a.m.-5:00 p.m. in their own time zone.
##Using IDLE, create a new file.
##Import the datetime module and any others to aid in time zone calculations.
##Create a script that will find out the current times in the Portland HQ and NYC and London branches. Then, compare that time with each branch's hours to see if they are open or closed.
##Print out to the screen the three branches and whether they are open or closed.


##Import the datetime module and any others to aid in time zone calculations.
from datetime import datetime
from datetime import datetime, timedelta
from pytz import timezone
import pytz
utc = pytz.utc


#current Datetime
unaware = datetime. now()
print("Timezone naive:", unaware)

#Standard UTC timezone aware Datetime
aware =datetime. now(pytz.utc)
print("Timezone Aware:" , aware)

#Portland HQ time zone is Pacific standard time UTC -8PST
#pacific time print line 29
dt_us_pacific = datetime.now(pytz.timezone('America/Tijuana'))
print("US Pacific timezone DateTime:", dt_us_pacific.strftime("%Y:%m:%d %H:%M:%S %Z %z"))

#NYC time zone is -5 UTC
#London time zone is ==UTC
#eastern time print line 35
dt_us_eastern = datetime.now(pytz.timezone('America/New_York'))
print("US Eastern timezone DateTime:", dt_us_eastern.strftime("%Y:%m:%d %H:%M:%S %Z %z"))

#local UK time (also UTC time) print line 39
dt_uk = datetime.now(pytz.timezone('Europe/London'))
print("Uk DateTime:", dt_uk.strftime("%Y:%m:%d %H:%M:%S %Z %z"))


##Create a script that will find out the current times in the Portland HQ and NYC and London branches. Then, compare that time with each branch's hours to see if they are open or closed.
##Print out to the screen the three branches and whether they are open or closed.


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
