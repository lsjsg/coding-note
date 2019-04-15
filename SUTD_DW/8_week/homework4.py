class Polynomial:
    def __init__(self, coeff):
        self.coeff = coeff

    def __add__(self, other):
        if len(self.coeff) > len(other.coeff):
            ret, para = self.coeff[:], other.coeff[:]
        else:
            ret, para = other.coeff[:], self.coeff[:]
        for i in range(len(para)):
            ret[i] += para[i]
        return Polynomial(ret)

    def __sub__(self, other):
        if len(self.coeff) > len(other.coeff):
            ret, para, rev = self.coeff[:], other.coeff[:], False
        else:
            ret, para, rev = other.coeff[:], self.coeff[:], True
        for i in range(len(para)):
            ret[i] -= para[i]
        if rev == True:
            for i in range(len(ret)):
                ret[i] = -ret[i]
        return Polynomial(ret)

    def __call__(self, x):
        sum = 0.0
        for i in range(len(self.coeff)):
            sum += self.coeff[i] * x**i
        return sum

    def __mul__(self, other):
        ret = (len(self.coeff) + len(other.coeff) - 1) * [0]
        for i in range(len(other.coeff)):
            for j in range(len(self.coeff)):
                ret[i + j] += other.coeff[i] * self.coeff[j]
        return Polynomial(ret)

    def differentiate(self):
        for i in range(1, len(self.coeff)):
            self.coeff[i-1] = self.coeff[i]*i
        self.coeff.pop()

    def derivative(self):
        ret = (len(self.coeff)-1)*[0]
        for i in range(1, len(self.coeff)):
            ret[i-1] = self.coeff[i]*i
        return Polynomial(ret)