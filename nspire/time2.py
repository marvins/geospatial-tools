#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#*                                                                                    *#
#*                           Copyright (c) 2025 Terminus LLC                          *#
#*                                                                                    *#
#*                                All Rights Reserved.                                *#
#*                                                                                    *#
#*          Use of this source code is governed by LICENSE in the repo root.          *#
#*                                                                                    *#
#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#

#  Python Libraries
import time as _time

#  Constants
SECS_PER_MIN  = 60
SECS_PER_HOUR = 3600
SECS_PER_DAY  = 86400

class struct_time:
   
    def __init__(self):
        self.tm_year  = None
        self.tm_mon   = None
        self.tm_mday  = None
        self.tm_hour  = None
        self.tm_min   = None
        self.tm_sec   = None
        self.tm_wday  = None
        self.tm_yday  = None
        self.tm_isdst = None

    def __str__(self):
      output = '( yr: ' + str(self.tm_year) + \
             ', mo: ' + str(self.tm_mon) + \
            ', mday: ' + str(self.tm_mday) + \
            ', hour: ' + str(self.tm_hour) + \
            ', min: ' + str(self.tm_min) + \
            ', sec: ' + str(self.tm_sec) + \
            ', wday: ' + str(self.tm_wday) + \
            ', yday: ' + str(self.tm_yday) + \
            ', isdst: ' + str(self.tm_isdst)
      return output

DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def is_leap_year( y ):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

def days_in_month(y, m):
    # year, month -> number of days in that month in that year.
    if m == 2 and is_leap_year(y):
        return 29
    return DAYS_IN_MONTH[m]

def gmtime():

    #  Get the unix seconds
    secs = _time.clock()
    print('secs: ', secs, ', lt: ', _time.localtime())
    
    #  Time Components
    tm = struct_time()
    
    tm.tm_sec  = int( secs ) % 60
    tm.tm_min  = int( secs / 60) % 60
    
    # Calculate days
    tm.tm_yday = int( int( secs ) / SECS_PER_DAY )

    tm.tm_hour = int( ( int( secs ) % SECS_PER_DAY ) / 3600 )
    print('Part 1: ', int(secs)%SECS_PER_DAY, ', tm hour: ', tm.tm_hour)
    
    #  Unix time starts in 1970 on a Thursday
    tm.tm_year = 1970
    dy_in_yr = 365
    dayOfWeek = 4

    #  Next, we resolve the year
    while tm.tm_yday > dy_in_yr:
        
        # If it's greater, than subtract this years day and do the next
        tm.tm_yday -= dy_in_yr

        dy_in_yr = 365
        if is_leap_year( tm.tm_year + 1 ):
          dy_in_yr = 366

        tm.tm_year += 1


    #  Now the month
    tm.tm_mday = tm.tm_yday
    tm.tm_mon  = 1
    while True:

        dim = days_in_month( tm.tm_year, tm.tm_mon )
        if tm.tm_mday <= dim:
            break
        tm.tm_mday -= dim
        tm.tm_mon += 1


    return tm

