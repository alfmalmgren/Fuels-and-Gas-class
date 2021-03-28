#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 00:18:53 2021

@author: alf
"""
import unittest
from Elements_class import *


class TestElements(unittest.TestCase):

###############################################################################
    def test_molar_weight(self):
        '''
        Testing the molar_weight method
        Testing the first (H) and last (HCl) items in the dictionary
        '''
        element = Elements()  # Create an elements object
        self.assertAlmostEqual(element.molar_weight('H'),1.00794)
        self.assertAlmostEqual(element.molar_weight('SO3'),80.0632)
        del element
        return
###############################################################################   
    def test_molesperkg(self):
        '''
        Testing the molesperkg function
        the analysis is given in a dictionary
        '''
        analysis = {'C':25.0}   #,'H':5.0,'O':10.0,'H2O':50.0,'ash':10.0}
        element = Elements()  # Create an elements object
        self.assertEqual(element.molesperkg(analysis),{'C':20.814773493634842}) #,'H':49.60612734,\
                        #'O':6.25023438,'H2O':27.75421753,'ash':0.0})
        del element
###############################################################################