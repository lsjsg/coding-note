
def processing(time,tem):
    gap = []
    for i in range(1,len(tem)):
        gap.append(abs(tem[i]-tem[i-1]))
    gap = np.array(gap)
    def trans(k,t):
        ret = 0
        for i in range(100):
            ret += k * np.exp((100-t)*(coef)+intercept)
        return ret
    expo = []
    for i in range(len(time)-1):
        expo.append(trans(gap[i],time[i]))
    x = np.array(expo).reshape(len(expo),1)
    y = tem[1:]
    return x,y
#     print(x)
#     expo = np.exp((100-time[1:])*coef+intercept)

#     gap = gap.reshape(gap.shape[0],1)
#     x = []
#     print(gap.shape)
#     print(expo.shape)
# print(processing(time,tem))
    
        
#     x = gap.T * expo
#     y = tem[1:].reshape(tem[1:].shape[0],1)
#     x = x.reshape(x.shape[1],1)
#     return x,y
x,y = processing(np.array(result["temperature0"]),np.array(result["time0"]))
x_test,y_test = processing(np.array(result["temperature1"]),np.array(result["time1"]))

def temper(x,y,x_test,y_test):
    model = linear_model.LinearRegression().fit(x,y)
    pred = model.predict(x_test)
    MSE=mean_squared_error(y_test,pred)
    R2_score=r2_score(y_test,pred)
    return model,model.coef_,model.intercept_,MSE,R2_score

print(temper(x,y,x_test,y_test))
# model = temp(x,y,x_test,y_test)[0]
# print(x)