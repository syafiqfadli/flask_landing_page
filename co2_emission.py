import pandas as pd
import numpy as np
import pickle

from sklearn import linear_model


def co2_emission():
    df = pd.read_csv("FuelConsumptionCo2.csv")
    cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]

    msk = np.random.rand(len(df)) < 0.8
    train = cdf[msk]

    regr = linear_model.LinearRegression()
    train_x = np.asanyarray(train[['ENGINESIZE']])
    train_y = np.asanyarray(train[['CO2EMISSIONS']])
    regr.fit(train_x, train_y)

    file = open('model.pkl', 'wb')
    pickle.dump(regr, file)
    file.close()


co2_emission()
