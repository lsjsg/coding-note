from libdw import sm
class FirstWordSM(sm.SM):
    start_state = True
    def get_next_values(self, state, inp):
        if (inp.isalpha() or inp == "#") and bool(state) == True:
            next_state = inp
            output = inp
        elif inp == " " and state != True:
            next_state = None
            output =None
        elif inp == " " and state == True:
            next_state = True
            output = None
        elif inp=="\n":
            next_state = True
            output = None
        else:
            next_state = None
            output =None
        return next_state, output