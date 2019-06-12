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

    data  = read_csv('GOODDATA.csv', header = 1,index_col=0, squeeze=True,)
    ####GOODDATA2 FOR ITEM 30160HT1#####GOODDATA FOR ITEM 30110J10####
    X = data

    size = int(len(X) * .268)#268
    train, test = X[0:size], X[size:len(X)]
    history = [x for x in train]
    predictions = list()
    for t in range(len(test)):
        model = ARIMA(history, order=(1,0,0))
        model_fit = model.fit(disp=0)
#    print(model_fit.summary())
        output = model_fit.forecast()[0]
        yhat = output[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)
        print('predicted=%f, expected =%f' % (yhat,obs))

    #pred_uc = model_fit.forecast(steps=10)
#    pred_ci = pred_uc.conf_int()


    model_fit.plot_predict(5)

    error = mean_squared_error(test, predictions)
    print('Test MSE: %.3f' % error)


    #pyplot.plot(pred_uc, color = 'b', label = "Predicted")
#    pyplot.plot(v, color = 'b')
    pyplot.plot(test, label= "Witnessed Sales for Item 30110J10")
    pyplot.plot(predictions, color='red', label = "Computer-Taught Predicted Sales 30110J10")

    pyplot.legend(loc = 'upper left')
    pyplot.ylabel('Sales Quantity')
    pyplot.xlabel('Elapsed Time from 5/1/14-5/1/19')
    pyplot.title('Teaching Algorithm for Forecasting Item Purchasing 30110J10')
    pyplot.grid()
    pyplot.show()
    #y = [MoYrArray, CountArray]
#    plt.scatter(MoYrArray, CountArray, s =4, c ='b', label = 'Test')

#    plt.show()






    #for i in range(len(Rated)):

if  __name__ == '__main__':
        main()
