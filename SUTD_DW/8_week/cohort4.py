"""
class Line:
    def __init__(self,c0,c1):
        self.c0 = c0
        self.c1 = c1
    def __call__(self,x):
        return self.c0 + x*self.c1
    def table(self,L,R,n):
        x,y,ret = [],[],''
        if L == R:
            x.append(float(L))
            y.append(round(float(self.c0+L*self.c1),2))
        elif n != 0:
            step = (R-L)/(n-1)
            for i in range(n):
                tmp = float(L + i * step)
                x.append(round(tmp,2))
                y.append(round(self.c0 + tmp*self.c1,2))
        else:
            return "Error in printing table"
        for i in range(len(x)):
            left = "{:.2f}".format(x[i])
            right = "{:.2f}".format(y[i])
            ret += "{:>10}".format(left) + "{:>10}\n".format(right)
        return ret
"""
class Line:
    def __init__(self,c0,c1):
    	self.c0=c0
    	self.c1=c1
    def __call__(self,x):
    	return float(self.c0+self.c1*x)
    def table(self,L,R,n):
    	if n==0:
    		return 'Error in printing table'
    	elif L == R:
    		x= '{:.2f}'.format(L)
    		y='{:.2f}'.format(self(L))
    		return '{:>10}'.format(x)+ '{:>10}'.format(y)+'\n'
    	else:
    		table=''
    		for i in range(n):
    			x='{:.2f}'.format(L+i*(R-L)/(n-1))
    			y='{:.2f}'.format(self(L+i*(R-L)/(n-1)))
    			table+='{:>10}'.format(x)+'{:>10}'.format(y)+'\n'
    		return table