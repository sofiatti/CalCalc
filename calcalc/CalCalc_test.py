import unittest

from CalCalc import calculate

class CalCalcTests(unittest.TestCase):

    def test_1(self):
        a = '5.965305×10^31 kg  (kilograms)'
        assert a == calculate('weight of the sun * 30')

    def test_2(self):
        assert abs(16 - float(calculate('4**2'))) < 0.001
    
    def test_3(self):
        a = '510.9989 keV/c^2' 
        assert a == calculate('mass of electron')

    def test_4(self):
        assert abs(6 - float(calculate('1+2+3'))) < 0.001
    

    def test_5(self):
        assert abs(5.44 - float(calculate('3.2*1.7'))) < .001   

if __name__=='__main__':
    unittest.main()
