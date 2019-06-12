import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
from collections import defaultdict
import os

def main():

    data  = pd.read_csv('RR_Observation.csv', usecols=['OrderNum', 'Threshold', 'Shipping Loss Percent'])

    OrderNum = data['OrderNum']
    Threshold = data['Threshold']
    ShipLoss = data['Shipping Loss Percent']



    OrderNumArray = []
    OrderNumArray.append(OrderNum.values)
    ThresholdArray = []
    ThresholdArray.append(Threshold.values)
    ShipLossArray = []
    ShipLossArray.append(ShipLoss.values)
    placeholder = 0

    ThreshArraySmall = []
    ThreshArrayBig = []





    plt.scatter(ThresholdArray, ShipLossArray, s =4, c ='b', label = 'Orders Placed in Manual Routing')
    plt.plot([10,10], [0,80], c = 'r', label= "$10 Threshold Marker (Current Threshold)")
    plt.plot([0,80], [20,20], c = 'r', label= "20% Out of Favor (Current Threshold)")
    plt.plot([15,15], [0,80], c = 'y', label= "$15 Threshold Marker")
    plt.plot([0,80], [25,25], c = 'y', label= "25% Out of Favor")
    plt.plot([20,20], [0,80], c = 'g', label= "$20 Threshold Marker")
    plt.plot([0,80], [30,30], c = 'g', label= "30% Out of Favor")
#    plt.plot([0,3500], [0,2100], c = 'r', label= "40% Out of Favor")
    plt.legend(loc='upper right');

    plt.xlabel('Shipping Loss in USD')
    plt.ylabel('Percent Shipping Loss')
    plt.title('1/3 of Orders Placed in Manual Roting Review 5/29-5/30 Tracking and Mapping Chart')

    plt.show()






    #for i in range(len(Rated)):

if  __name__ == '__main__':
        main()
