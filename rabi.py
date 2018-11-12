import numpy as np
import constant as con

class Rabi():
    def __init__(self):
        self.rabi = 0

    def cal_intensity(self,P): # P [W]
        return  P/(np.pi*(con.r0**2)); # Intensity inside a fiber [W/m^2]

    def cal_Efield(self,I):
        return np.sqrt(2*I/(con.c*con.n*con.epsilon0)); # electric field

    def cal_Rabi(self,P,transition):
        self.I = self.cal_intensity(P)
        self.E = self.cal_Efield(self.I)
        self.rabi = con.d[transition]*self.E/(2*np.pi*con.hbar)
        return 1.0e-9 * self.rabi # [GHz]

#print("Rabi requency: {0:.2f} MHz".format(rabi*1.0e-6))
