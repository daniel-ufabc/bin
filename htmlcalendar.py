#!/usr/bin/python3

import re
import sys
import calendar

def printTable(month, year, classes):
    cal = calendar.Calendar(calendar.SUNDAY)
    monthnames = {1: 'J A N E I R O', 
                  2: 'F E V E R E I R O', 
                  3: 'M A R &Ccedil; O', 
                  4: 'A B R I L', 
                  5: 'M A I O', 
                  6: 'J U N H O', 
                  7: 'J U L H O', 
                  8: 'A G O S T O', 
                  9: 'S E T E M B R O', 
                  10: 'O U T U B R O', 
                  11: 'N O V E M B R O', 
                  12: 'D E Z E M B R O'}
    tableheader = """        <table class="onemonth">
          <thead> 
            <tr> <th class="monthname" colspan="7">%s</th> </tr>
          </thead>
          <tbody>
            <tr>
              <td class="header_holyday">DOM</td>
              <td class="header_weekday">SEG</td>
              <td class="header_weekday">TER</td>
              <td class="header_weekday">QUA</td>
              <td class="header_weekday">QUI</td>
              <td class="header_weekday">SEX</td>
              <td class="header_weekday">SAB</td>
            </tr>
            <tr style="height: 6px;"> <td colspan="7"> </td> </tr>""" 
    print(tableheader % monthnames[month])

    weekcount = 0
    for i, day in cal.itermonthdays2(year, month):
        if day == 6:
            print('            <tr>')
            print('              <td class="holyday"> ', end = "")
        else:
            if classes[day] == True and i != 0:
                print('              <td class="workday"> ', end = "")
            else:
                print('              <td class="weekday"> ', end = "")
        if i == 0:
            print('&nbsp; </td>')
        else:
            print(str(i) + ' </td>')
        if day == 5:
            print('            </tr>')   
            weekcount += 1

    if weekcount < 6:
        extraweek = """            <tr>
              <td class="holyday"> &nbsp; </td>
              <td class="weekday"> &nbsp; </td>
              <td class="weekday"> &nbsp; </td>
              <td class="weekday"> &nbsp; </td>
              <td class="weekday"> &nbsp; </td>
              <td class="weekday"> &nbsp; </td>
              <td class="weekday"> &nbsp; </td>
            </tr>"""
        print(extraweek)
 
    tablefooter = """          </tbody>
        </table>"""
    print(tablefooter)

def main():
    true_value_list = ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh', 'sim', 'ano']
    startdate = ""
    finaldate = ""

#    valid = re.compile(r"^([0-9]{4})/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|30|31)$")
    valid = re.compile(r"^([0-9]{4})/(0[1-9]|1[0-2])$")

    while(valid.match(startdate) == None):
        startdate = input("Start date (YYYY/MM): ")

    while(valid.match(finaldate) == None):
        finaldate = input("Final date (YYYY/MM): ")

    sdmatch = valid.match(startdate)
    fdmatch = valid.match(finaldate)

    syear = int(sdmatch.group(1))
    fyear = int(fdmatch.group(1))

    smonth = int(sdmatch.group(2))
    fmonth = int(fdmatch.group(2))

#    sday = int(sdmatch.group(3))
#    fday = int(fdmatch.group(3))
    
    # compare dates to see if startdate < finaldate
    if syear > fyear:
        print("Classes cannot end before they begin!")
        exit()
    elif syear == fyear:
        if smonth > fmonth:
            print("Classes cannot end before they begin!")
            exit()
        elif smonth == fmonth:
            print("Classes during a single month, but ok.")

    print()
    cmon = input("Classes on Mondays [y/N]? ").lower() in true_value_list
    ctue = input("Classes on Tuesdays [y/N]? ").lower() in true_value_list
    cwed = input("Classes on Wednesdays [y/N]? ").lower() in true_value_list
    cthu = input("Classes on Thursdays [y/N]? ").lower() in true_value_list
    cfri = input("Classes on Fridays [y/N]? ").lower() in true_value_list
    csat = input("Classes on Saturdays [y/N]? ").lower() in true_value_list

    classes = (cmon, ctue, cwed, cthu, cfri, csat, False) 

    new_row = """<table align="center">
  <tbody>
    <tr>"""
    end_row = """    </tr>
  </tbody>
</table>"""

    fmonth += 1
    if fmonth == 12:
        fyear += 1

    cdate = [smonth, syear]
    count = 0
    while cdate != [fmonth, fyear]:
        if count % 5 == 0:
            print(new_row)
        print('      <td>')
        printTable(cdate[0], cdate[1], classes)
        print('      </td>')
        count += 1
        cdate[0] += 1
        if cdate[0] == 13:
            cdate[1] += 1
            cdate[0] = 1
        if count % 5 == 4:
            print(end_row)

    if count % 5 != 4:
        print(end_row)
            

    
    



def oldmain():
    if len(sys.argv) == 3:
        makeTable(int(sys.argv[1]), int(sys.argv[2]))
    else:
        msg = """
Usage: htmlcalendar.py <year> <month>
    
    <year>  -- in a 4 digit format (e.g. 2013)
    <month> -- a number from 1 upto 12
"""
        print(msg)

if __name__ == '__main__':
    main()

    
