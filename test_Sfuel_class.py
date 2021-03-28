#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 23:35:42 2020

@author: alf

Methods:
    test_molesperkg
    test_ar_to_db
    ar_to_db
    populate_proxult
    populate
    print_fuel
    

"""
import unittest
from Sfuel_class import *
from Ggas_class import *

class TestFuel(unittest.TestCase):
    
    

#==============================================================================
    def test_molesperkg(self):
        '''
        Testing the molesperkg function
        the analysis is given in a dictionary
        '''
        analysis = {'C':25.0}   #,'H':5.0,'O':10.0,'H2O':50.0,'ash':10.0}
        fuel = Sfuel()
        self.assertEqual(fuel.molesperkg(analysis),{'C':20.814773493634842}) #,'H':49.60612734,\
                        #'O':6.25023438,'H2O':27.75421753,'ash':0.0})
        del fuel

#==============================================================================
    def test_ar_to_db(self):
        '''
        Testing the ar_to_db function
        '''
        fuel = Sfuel()
        self.assertAlmostEqual(fuel.ar_to_db(10, 50),20)     # conversion
        self.assertAlmostEqual(fuel.ar_to_db(0, 50),0)       # element = 0
        self.assertAlmostEqual(fuel.ar_to_db(105, 50),-1000) # element > 100%
        self.assertAlmostEqual(fuel.ar_to_db(10, 0),10)      # moisture = 0 % 
        self.assertAlmostEqual(fuel.ar_to_db(10, 105),-2000) # mosture > 100%
        del fuel
#==============================================================================
    def test_CP_coeff_NASA(self):
        '''
        Testing the gas_cp method
        This method uses CP_coeff_NASA and polyAveNASA to calculate its output
        '''
        NASA = NASA_coeff()  # Create a gas object
        
        self.assertAlmostEqual(NASA.CP_coeff_NASA('CO2'),(2.35677352,8.98459677e-3,\
            -7.12356269e-6,2.45919022e-9,-1.43699548e-13,4.63659493,2.74131991e-3,\
            -9.95828531e-7,1.60373011e-10,-9.16103468e-15,44.0098,0))
        del NASA      # Delete the gas object
###############################################################################
    def test_polyAveNASA (self):
        
        NASA = NASA_coeff()  # Create a gas object
        self.assertAlmostEqual(NASA.polyAveNASA (273.15,293.15,2.35677352,\
            8.98459677e-3,-7.12356269e-6,2.45919022e-9,-1.43699548e-13,\
            4.63659493,2.74131991e-3,-9.95828531e-7,1.60373011e-10,\
            -9.16103468e-15),4.384371010057103)
        del NASA
###############################################################################
    def test_gas_cp (self):
        '''
        
        '''        
        NASA = NASA_coeff()  # Create a gas object
        NASA.CO2_v = 15
        NASA.H2O_v = 10
        NASA.O2_v  = 10
        NASA.N2_v  = 60
        NASA.SO2_v = 1
        NASA.CO_v  = 1
        NASA.H2_v  = 1
        NASA.CH4_v = 1
        NASA.HCl_v = 1
        self.assertAlmostEqual(NASA.gas_cp(273.15,293.15),1044.834271634705)
        del NASA
###############################################################################
    def test_flue_gas(self):
        '''
        The flue gas method calculates the flue gas composition and air 
        required for stoichiometric combustion and populates the given
        gas class object with the results.
        Requires both the Fuel class and the Gas class
        flue_gas
        comb_gas is a gas object that is populated with the oxygen concentration
        '''
        fuel     = Sfuel()      # Create a fuel object
        fuel.populate_proxult(base='ar', C=50.0, H=5.0, N=1.0, S=0, Cl=0,\
                              O=14.0, Ash=10.0 , NCV=0, GCV=0, VM=0, moist=30.0)
        fuel.populate_masstemp(massflow=10.0, temperature=298.15)
        fuel.populate()
       # fuel.update()
        flue_gas = Gas()       # Create a gas object (flue gas)
        flue_gas.populate(N2=79.0, O2=21.0, T=273.15, NCV=0.0, P0=1.01325, massflow=5.0)
        flue_gas.update()
      #  air      = Gas()       # Create a gas object (air)
      #  air.populate(N2=79.0, O2=21.0, T=273.15, NCV=0.0, P0=1.01325, massflow=5.0)
      #  air.update()
        NCV = 15000.0
        percO2 = 5.0
        # The method returns the requirem air flow
        self.assertAlmostEqual(fuel.flue_gas(percO2, flue_gas, NCV),9.846217291082)  # Check a proper fuel with known FG flow
        del fuel               # Clean up
        del flue_gas           # Clean up
      #  del air                # Clean up


#=#
#    def test_cp(self):
#        '''
#        Testing the gas_cp method
#        This method uses CP_coeff_NASA and polyAveNASA to calculate its output
#        '''
#        gas = Gas()  # Create a gas object
#        gas.populate(N2=79.0, O2=21.0, T=273.15, NCV=0.0, P0=1.01325, massflow=0.0)
#        self.assertAlmostEqual(gas.gas_cp(273.15, 373.15),1013.309021075)
#        del gas      # Delete the gas object
        
#    def test_burn_stoich(self):
#        gas = Gas()  # Create a gas object
#        
#        del gas      # Delete the gas object
