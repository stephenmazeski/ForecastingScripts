## Scripts maps out shipping loss comparison of various month/year combinations. Wanted to get used to working with this specific data file. Trials only

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
from collections import defaultdict
import os
import glob


columns = defaultdict(list)

def main():

    files = glob.glob('RouteShipLoss/*.csv')
    files2 = pd.read_csv('July 2014.csv', usecols=['Cust paid', 'We paid'])
    files3  = pd.read_csv('March 2019.csv', usecols=['Cust paid', 'We paid'])
    files4  = pd.read_csv('June 2018.csv', usecols=['Cust paid', 'We paid'])


    for f in files:

        g = pd.read_csv(f, usecols=['Cust paid', 'We paid'])

        CustCharge2017 = g['Cust paid']
        WebCharge2017 = g['We paid']

        CustArray2017 = []
        CustArray2017.append(CustCharge2017.values)


        WebArray2017 = []
        WebArray2017.append(WebCharge2017.values)



    CustCharge2014 = files2['Cust paid']
    WebCharge2014 = files2['We paid']

    CustArray2014 = []
    CustArray2014.append(CustCharge2014.values)
    WebArray2014 = []
    WebArray2014.append(WebCharge2014.values)


    CustCharge2019 = files3['Cust paid']
    WebCharge2019 = files3['We paid']

    CustArray2019 = []
    CustArray2019.append(CustCharge2019.values)
    WebArray2019 = []
    WebArray2019.append(WebCharge2019.values)



    CustCharge2018 = files4['Cust paid']
    WebCharge2018 = files4['We paid']

    CustArray2018 = []
    CustArray2018.append(CustCharge2018.values)
    WebArray2018 = []
    WebArray2018.append(WebCharge2018.values)




    for d in range(len(CustArray2017)):
        Difference2017 = []
        Difference2017.append(CustArray2017[d]/WebArray2017[d])

    for c in range(len(CustArray2014)):
        Difference2014 = []
        Difference2014.append(CustArray2014[c]/WebArray2014[c])

    for c in range(len(CustArray2018)):
        Difference2018 = []
        Difference2018.append(CustArray2018[c]/WebArray2018[c])

    for c in range(len(CustArray2019)):
        Difference2019 = []
        Difference2019.append(CustArray2019[c]/WebArray2019[c])


    x = 0
    y = 0
    z = 0
    a = 0


    x = np.nansum(CustArray2014)


    y = np.nansum(CustArray2017)


    z = np.nansum(CustArray2018)


    a = np.nansum(CustArray2019)


    print(x , y, z, a)
    #for f in files:
    xx = len(sum(CustArray2014)) ##Count for Big Array
    yy = len(sum(CustArray2017)) ##Count for Small Array
    zz = len(sum(CustArray2018)) ##Count for Small Array
    aa = len(sum(CustArray2019)) ##Count for Small Array
    print(xx, yy, zz, aa)

    xSampleMean = x/xx
    ySampleMean = y/yy
    zSampleMean = z/zz
    aSampleMean = a/aa

    print("||| Sample mean for optimal percent for September 2017: ", ySampleMean , "||| Sample mean for optimal percent for June 2018: ", zSampleMean , "||| Sample mean for optimal percent for March 2019: ", aSampleMean)
    print("Change from 2017 to 2018 is: ", ySampleMean-zSampleMean)
    print("Change from 2018 to 2019 is: ", zSampleMean-aSampleMean)

    ### Will now calculate the top 20 losses for each split. Here we will do further analysis on the large loss sums of money



#    print(max(sum(Difference2014)))
    plt.scatter(WebArray2014, CustArray2014, s =4, c ='b', label = 'July 2014 Routing')
    plt.scatter(WebArray2017, CustArray2017,s =4,c ='k', label = "Sept 2017 Routing")
    plt.scatter(WebArray2018, CustArray2018,s =4,c ='r', label = "June 2018 Routing")
    plt.scatter(WebArray2019, CustArray2019,s =4,c ='g', label = "March 2019 Routing")
    plt.plot([0,3500], [0,3500], c = 'g', label= "Best Case Scenario")
    plt.plot([0,3500], [0,2800], c = 'y', label= "20% Out of Favor")
    plt.plot([0,3500], [0,2100], c = 'r', label= "40% Out of Favor")
    plt.legend(loc='upper left');

    plt.xlabel('Webstaurant Paid Shipment (USD)')
    plt.ylabel('Customer Paid Shipment (USD)')
    plt.title('Relationship Between Webstaurant Payments for Shipping and Customer Payments (in USD)')

    plt.show()
    #for p in range(len(RatedArray)):
    #    print(RatedArray[p] - ActualArray[p])






    #for i in range(len(Rated)):

if  __name__ == '__main__':
        main()
