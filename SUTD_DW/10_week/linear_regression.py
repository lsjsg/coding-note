import numpy as np
from sklearn import linear_model 
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def linear_regression(bunchobject, x_index, y_index, size, seed):
    X=bunchobject.data[:,[x_index]]
    Y=bunchobject.data[:,[y_index]]
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=size,random_state=seed)
    regr=linear_model.LinearRegression().fit(X_train,Y_train)
    y_predict=regr.predict(X_test)
    MSE=mean_squared_error(Y_test,y_predict)
    R2_score=r2_score(Y_test,y_predict)
    coefficients=regr.coef_
    intercept=regr.intercept_
    results={'coefficients':coefficients,'mean squared error':MSE,'r2 score':R2_score,'intercept':intercept}
    return X_train, Y_train, X_test, y_predict, results