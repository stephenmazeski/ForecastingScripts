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

    Dec2018File = pd.read_csv(r'RecentShipLoss\Dec 2018.csv', usecols=['Cust paid', 'We paid'])
    Jan2019File  = pd.read_csv(r'RecentShipLoss\Jan 2019.csv', usecols=['Cust paid', 'We paid'])
    Feb2019File  = pd.read_csv(r'RecentShipLoss\Feb 2019.csv', usecols=['Cust paid', 'We paid'])
    March2019File  = pd.read_csv(r'RecentShipLoss\March 2019.csv', usecols=['Cust paid', 'We paid'])
    April2019File  = pd.read_csv(r'RecentShipLoss\April 2019.csv', usecols=['Cust paid', 'We paid'])


###DECEMBER 2018####
    C_Charge_Dec2018 = Dec2018File['Cust paid']
    W_Charge_Dec2018 = Dec2018File['We paid']

    C_Array_Dec2018 = []
    C_Array_Dec2018.append(C_Charge_Dec2018.values)
    W_Array_Dec2018 = []
    W_Array_Dec2018.append(W_Charge_Dec2018.values)

###January 2019####
    C_Charge_Jan2019 = Jan2019File['Cust paid']
    W_Charge_Jan2019 = Jan2019File['We paid']

    C_Array_Jan2019 = []
    C_Array_Jan2019.append(C_Charge_Jan2019.values)
    W_Array_Jan2019 = []
    W_Array_Jan2019.append(W_Charge_Jan2019.values)


###February 2019####
    C_Charge_Feb2019 = Feb2019File['Cust paid']
    W_Charge_Feb2019 = Feb2019File['We paid']

    C_Array_Feb2019 = []
    C_Array_Feb2019.append(C_Charge_Feb2019.values)
    W_Array_Feb2019 = []
    W_Array_Feb2019.append(W_Charge_Feb2019.values)


###March 2019####
    C_Charge_Mar2019 = March2019File['Cust paid']
    W_Charge_Mar2019 = March2019File['We paid']

    C_Array_Mar2019 = []
    C_Array_Mar2019.append(C_Charge_Mar2019.values)
    W_Array_Mar2019 = []
    W_Array_Mar2019.append(W_Charge_Mar2019.values)


###DECEMBER 2018####
    C_Charge_Apr2019 = April2019File['Cust paid']
    W_Charge_Apr2019 = April2019File['We paid']

    C_Array_Apr2019 = []
    C_Array_Apr2019.append(C_Charge_Apr2019.values)
    W_Array_Apr2019 = []
    W_Array_Apr2019.append(W_Charge_Apr2019.values)





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


    print(SumDec2018 , SumJan2019, SumFeb2019, SumMar2019, SumApr2019)
    #for f in files:
    Count_Dec2018 = len(sum(C_Array_Dec2018)) ##Count for Dec2018
    Count_Jan2019 = len(sum(C_Array_Jan2019)) ##Count for Jan2019
    Count_Feb2019 = len(sum(C_Array_Feb2019)) ##Count for Feb2019
    Count_Mar2019 = len(sum(C_Array_Mar2019)) ##Count for Mar2019
    Count_Apr2019 = len(sum(C_Array_Apr2019)) ##Count for Apr2019
    print(Count_Dec2018, Count_Jan2019, Count_Feb2019, Count_Mar2019, Count_Apr2019)

    Dec2018SampleMean = SumDec2018/Count_Dec2018
    Jan2019SampleMean = SumJan2019/Count_Jan2019
    Feb2019SampleMean = SumFeb2019/Count_Feb2019
    Mar2019SampleMean = SumMar2019/Count_Mar2019
    Apr2019SampleMean = SumApr2019/Count_Apr2019



    std_Dec2018 = np.std(DifferenceDec2018)
    std_Jan2019 = np.std(DifferenceJan2019)
    std_Feb2019 = np.std(DifferenceFeb2019)
    std_Mar2019 = np.std(DifferenceMar2019)
    std_Apr2019 = np.std(DifferenceApr2019)

    print(std_Dec2018,std_Jan2019,std_Feb2019,std_Mar2019,std_Apr2019)

    Threshold = 2.99

    ##Z score Dec2018
    dec_out = []
    for y in DifferenceApr2019:
        dec_z = (y - Apr2019SampleMean)/std_Apr2019
#    print(DifferenceDec2018)
    print(dec_z)
    outlier = []
    for a in dec_z:
        if abs(a) > Threshold:
            outlier.append(a)

    print(len(outlier))




    print("||| Sample mean for optimal percent for December 2018: ", Dec2018SampleMean , "\n||| Sample mean for optimal percent for January 2019: ", Jan2019SampleMean , "\n||| Sample mean for optimal percent for February 2019: ", Feb2019SampleMean, "\n||| Sample mean for optimal percent for March 2019: ", Mar2019SampleMean, "\n||| Sample mean for optimal percent for April 2019: ", Apr2019SampleMean)
#    print("Change from 2017 to 2018 is: ", ySampleMean-zSampleMean)
#    print("Change from 2018 to 2019 is: ", zSampleMean-aSampleMean)

    ### Will now calculate the top 20 losses for each split. Here we will do further analysis on the large loss sums of money


#    print(max(sum(Difference2014)))
    plt.scatter(W_Array_Dec2018, C_Array_Dec2018, s =4, c ='b', label = 'December 2018 Routing')
    plt.scatter(W_Array_Jan2019, C_Array_Jan2019,s =4,c ='k', label = "January 2019 Routing")
    plt.scatter(W_Array_Feb2019, C_Array_Feb2019,s =4,c ='r', label = "February 2019 Routing")
    plt.scatter(W_Array_Mar2019, C_Array_Mar2019,s =4,c ='g', label = "March 2019 Routing")
    plt.scatter(W_Array_Apr2019, C_Array_Apr2019,s =4,c ='y', label = "April 2019 Routing")

    plt.plot([0,3500], [0,3500], c = 'g', label= "Best Case Scenario")
    plt.plot([0,3500], [0,2800], c = 'y', label= "20% Out of Favor")
    plt.plot([0,3500], [0,2100], c = 'r', label= "40% Out of Favor")
    plt.plot(W_Array_Dec2018,C_Array_Dec2018)
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
