# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:16:55 2018

@author: AMalmgren
"""

import unittest
from Ggas_class import *

class TestGas(unittest.TestCase):
    
  #  def test_create_test_data(self):
  #      TestGas = Gas()
  #      return TestGas
    
#    def test_molar_weight(self):
#        '''
#        Testing the molar_weight method
#        Testing the first (H) and last (HCl) items in the dictionary
#        '''
#
#        gas = Gas()  # Create a gas object
#        self.assertAlmostEqual(gas.molar_weight('H'),1.00794)
#        self.assertAlmostEqual(gas.molar_weight('HCl'),36.46064)
#        del gas      # Delete the gas object
        
    def test_cp(self):
        '''
        Testing the gas_cp method
        This method uses CP_coeff_NASA and polyAveNASA to calculate its output
        '''
        gas = Gas()  # Create a gas object
        gas.populate(N2=79.0, O2=21.0, T=273.15, NCV=0.0, P0=1.01325, massflow=0.0)
        self.assertAlmostEqual(gas.gas_cp(273.15, 373.15),1013.309021075)
        del gas      # Delete the gas object
        
    def test_burn_stoich(self):
        gas = Gas()  # Create a gas object
        
        del gas      # Delete the gas object

    def test_mix(self):
        gas1 = Gas()
        gas2 = Gas()
        gas1.populate(N2=79.0,   O2=21.0, T=273.15, NCV=0.0, P0=1.01325, massflow=1.0)
        gas2.populate(CH4=100.0, O2=0.0,  T=273.15, NCV=0.0, P0=1.01325, massflow=1.0)
        gas1.mix(gas2, new_name='mixed')
        
        self.assertAlmostEqual(gas1.N2_v, 28.2306853)
        
    def test_Tad(self):
        gas = Gas()  # Create a gas object
        gas.populate(N2=79.0, O2=21.0, T=273.15, NCV=0.0, P0=1.01325, massflow=1.0)
        self.assertAlmostEqual(gas.Tad(15000.0),287.99408595775)
        del gas      # Delete the gas object