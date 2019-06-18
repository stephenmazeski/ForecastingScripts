#visual aid for shipping loss over past five months.

import matplotlib.pylab as plt
import numpy as np
import pandas as pd
import csv
from collections import defaultdict
import os
import glob
from scipy import stats


#columns = defaultdict(list)

def main():

    Dec2018File = pd.read_csv(r'RecentShipLoss\Dec 2018.csv', usecols=['Cust paid', 'We paid', 'no'])
    Jan2019File  = pd.read_csv(r'RecentShipLoss\Jan 2019.csv', usecols=['Cust paid', 'We paid', 'no'])
    Feb2019File  = pd.read_csv(r'RecentShipLoss\Feb 2019.csv', usecols=['Cust paid', 'We paid', 'no'])
    March2019File  = pd.read_csv(r'RecentShipLoss\March 2019.csv', usecols=['Cust paid', 'We paid', 'no'])
    April2019File  = pd.read_csv(r'RecentShipLoss\April 2019.csv', usecols=['Cust paid', 'We paid', 'no'])


###DECEMBER 2018####
    C_Charge_Dec2018 = Dec2018File['Cust paid']
    W_Charge_Dec2018 = Dec2018File['We paid']
    no_Dec2018 = Dec2018File['no']

    C_Array_Dec2018 = []
    C_Array_Dec2018.append(C_Charge_Dec2018.values)
    W_Array_Dec2018 = []
    W_Array_Dec2018.append(W_Charge_Dec2018.values)
    no_Array_Dec2018 = []
    no_Array_Dec2018.append(no_Dec2018.values)

###January 2019####
    C_Charge_Jan2019 = Jan2019File['Cust paid']
    W_Charge_Jan2019 = Jan2019File['We paid']
    no_Jan2019 = Jan2019File['no']

    C_Array_Jan2019 = []
    C_Array_Jan2019.append(C_Charge_Jan2019.values)
    W_Array_Jan2019 = []
    W_Array_Jan2019.append(W_Charge_Jan2019.values)
    no_Array_Jan2019 = []
    no_Array_Jan2019.append(no_Jan2019.values)

###February 2019####
    C_Charge_Feb2019 = Feb2019File['Cust paid']
    W_Charge_Feb2019 = Feb2019File['We paid']
    no_Feb2019 = Feb2019File['no']

    C_Array_Feb2019 = []
    C_Array_Feb2019.append(C_Charge_Feb2019.values)
    W_Array_Feb2019 = []
    W_Array_Feb2019.append(W_Charge_Feb2019.values)
    no_Array_Feb2019 = []
    no_Array_Feb2019.append(no_Feb2019.values)

###March 2019####
    C_Charge_Mar2019 = March2019File['Cust paid']
    W_Charge_Mar2019 = March2019File['We paid']
    no_March2019 = March2019File['no']

    C_Array_Mar2019 = []
    C_Array_Mar2019.append(C_Charge_Mar2019.values)
    W_Array_Mar2019 = []
    W_Array_Mar2019.append(W_Charge_Mar2019.values)
    no_Array_Mar2019 = []
    no_Array_Mar2019.append(no_March2019.values)

###DECEMBER 2018####
    C_Charge_Apr2019 = April2019File['Cust paid']
    W_Charge_Apr2019 = April2019File['We paid']
    no_April2019 = April2019File['no']

    C_Array_Apr2019 = []
    C_Array_Apr2019.append(C_Charge_Apr2019.values)
    W_Array_Apr2019 = []
    W_Array_Apr2019.append(W_Charge_Apr2019.values)
    no_Array_April2019 = []
    no_Array_April2019.append(no_April2019.values)




    for d in range(len(C_Array_Dec2018)):
        DifferenceDec2018 = []
        DifferenceDec2018.append(W_Array_Dec2018[d]-C_Array_Dec2018[d])

    for d in range(len(C_Array_Jan2019)):
        DifferenceJan2019 = []
        DifferenceJan2019.append(W_Array_Jan2019[d]-C_Array_Jan2019[d])

    for d in range(len(C_Array_Feb2019)):
        DifferenceFeb2019 = []
        DifferenceFeb2019.append(W_Array_Feb2019[d]-C_Array_Feb2019[d])

    for d in range(len(C_Array_Mar2019)):
        DifferenceMar2019 = []
        DifferenceMar2019.append(W_Array_Mar2019[d]-C_Array_Mar2019[d])

    for d in range(len(C_Array_Apr2019)):
        DifferenceApr2019 = []
        DifferenceApr2019.append(W_Array_Apr2019[d]-C_Array_Apr2019[d])


    SumDec2018 = 0
    SumJan2019 = 0
    SumFeb2019 = 0
    SumMar2019 = 0
    SumApr2019 = 0

    for i in range(len(C_Array_Dec2018)):
        SumDec2018 = np.nansum(W_Array_Dec2018[i]-C_Array_Dec2018[i])


    for i in range(len(C_Array_Jan2019)):
        SumJan2019 = np.nansum(W_Array_Jan2019[i]-C_Array_Jan2019[i])


    for i in range(len(C_Array_Feb2019)):
        SumFeb2019 = np.nansum(W_Array_Feb2019[i]-C_Array_Feb2019[i])


    for i in range(len(C_Array_Mar2019)):
        SumMar2019 = np.nansum(W_Array_Mar2019[i]-C_Array_Mar2019[i])


    for i in range(len(C_Array_Apr2019)):
        SumApr2019 = np.nansum(W_Array_Apr2019[i]-C_Array_Apr2019[i])


#    print(SumDec2018 , SumJan2019, SumFeb2019, SumMar2019, SumApr2019)
    #for f in files:


    kwargs = dict(histtype='stepfilled', alpha=0.13, normed=True, bins=20)

#    print(max(sum(Difference2014)))
    plt.hist(DifferenceDec2018,**kwargs)
    plt.hist(DifferenceJan2019,**kwargs)
    plt.hist(DifferenceFeb2019,**kwargs)
    plt.hist(DifferenceMar2019,**kwargs)
    plt.hist(DifferenceApr2019,**kwargs)

#    plt.plot([0,3500], [0,3500], c = 'g', label= "Best Case Scenario")
#    plt.plot([0,3500], [0,2800], c = 'y', label= "20% Out of Favor")
#    plt.plot([0,3500], [0,2100], c = 'r', label= "40% Out of Favor")
#    plt.plot(W_Array_Dec2018,C_Array_Dec2018)
    plt.legend(loc='upper left');

    plt.xlabel('Webstaurant Paid Shipment (USD)')
    plt.ylabel('Customer Paid Shipment (USD)')
    plt.title('Relationship Between Webstaurant Payments for Shipping and Customer Payments (in USD)')
    plt.grid()
    plt.show()
    #for p in range(len(RatedArray)):
    #    print(RatedArray[p] - ActualArray[p])






    #for i in range(len(Rated)):

if  __name__ == '__main__':
        main()
