from libdw import sm
class CommentsSM(sm.SM):
    start_state = None
    def get_next_values(self, state, inp):
        if inp=="#" and state == None:
            next_state = inp
            output = inp
        elif inp == "\n" and state is not None:
            next_state = None
            output = None
        elif state is not None:
            next_state = inp
            output = inp
        else:
            next_state=None
            output = None
        return next_state,output