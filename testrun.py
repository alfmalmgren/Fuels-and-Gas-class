#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 00:13:40 2020

@author: alf
"""
#from Sfuel_class import *

#fuel = Sfuel()
#fuel.populate_proxult('ar',C=45,H=5,N=5,S=0,Cl=0,O=5,Ash=10,moist=30)
#fuel.populate()
#fuel.print_fuel()

from Ggas_class import Gas

air  = Gas()
fuel = Gas()
mix  = Gas()
air.populate(Name='Air',N2=79.0,O2=21.0,CO=0.0,CO2=0.0,H2=0.0,SO2=0.0,SO3=0.0,\
                 HCl=0.0,CH4=0.0,C2H4=0.0,C2H6=0.0,NO=0.0,N2O=0.0,NO2=0.0,\
                 H2O=0.0,T=300.0,NCV=0.0,P0=1.01325,massflow=10.0)
air.update()
air.print()

fuel.populate(Name='Fuel',N2=0.0,O2=0.0,CO=10.0,CO2=50.0,H2=20.0,SO2=0.0,SO3=0.0,\
                 HCl=0.0,CH4=10.0,C2H4=0.0,C2H6=0.0,NO=0.0,N2O=0.0,NO2=0.0,\
                 H2O=10.0,T=300.0,NCV=0.0,P0=1.01325,massflow=1.0)
air.update()
fuel.print()

fuel.mix(air, 'Fuel/Air blend')
fuel.update()
fuel.print()

fuel.burn('Flue gas')
fuel.print()