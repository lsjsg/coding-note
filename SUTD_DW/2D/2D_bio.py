#!/usr/bin/env python
# coding: utf-8
import random
import math


class PrimerDesign(object):
    def __init__(self, name):
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

# tests


class PrimerDesign(PrimerDesign):
    # 1
    def primerlength(self, sq):
        sq_len = len(sq)
        if(sq_len > self.max_length):
            return (sq_len - self.max_length)*self.penalty_length
        elif(sq_len > self.min_length):
            return 0
        else:
            return (self.min_length - sq_len)*self.penalty_length
    # 2

    def annealtemperature(self, tsq):
        if tsq > self.max_temp:
            return (tsq - self.max_temp) * self.penalty_temp
        elif sq > self.min_temp:
            return 0
        else:
            return (self.min_temp - tsq) * self.penalty_temp
    # 3

    def temperaturedifference(self, fp, rp):
        delta_t = abs(fp - rp)
        if delta_t > self.max_tdiff:
            return self.penalty_tdiff * (delta_t - self.max_tdiff)
        else:
            return 0
    # 4

    def numruns(self, sq):
        last, l, count = sq[0], [], 0
        for i in sq[1:]:
            if i == last:
                count += 1
            else:
                l.append(count)
                count, last = 0, i
        count = max(l)
        if count <= self.run_threshold:
            return 0
        else:
            return (count - self.run_threshold) * self.penalty_repeats
    # 5

    def cgcontent(self, sq):
        cg = (list(sq).count("c") + list(sq).count("g")) / (len(list(sq)))
        if cg > 0.6:
            return self.penalty_cg * (cg - 0.6)
        elif cg >= 0.4:
            return 0
        else:
            return self.penalty_cg * (0.4 - cg)
    # 6

    def repeats(self, sq):
        d = {}
        for i in range(len(sq)-1):
            count = sq.count(sq[i:i+2])
            if count > 1:
                d[sq[i:i+2]] = count
        repeats = sum(d.values())
        return self.penalty_repeats*repeats
    # 7

    def specificity(self, sq, pr):
        return self.penalty_repeats*(sq.count(pr)-1)

    def cost_objective_function(self, fp, rp, sq):
        cost = self.annealtemperature(fp) + self.annealtemperature(rp) + self.numruns(
            fp) + self.numruns(rp) + self.temperaturedifference(fp, rp)
        return cost


# ### Store the DNA sequence given to you in the variable below
dna_sequence = ''' '''
# ### Instantiate your class and read in the DNA sequence

# ### If you need to adjust any parameter from their default values in the init method, do it here

# ### Show the outcome of your testing and the functions in the subsequent cells
