from math import exp
def approx_ode(h,t0,y0,tn):
    # Inputs - h  : step size
    #          t0 : initial t value (at step 0)
    #          y0 : initial y value (at step 0)
    #          tn : t value at step n
    # Add your code below!
    t,y=t0,y0
    while t < tn - 1e-5:
        y += h * (3 + exp(-t) - y/2)
        t += h
    return round(y,3)