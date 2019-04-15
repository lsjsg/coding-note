from libdw import sm
class CM(sm.SM):
    start_state = 0
    def get_next_values(self,state, inp):
        if inp == 50 and state == 0:
            nextstate = 1
            output = (50, '--',0)
        elif inp == 100 and state == 0:
            nextstate = 0
            output = (0, "coke",0)
        elif inp == 50 and state == 1:
            nextstate = 0
            output = (0, "coke",0)
        elif inp == 100 and state == 1:
            nextstate = 0
            output = (0, "coke",50)
        else:
            nextstate = state
            if state == 1:
                balance = 50
            elif state == 0:
                balance = 0
            output = (balance,"--",inp)
        return nextstate, output
