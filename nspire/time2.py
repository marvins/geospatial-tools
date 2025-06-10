

import time as _time

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


def gmtime():

    #  Get the unix seconds
    unix_secs = _time.clock()

    #  Time Components
    tm = struct_time()
    tm.tm_min  = int( unix_secs / 60 )
    tm.tm_sec  = int( unix_secs - (tm.tm_min * 60) )
    tm.tm_hour = tm.tm_min / 60
    tm.tm_min  = tm.tm_min - (tm.tm_hour / 60)

#    // Calculate days
#    tm.tm_mday = tm.tm_hour / 24
#    tm.tm_hour = tm.tm_hour - (tm.tm_mday * 24) 
#
#  /* Unix time starts in 1970 on a Thursday */
#  year      = 1970;
#  dayOfWeek = 4;
#
#  while(1)
#  {
#    bool     leapYear   = (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0));
#    uint16_t daysInYear = leapYear ? 366 : 365;
#    if (days >= daysInYear)
#    {
#      dayOfWeek += leapYear ? 2 : 1;
#      days      -= daysInYear;
#      if (dayOfWeek >= 7)
#        dayOfWeek -= 7;
#      ++year;
#    }
#    else
#    {
#      tm->tm_yday = days;
#      dayOfWeek  += days;
#      dayOfWeek  %= 7;
#
#      /* calculate the month and day */
#      static const uint8_t daysInMonth[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
#      for(month = 0; month < 12; ++month)
#      {
#        uint8_t dim = daysInMonth[month];
#
#        /* add a day to feburary if this is a leap year */
#        if (month == 1 && leapYear)
#          ++dim;
#
#        if (days >= dim)
#          days -= dim;
#        else
#          break;
#      }
#      break;
#    }
#  }
#
#  tm->tm_sec  = seconds;
#  tm->tm_min  = minutes;
#  tm->tm_hour = hours;
#  tm->tm_mday = days + 1;
#  tm->tm_mon  = month;
#  tm->tm_year = year;
#  tm->tm_wday = dayOfWeek;
#