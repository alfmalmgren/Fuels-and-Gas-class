#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:55:55 2021

@author: alf
"""
import unittest
from NASA_coeff_class import *

class TestNASA_coeff(unittest.TestCase):
###############################################################################    
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