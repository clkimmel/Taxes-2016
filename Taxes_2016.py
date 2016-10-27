# import system modules
import os
import math

#Print the welcome message and instructions.
print "This program was developed to calculate your total taxes in North Carolina."
print "North Carolina Tax Calculator © 2016 Charles Kimmel All rights reserved."
print "For use as is and at your own risk." '\n' "The author is not liable for any issues that may arise from using this software."
print '\n'

def start():
    #Define salary
    x = input("Enter your gross salary: ")
    # 10% bracket
    if x <= 9275:
       y = x * 0.1
       p = ((y / x) * 100)
    # 15% bracket
    elif 9275 < x <= 37650:
       m = x - 9275
       i = (9275*0.1)
       y = (m * 0.15) + i
       p = ((y / x) * 100) + ((i / x) * 100)
    # 25% bracket
    elif 37650 < x <= 91150:
       m = x - 37650
       i = (9275*0.1)
       ii = ((37650 - 9275) * 0.15)       
       y = i + ii + (m * 0.25)
       p = ((y / x) * 100) + ((i / x) * 100) + ((ii / x) * 100)
    # 28% bracket
    elif 91150 < x <= 190150:
       m = x - 91150
       i = (9275*0.1)
       ii = ((37650 - 9275) * 0.15)
       iii = ((91150 - 37650) * 0.25)
       y = i + ii + iii + (m * 0.28)
       p = ((y / x) * 100) + ((i / x) * 100) + ((ii / x) * 100) + ((iii / x) * 100)
    # 33% bracket
    elif 190150 < x <= 413350:
       m = x - 190150
       i = (9275*0.1)
       ii = ((37650 - 9275) * 0.15)
       iii = ((91150 - 37650) * 0.25)
       iv = ((190150 - 91150) * 0.28)
       y = i + ii + iii + iv + (m * 0.33)
       p = ((y / x) * 100) + ((i / x) * 100) + ((ii / x) * 100) + ((iii / x) * 100) + ((iv / x) * 100)
    # 35% bracket
    elif 413350 < x <= 415050:
       m = x - 413350
       i = (9275*0.1)
       ii = ((37650 - 9275) * 0.15)
       iii = ((91150 - 37650) * 0.25)
       iv = ((190150 - 91150) * 0.28)
       v = ((413350 - 190150) * 0.33)
       y = i + ii + iii + iv + v + (m * 0.35)
       p = ((y / x) * 100) + ((i / x) * 100) + ((ii / x) * 100) + ((iii / x) * 100) + ((iv / x) * 100) + ((v / x) * 100)
    # 39% bracket
    elif x > 415050:
       m = x - 413350
       i = (9275*0.1)
       ii = ((37650 - 9275) * 0.15)
       iii = ((91150 - 37650) * 0.25)
       iv = ((190150 - 91150) * 0.28)
       v = ((413350 - 190150) * 0.33)
       vi = ((415050 - 413350) * 0.35)
       y = i + ii + iii + iv + v + vi + (m * 0.396)
       p = ((y / x) * 100) + ((i / x) * 100) + ((ii / x) * 100) + ((iii / x) * 100) + ((iv / x) * 100) + ((v / x) * 100) + ((vi / x) * 100)
    # Give one space.
    print "\n"
    
    # Net Income.
    Net = x - y
    # Net Income.
    biw = (Net / 26)
    mo = (Net / 12)
    # Calculate State Taxes.
    State = x * 0.055
    # Calculate Social Security Tax.
    SS = x * 0.062
    # Calculated Total Tax.
    T = y + State + SS
    # Calculated Total Tax Percentage.
    tst = ((State/x) * 100)
    tss = ((SS/x) * 100)
    TP = p + tst + tss
   

    print "//////////////////////////////////////////////////////////////"
    print "Net Income: %s"%('$'+str(round(Net,2)))
    print "Monthy Paycheck: %s"%('$'+str(round(mo,2)))
    print "Bi-Weekly Paycheck: %s"%('$'+str(round(biw,2)))
    print "//////////////////////////////////////////////////////////////"
    print "\n"
    print "**************************************************************"
    print "Total Tax Burden: %s"%('$'+str(round(T,2)))
    print "Total Federal Taxes: %s"%('$'+str(round(y,2)))
    print "Total State Taxes: %s"%('$'+str(round(State,2)))
    print "Total Social Security: Tax %s"%('$'+str(round(SS,2)))
    print "**************************************************************"
    print "\n"
    print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"    
    print "Federal Tax Percentage: %s"%(str(round(p,2))+"%")
    print "State Tax Percentage: %s"%(str(round(tst,2))+"%")
    print "Social Security Tax Percentage: %s"%(str(round(tss,2))+"%")
    print "Total Tax Percentage: %s"%(str(round(TP,2))+"%")
    print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    
# Restart program and give one space.
    print "\n"

n = -1

while n < 0:
 start ()
