##=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# PROGRAM NAME: logMe.py
# AUTHOR: GARY DAVIS
# DATE: 7/27/2023
# DESCRIPTION: this program takes in a string to be written to the log file
# (datalog.txt)with the date and time that the log was entered.
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
import time
def logMe(message):
    timestamp = time.localtime()
    year = timestamp[0]
    month = timestamp[1]
    day = timestamp[2]
    hour = timestamp[3]
    min = timestamp[4]
    second = timestamp[5]
    outputlog = "["+str(month) + "/" + str(day) + "/" +  str(year) +" ~ " + str(hour) +":"+str(min)+":"+str(second) +"] - "+message
    with open("datalog.txt", "a") as datalog:
        datalog.write("\n")
        datalog.write(outputlog)
        datalog.close()
    return outputlog