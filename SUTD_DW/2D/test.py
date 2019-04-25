class PrimerDesign(object):
    
    def __init__ (self, name):

        '''parameters for the length criterion'''
        self.max_length = 0
        self.min_length = 0
        self.penalty_length = 10
        
        '''parameters for the temperature difference criterion'''
        self.max_tdiff = 0
        self.min_tdiff = 0
        self.penalty_tdiff = 10
        
        '''parameters for the cg content criterion'''
        self.max_cg = 0
        self.min_cg = 0
        self.penalty_cg = 10
        
        '''parameters for the annealing temperature criterion'''
        self.max_temp = 0
        self.min_temp = 0
        self.penalty_temp = 10
        
        '''parameters for the run criterion'''
        self.run_threshold = 0
        self.penalty_runs = 10
        
        '''parameters for the repeat criterion'''
        self.repeat_threshold = 0
        self.penalty_repeats = 10
        
        '''parameters for the specificity criterion'''
        self.penalty_specificity = 10 
        
        '''locations where the forward primer should be chosen from'''
        self.fp_start = 0
        self.fp_end = 0
        
        '''locations where the reverse primer should be chosen from'''
        self.rp_start = 0
        self.rp_end = 0
        
        ''' parameters for the simulated annealing portion'''
        self.initial_temperature = 200
        self.stopping_temperature = 0.01
        self.drop_fraction = 0.999 