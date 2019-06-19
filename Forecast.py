#Autoregressive Integrated Moving Average Model

from pandas import read_csv
from pandas import datetime
from pandas import DataFrame
from matplotlib import pyplot
import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm


def main():

    data  = read_csv('testy.csv', header = 1,index_col=0, squeeze=True,)
    ####GOODDATA2 FOR ITEM 30160HT1#####GOODDATA FOR ITEM 30110J10####
    X = data

    size = int(len(X) * .155)
    #Create variable size which is initialized as only a small portion of the original array X

    train, test = X[0:size], X[size:len(X)] #Introduce Train/Test
    history = [x for x in train] #Train is now the original dataset
    predictions = list()


    #Proceed with ARIMA Forecating Algo
    for t in range(len(test)):
        model = ARIMA(history, order=(2,1,0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()[0]
        yhat = output[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)
        print('predicted=%f, expected =%f' % (yhat,obs))

    #Create a sum of the Predicted and Historical values of the past in order to compare totals.
    predsum = sum(predictions)
    hissum = sum(history)

    print('Sum of predicted is = %f ::: Sum of observed is = %f' % (predsum,hissum))

    #PLOT PREDICTIONS
    model_fit.plot_predict(dynamic=False)

    error = mean_squared_error(test, predictions)
    print('Test MSE: %.3f' % error)

    #PLOT HISTORY
    pyplot.plot(test, label= "Witnessed Sales for Item 30160HT1") ##MONDAY 17 ---------- 646      PREDICTED: 900-100
    pyplot.plot(predictions, color='red', label = "Computer-Taught Predicted Sales 30160HT1")

    pyplot.legend(loc = 'upper left')
    pyplot.ylabel('Sales Quantity')
    pyplot.xlabel('Elapsed Time from 1/1/14-5/1/19')
    pyplot.title('Teaching Algorithm for Forecasting Item Purchasing 30160HT1')
    pyplot.grid()
    pyplot.show()
    #y = [MoYrArray, CountArray]


if  __name__ == '__main__':
        main()
