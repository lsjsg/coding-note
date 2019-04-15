from libdw import sm

class SimpleAccount(sm.SM):
    def __init__(self,balance=0):
        self.start_state = balance
        
    def get_next_state(self,state,inp):
        if inp < 0 and state < 100:
            next_state = state + inp - 5
        else:
            next_state = state + inp
        output = next_state
        return next_state
# test cases
a = SimpleAccount()
l = [100,100,-23,-23,534,-435]
print(a.transduce(l))