from rabi import Rabi
import constant as con

class Population():
    # hyperfine shift [GHz]
    Omega = 0

    def __init__(self):
        self.s = 0

    def rhoee(self, detune, Omega, freqoff):
        return Omega**2/(detune-freqoff)**2+2*Omega**2

    def rhosum(self, detune, power):
        for f in ['eF3','eF4','eF5']: # transition to eF2 is forbiden
            Omega = Rabi().cal_Rabi(power, 'gF4'+f)
            self.s = self.s + self.rhoee(detune, Omega, con.hyperfine[f])
        return self.s


