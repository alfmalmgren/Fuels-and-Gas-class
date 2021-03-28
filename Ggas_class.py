# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:33:18 2020
Copied to this folder 2020-11-26

@author: AMalmgren
"""
from Elements_class import *
from NASA_coeff_class import *

class Gas(Elements, NASA_coeff):
    '''
    This class holds the analysis data for a gas
    It also contain methods for:
    - clear            resets all variables to 0
    - update           recalculates all analysis data from vol%
    - populate         give values to variables, input is % by vol
    - mix              blends two gases, both objects of this class
    - CV_gas           calculates the CV for the gas in the object
    - burn             combust a combustible gas with an oxidiser, both objects of this class
    - burn_stoich      combust a gas with exact the stoichiometric amount of given 
                       oxidiser, both objects of this class
    - print            prints the composition etc. of the object gas
    - molar_weight(i)  calculates the molar weight of an element or molequle
    - polyAveNASA(i)   uses coefficients from "CP_coeff_NASA" to calculate a 
                       polynomial value
    - CP_coeff_NASA(i) holds coefficients for gas Cp calculations
    - gas_cp(i)        calculates the CV for the gas in the object from the 
                       polynomial value from polyAveNASA
    (i) = inherited
    '''
    def __init__(self):
        '''
        Initiate the variables for gas composition
        '''
        #
                
        # Initiate the variables
        self.Name         = ''
        # % by volume
        self.N2_v         =  0.0  # [% by volume]
        self.O2_v         =  0.0  # [% by volume]
        self.CO_v         =  0.0  # [% by volume]
        self.CO2_v        =  0.0  # [% by volume]
        self.H2_v         =  0.0  # [% by volume]
        self.HCl_v        =  0.0  # [% by volume]
        self.SO2_v        =  0.0  # [% by volume]
        self.SO3_v        =  0.0  # [% by volume]
        self.CH4_v        =  0.0  # [% by volume]
        self.C2H4_v       =  0.0  # [% by volume]
        self.C2H6_v       =  0.0  # [% by volume]
        self.H2O_v        =  0.0  # [% by volume]
        self.NO_v         =  0.0  # [% by volume]
        self.NO2_v        =  0.0  # [% by volume]
        self.N2O_v        =  0.0  # [% by volume]
        
        # % by mass
        self.N2_m         =  0.0  # [%, by mass]
        self.O2_m         =  0.0  # [%, by mass]
        self.CO_m         =  0.0  # [%, by mass]
        self.CO2_m        =  0.0  # [%, by mass]
        self.H2_m         =  0.0  # [%, by mass]
        self.HCl_m        =  0.0  # [%, by mass]
        self.SO2_m        =  0.0  # [%, by mass]
        self.SO3_m        =  0.0  # [%, by mass]
        self.CH4_m        =  0.0  # [%, by mass]
        self.C2H4_m       =  0.0  # [%, by mass]
        self.C2H6_m       =  0.0  # [%, by mass]
        self.H2O_m        =  0.0  # [%, by mass]
        self.NO_m         =  0.0  # [%, by mass]
        self.NO2_m        =  0.0  # [%, by mass]
        self.N2O_m        =  0.0  # [%, by mass]
        # mass per kg
        self.mN2          =  0.0  # [g/Nm3]
        self.mO2          =  0.0  # [g/Nm3]
        self.mCO          =  0.0  # [g/Nm3]
        self.mCO2         =  0.0  # [g/Nm3]
        self.mH2          =  0.0  # [g/Nm3]
        self.mHCl         =  0.0  # [g/Nm3]
        self.mSO2         =  0.0  # [g/Nm3]
        self.mSO3         =  0.0  # [g/Nm3]
        self.mCH4         =  0.0  # [g/Nm3]
        self.C2H4         =  0.0  # [g/Nm3]
        self.C2H6         =  0.0  # [g/Nm3]
        self.mH2O         =  0.0  # [g/Nm3]
        self.NO           =  0.0  # [g/Nm3]
        self.NO2          =  0.0  # [g/Nm3]
        self.N2O          =  0.0  # [g/Nm3]
        # moles per kg gas
        self.moles_N2     =  0.0  # [moles/Nm3]
        self.moles_O2     =  0.0  # [moles/Nm3]
        self.moles_CO     =  0.0  # [moles/Nm3]
        self.moles_CO2    =  0.0  # [moles/Nm3]
        self.moles_H2     =  0.0  # [moles/Nm3]
        self.moles_HCl    =  0.0  # [moles/Nm3]
        self.moles_SO2    =  0.0  # [moles/Nm3]
        self.moles_SO3    =  0.0  # [moles/Nm3]
        self.moles_CH4    =  0.0  # [moles/Nm3]
        self.moles_C2H4   =  0.0  # [moles/Nm3]
        self.moles_C2H6   =  0.0  # [moles/Nm3]
        self.moles_H2O    =  0.0  # [moles/Nm3]
        self.moles_NO     =  0.0  # [moles/Nm3]
        self.moles_NO2    =  0.0  # [moles/Nm3]
        self.moles_N2O    =  0.0  # [moles/Nm3]
        
        self.Massflow     = 0.0   # [kg/s]
        self.Gas_density  = 0.0   # [kg/m3]
        
        self.T0           =  0.0  # [K]
        self.NCV_given    =  0.0  # [J/kg]
        self.GCV_given    =  0.0  # [J/kg]
        self.NCV_calc     =  0.0  # [J/kg]
        self.GCV_calc     =  0.0  # [J/kg]

#==============================================================================
#   POPULATE THE OBJECT
#==============================================================================
    def populate(self, Name='',N2=0.0,O2=0.0,CO=0.0,CO2=0.0,H2=0.0,SO2=0.0,SO3=0.0,\
                 HCl=0.0,CH4=0.0,C2H4=0.0,C2H6=0.0,NO=0.0,N2O=0.0,NO2=0.0,\
                 H2O=0.0,T=273.15,NCV=0.0,P0=1.01325,massflow=0.0):
        '''
        Give gas components in volume %
        Components: N2, O2, CO, CO2, H2, HCl, SO2, CH4
        T:    Temperature, default is 273.15    [K]
        NCV:  Net CV                            [MJ/kg]
        P0:   Gas pressure, defoult = 1.01325   [bar]
        massflow: massflow ofgas, default = 0.0 [kg/s]
        '''
        self.Name = Name
        #Check composition adds up to 100
        tot_perc = N2+O2+CO+CO2+H2+HCl+SO2+SO3+CH4+C2H4+C2H6+H2O+NO+N2O+NO2
        if abs(tot_perc/100)>1.0:
            print('\n\nThe analysis adds up to {:5.1f} %\n\n'.format(tot_perc))
        self.N2_v      =  N2
        self.O2_v      =  O2
        self.CO_v      =  CO
        self.CO2_v     =  CO2
        self.H2_v      =  H2
        self.HCl_v     =  HCl
        self.SO2_v     =  SO2
        self.SO3_v     =  SO3
        self.CH4_v     =  CH4
        self.C2H4_v    =  C2H4
        self.C2H6_v    =  C2H6
        self.H2O_v     =  H2O
        self.NO_v      =  NO
        self.N2O_v     =  N2O
        self.NO2_v     =  NO2
        self.T0        = T          # [K]
        self.Massflow  = massflow   # [kg/s]
        self.NCV_given = NCV*1.0e6  # Store as J/kg
        self.update()
#==============================================================================
#   UPDATE ALL THE CALCULATED PARAMETERS
#==============================================================================
       
    def update(self):
        '''
        Calculate data from %vol, mass flow and NCV
        '''
        
        # Convert to mass percent
        # Vol% is the same as mole%
        # 1 mol = 22.413 l @ STP (0°C, 1 atm)
        # look at 1 Nm3 gas
        Tot_moles = 1000.0/22.413   # = 44.617 mol/Nm3 gas at STP
        # moles per m3
        self.moles_N2   = self.N2_v   * Tot_moles / 100.0  # [moles/Nm3]
        self.moles_O2   = self.O2_v   * Tot_moles / 100.0  # [moles/Nm3]
        self.moles_CO   = self.CO_v   * Tot_moles / 100.0  # [moles/Nm3]
        self.moles_CO2  = self.CO2_v  * Tot_moles / 100.0  # [moles/Nm3]
        self.moles_H2   = self.H2_v   * Tot_moles / 100.0  # [moles/Nm3]
        self.moles_HCl  = self.HCl_v  * Tot_moles / 100.0  # [moles/Nm3]
        self.moles_SO2  = self.SO2_v  * Tot_moles / 100.0  # [moles/Nm3]
        self.moles_SO3  = self.SO3_v  * Tot_moles / 100.0  # [moles/Nm3]
        self.moles_CH4  = self.CH4_v  * Tot_moles / 100.0  # [moles/Nm3]
        self.moles_C2H4 = self.C2H4_v * Tot_moles / 100.0  # [moles/Nm3]
        self.moles_C2H6 = self.C2H6_v * Tot_moles / 100.0  # [moles/Nm3]
        self.moles_H2O  = self.H2O_v  * Tot_moles / 100.0  # [moles/Nm3]
        self.moles_NO   = self.NO_v   * Tot_moles / 100.0  # [moles/Nm3]
        self.moles_N2O  = self.N2O_v  * Tot_moles / 100.0  # [moles/Nm3]
        self.moles_NO2  = self.NO2_v  * Tot_moles / 100.0  # [moles/Nm3]
        # g/Nm3
        self.mN2   = self.moles_N2   * self.molar_weight('N2')    # [g/Nm3]
        self.mO2   = self.moles_O2   * self.molar_weight('O2')    # [g/Nm3]
        self.mCO   = self.moles_CO   * self.molar_weight('CO')    # [g/Nm3]
        self.mCO2  = self.moles_CO2  * self.molar_weight('CO2')   # [g/Nm3]
        self.mH2   = self.moles_H2   * self.molar_weight('H2')    # [g/Nm3]
        self.mHCl  = self.moles_HCl  * self.molar_weight('HCl')   # [g/Nm3]
        self.mSO2  = self.moles_SO2  * self.molar_weight('SO2')   # [g/Nm3]
        self.mSO3  = self.moles_SO3  * self.molar_weight('SO2')   # [g/Nm3]
        self.mCH4  = self.moles_CH4  * self.molar_weight('CH4')   # [g/Nm3]
        self.mC2H4 = self.moles_C2H4 * self.molar_weight('C2H4')  # [g/Nm3]
        self.mC2H6 = self.moles_C2H6 * self.molar_weight('C2H6')  # [g/Nm3]
        self.mH2O  = self.moles_H2O  * self.molar_weight('H2O')   # [g/Nm3]
        self.mNO   = self.moles_NO   * self.molar_weight('NO')    # [g/Nm3]
        self.mN2O  = self.moles_N2O  * self.molar_weight('N2O')   # [g/Nm3]
        self.mNO2  = self.moles_NO2  * self.molar_weight('NO2')   # [g/Nm3]
        mtot = self.mN2 + self.mO2 + self.mCO + self.mCO2 + self.mH2 + self.mHCl + self.mSO2 + self.mCH4 + self.mH2O # [g/Nm3]
        # Gas density
        self.Gas_density = mtot/1000.0        # [kg/Nm3]
        # % by mass
        self.N2_m   =  self.mN2/mtot   * 100.0  # [%, by mass]
        self.O2_m   =  self.mO2/mtot   * 100.0  # [%, by mass]
        self.CO_m   =  self.mCO/mtot   * 100.0  # [%, by mass]
        self.CO2_m  =  self.mCO2/mtot  * 100.0  # [%, by mass]
        self.H2_m   =  self.mH2/mtot   * 100.0  # [%, by mass]
        self.HCl_m  =  self.mHCl/mtot  * 100.0  # [%, by mass]
        self.SO2_m  =  self.mSO2/mtot  * 100.0  # [%, by mass]
        self.SO3_m  =  self.mSO3/mtot  * 100.0  # [%, by mass]
        self.CH4_m  =  self.mCH4/mtot  * 100.0  # [%, by mass]
        self.C2H4_m =  self.mC2H4/mtot * 100.0  # [%, by mass]
        self.C2H6_m =  self.mC2H6/mtot * 100.0  # [%, by mass]
        self.H2O_m  =  self.mH2O/mtot  * 100.0  # [%, by mass]
        self.NO_m   =  self.mNO/mtot   * 100.0  # [%, by mass]
        self.N2O_m  =  self.mN2O/mtot  * 100.0  # [%, by mass]
        self.NO2_m  =  self.mNO2/mtot  * 100.0  # [%, by mass]
     
        #Calculate a GCV from the analysis
        self.GCV_calc = (self.CV_gas('H2') * self.H2_m + self.CV_gas('CH4') * self.CH4_m +\
            self.CV_gas('C2H4') * self.C2H4_m + self.CV_gas('C2H6') * self.C2H6_m +\
            self.CV_gas('CO') * self.CO_m)/100.0  # [J/kg]
        # Convert to NCV using Dulong's formula
        self.NCV_calc = (self.GCV_calc/1000.0 - 24.44*(9*self.H2_m*2) + self.H2O_m)*1000.0 # [J/kg]
        
#==============================================================================
#   MIX TWO GASES TOGETHER
#==============================================================================
    def mix(self, new_gas, new_name=''):
        '''
        new_gas has tp be an object of the same class
        add the content of new_gas to self and update temperature, CV etc.        
        '''
        self.Name    = new_name
        # Mass and volumetric flow
        massflow_tot = self.Massflow + new_gas.Massflow          # [kg/s]
        new_volflow  = new_gas.Massflow / new_gas.Gas_density    # [Nm3/s]
        old_volflow  = self.Massflow    / self.Gas_density       # [Nm3/s]
        volflow_tot  = new_volflow + old_volflow                 # [Nm3/s]
               
        # New vol %
        N2_v   = (self.N2_v   * old_volflow + new_gas.N2_v   * new_volflow)/volflow_tot   # [% by mass]
        O2_v   = (self.O2_v   * old_volflow + new_gas.O2_v   * new_volflow)/volflow_tot   # [% by mass]
        CO_v   = (self.CO_v   * old_volflow + new_gas.CO_v   * new_volflow)/volflow_tot   # [% by mass]
        CO2_v  = (self.CO2_v  * old_volflow + new_gas.CO2_v  * new_volflow)/volflow_tot   # [% by mass]
        H2_v   = (self.H2_v   * old_volflow + new_gas.H2_v   * new_volflow)/volflow_tot   # [% by mass]
        HCl_v  = (self.HCl_v  * old_volflow + new_gas.HCl_v  * new_volflow)/volflow_tot   # [% by mass]
        SO2_v  = (self.SO2_v  * old_volflow + new_gas.SO2_v  * new_volflow)/volflow_tot   # [% by mass]
        SO3_v  = (self.SO3_v  * old_volflow + new_gas.SO3_v  * new_volflow)/volflow_tot   # [% by mass]
        CH4_v  = (self.CH4_v  * old_volflow + new_gas.CH4_v  * new_volflow)/volflow_tot   # [% by mass]
        C2H4_v = (self.C2H4_v * old_volflow + new_gas.C2H4_v * new_volflow)/volflow_tot   # [% by mass]
        C2H6_v = (self.C2H6_v * old_volflow + new_gas.C2H6_v * new_volflow)/volflow_tot   # [% by mass]
        H2O_v  = (self.H2O_v  * old_volflow + new_gas.H2O_v  * new_volflow)/volflow_tot   # [% by mass]
        NO_v   = (self.NO_v   * old_volflow + new_gas.NO_v   * new_volflow)/volflow_tot   # [% by mass]
        N2O_v  = (self.N2O_v  * old_volflow + new_gas.N2O_v  * new_volflow)/volflow_tot   # [% by mass]
        NO2_v  = (self.NO2_v  * old_volflow + new_gas.NO2_v  * new_volflow)/volflow_tot   # [% by mass]
        
        # Work out new temperature
        Q1 = self.Massflow    * (self.T0 - 273.15)    * self.gas_cp(273.15,    (self.T0))    # [W]
        Q2 = new_gas.Massflow * (new_gas.T0 - 273.15) * new_gas.gas_cp(273.15, (new_gas.T0)) # [W]
        T = ((self.T0) * self.Massflow + (new_gas.T0) * new_gas.Massflow)/(massflow_tot) # First rough estimate mass weighed average
        T2 = 273.15 +  (Q1 + Q2)/((self.gas_cp(273.15, T)*self.Massflow + new_gas.gas_cp(273.15, T)*new_gas.Massflow)/(self.Massflow+new_gas.Massflow))/massflow_tot
        T2 = 273.15 + (Q1 + Q2)/((self.gas_cp(273.15, T2)*self.Massflow + new_gas.gas_cp(273.15, T2)*new_gas.Massflow)/(self.Massflow+new_gas.Massflow))/massflow_tot
        
        NCV = (self.NCV_given * self.Massflow + new_gas.NCV_given * new_gas.Massflow)/massflow_tot  # [J/kg]
        
       # self.clear()                       # Clear all old data
        # Update: N2, O2, CO, CO2, H2O, H2, CH4, O2, HCl, temperature, massflow, NCV
        self.populate(Name=self.Name,N2=N2_v,O2=O2_v,CO=CO_v,CO2=CO2_v,H2O=H2O_v,H2=H2_v,CH4=CH4_v,SO2=SO2_v,\
                      SO3=SO3_v,HCl=HCl_v,C2H4=C2H4_v,C2H6=C2H6_v,NO=NO_v,N2O=N2O_v,NO2=NO2_v,\
                      T=T2,NCV=NCV*1.0e-6,massflow=massflow_tot)
        self.update()

#==============================================================================        
#   CALORIFIC VALUE FOR A GAS
#==============================================================================  
    def CV_gas(self,gas):
        '''
        Calculates the calorific value for a gas in J/kg
        gas = string of gas ('H2', 'CH4', 'CO') are recognised
        returns calorific value [J/kg]
        '''
        if gas == 'H2':      # Hydrogen
            return 119.8e6   # [J/kg]
        elif gas == 'CH4':   # Methane
            return 50.0e6    # [J/kg]
        elif gas == 'CO':    # Carbon monoxide
            return 10.1e6    # [J/kg]
        elif gas == 'C2H4':  # Ethylene
            return 47.2e6    # [J/kg]
        elif gas == 'C2H6':  # Ethane
            return 47.5e6    # [J/kg]
        else:
            print('{} is not a rcognised gas, try H2, CO or CH4.'.format(gas))
            return 'Not recognised gas'

#==============================================================================        
#   USE ALL OXYGEN AVAILABLE FOR OXIDATION
#==============================================================================       
    def burn(self, name=''):
        '''
        Burn combustible gas components as far as possible with available oxygen
        
        It is assumed that the temperature is high enough for combustion
        to take place.
        '''
        self.Name = name
        # mol/Nm3 gas
        Tot_moles = 1000.0/22.413   # mol/Nm3 gas at STP
        Q1, Q2 = 0.0, 0.0
        # mol% vol
        N2_g     = self.moles_N2  / self.Gas_density    # [moles per kg gas]
        O2_g     = self.moles_O2  / self.Gas_density    # [moles per kg gas]
        CO_g     = self.moles_CO  / self.Gas_density    # [moles per kg gas]
        CO2_g    = self.moles_CO2 / self.Gas_density    # [moles per kg gas]
        H2_g     = self.moles_H2  / self.Gas_density    # [moles per kg gas]
        HCl_g    = self.moles_HCl / self.Gas_density    # [moles per kg gas]
        SO2_g    = self.moles_SO2 / self.Gas_density    # [moles per kg gas]
        CH4_g    = self.moles_CH4 / self.Gas_density    # [moles per kg gas]
        H2O_g    = self.moles_H2O / self.Gas_density    # [moles per kg gas]
        
        # ASSUMPTION: The temperature is high enough for combustion to take place
        # Check if combustible gases present
        if (CO_g + H2_g + CH4_g)>0.0:    # Yes
            # Required O2 for stoichiometric combustion
            O2_req = CO_g/2 + H2_g/2 + CH4_g * 2  # Required oxygen for complete combustion
            if O2_g>=O2_req:                      # Yes, so over stoichiometric combustion
                # CO + 1/2 O2 => CO2
                CO2_g += CO_g
                O2_g -= CO_g/2
                heat_rel = CO_g * self.molar_weight("CO") / 1000 * self.CV_gas('CO')  # [J/Nm3]
                CO_g = 0.0
                # H2 + 1/2 O2 => H2O
                H2O_g += H2_g
                O2_g -= H2_g/2
                heat_rel += H2_g * self.molar_weight("H2") / 1000 * self.CV_gas('H2')  # [J/Nm3]
                H2_g = 0.0
                # CH4 + 2 O2 => CO2 + 2 H2O
                CO2_g += CH4_g
                H2O_g += CH4_g * 2.0
                O2_g -= CH4_g * 2.0
                heat_rel += CH4_g * self.molar_weight("CH4") / 1000 * self.CV_gas('CH4')  # [J/Nm3]
                CH4_g = 0.0
            else:        # No, so under stoichiometric combustion, burn equal
                         # fractions of all components to use available oxygen
                frac = O2_g/O2_req      # fraction to burn
                # CO + 1/2 O2 => CO2
                CO2_g += CO_g * frac
                O2_g -= CO_g * frac /2
                heat_rel = CO_g * frac * self.molar_weight("CO") / 1000 * self.CV_gas('CO')   # [J/Nm3]
                CO_g -= CO_g * frac
                # H2 + 1/2 O2 => H2O
                H2O_g += H2_g * frac
                O2_g -= H2_g * frac / 2
                heat_rel += H2_g * frac * self.molar_weight("H2") / 1000 * self.CV_gas('H2')  # [J/Nm3]
                H2_g -= H2_g * frac
                # CH4 + 2 O2 => CO2 + 2 H2O
                CO2_g += CH4_g * frac
                H2O_g += CH4_g * 2.0 * frac
                O2_g -= CH4_g * 2.0 * frac
                heat_rel += CH4_g * frac * self.molar_weight("CH4") / 1000 * self.CV_gas('CH4')  # [J/Nm3]
                CH4_g -= CH4_g * frac
        
        # Convert to % by volume
            Tot_moles = N2_g + O2_g + CO_g + CO2_g + H2_g + HCl_g + SO2_g + CH4_g + H2O_g  # moles / kg gas 
        # update the object
            self.N2_v  = N2_g /Tot_moles*100      # [% vol]
            self.O2_v  = O2_g /Tot_moles*100      # [% vol]
            self.CO_v  = CO_g /Tot_moles*100      # [% vol]
            self.CO2_v = CO2_g/Tot_moles*100      # [% vol]
            self.H2_v  = H2_g /Tot_moles*100      # [% vol]
            self.HCl_v = HCl_g/Tot_moles*100      # [% vol]
            self.SO2_v = SO2_g/Tot_moles*100      # [% vol]
            self.CH4_v = CH4_g/Tot_moles*100      # [% vol]
            self.H2O_v = H2O_g/Tot_moles*100      # [% vol]
        # update other parameters inthe object
            self.update()
        
        # Gas temperature
            Q1 = self.Massflow * (self.T0 - 273.15) * self.gas_cp(273.15, self.T0) # [W]
            Q2 = heat_rel * self.Massflow              # [W]
            T2 = 273.15 + (Q1 + Q2)/self.gas_cp(273.15, self.T0)/self.Massflow
            T1 = T2 + 10
            count = 0
            while (abs(T1-T2)>1.0 and count<25): # Iterate for temperature
                T1 = T2
                T2 = 273.15 + (Q1 + Q2)/self.gas_cp(273.15, T2)/self.Massflow
                count += 1
            self.T0 = T2
        
        return Q2
#==============================================================================
#   BURN A STOICHIOMETRIC BLEND OF SELF AND AN OXIDISER LIKE AIR 
#==============================================================================
    def burn_stoich(self, Ox):
        '''
        Calculates the adiabatic flame temperature for a mix of two gases where
        the blend proportions are adjusted to give stoichiometric combustion
        
        Initially, assume no combustible gas in oxidiser.
        
        self = fuel gas
        Ox   = oxidiser gas
        '''
        print('\nBURN STOICH\n')
        
        # Work out how much oxygen is required to burn all combustible gas
        # moles O2 needed
        kg_O2_stoich = 0.0
        Q = 0.0
        mcomb = 0.5 * self.moles_CO + 2.0 * self.moles_CH4 + 0.5 * self.moles_H2 - self.moles_O2  # [moles/Nm3]
        # moles O2 per second required
        if mcomb>0:  # Check that O2 required is positive.
            mcomb /= self.Gas_density                # [moles O2/kg gas]
            mcomb *= self.molar_weight('O2') / 1000  # [kg O2/kg gas]
            mcomb = mcomb * self.Massflow            # [kg O2/s]
            kg_O2_stoich = mcomb                     # stoichiometric [kg O2/s]
            ox_massflow = mcomb / Ox.O2_m * 100      # [kg oxidiser/s]
        #   1 mole = 22.413 * 10^-3 Nm3
            Ox.Massflow = ox_massflow                # set oxidiser flow
        #   Blend oxidiser and fuel gas in stoichiometric proportions
            self.mix(Ox)
            self.burn()      # Burn the resulting gas and return
            Q = self.burn()  # Burn the resulting gas and return [W]
        return  (Q, kg_O2_stoich)
#==============================================================================
    def Tad (self,NCV, air_ratio):
        '''
        Input:
            T0        = Initial temperature(Kelvin)            [self.T0]
            NCV       = Net Calorific Value(MJ/kg fuel)
            air_ratio = ratio kg air/kg fuel

        Output:
            TAdNew = Calculated Adiabatic flame temperature (Kelvin)
                     if =-1, then not converted
        External functions:
            gas_cp
        Author:
        Date: 2015-02-13    
        '''
        T0 = self.T0
        n=0
        TAdNew=1510.0
        TAdOld=1500.0
        
        while abs(TAdNew-TAdOld)>1.0 and n<100:
            TAdOld=TAdNew
            cp = self.gas_cp(T0,TAdOld)
            print('T0: {:6.2f}, TAdNew: {:6.2f}, cp: {:7.2f}, massflow: {:6.2f}'.format(T0, TAdNew, cp, self.Massflow))
            # air_ratio+1 is kg FG/kg fuel
            TAdNew = T0 + NCV/cp/(air_ratio+1)
            n+=1
            #print n, TAdNew, NCV, MassFlowFlueGas
            if n==100:
                TAdNew=-1
        return TAdNew    #Temperature in Kelvin
#==============================================================================
#   PRINT GAS COMPOSITION ETC.
#==============================================================================      
    def print(self):
        '''
        Prints composition of the gas in the object. Also CV, density, temperature,
        mass flow and Cp
        '''
        print('\nComposition of {:}:'.format(self.Name))
        print('===========================')
        print('N2:             {:5.1f} % by vol {:5.1f} % by mass'.format(self.N2_v, self.N2_m))
        print('O2:             {:5.1f} % by vol {:5.1f} % by mass'.format(self.O2_v, self.O2_m))
        print('CO:             {:5.1f} % by vol {:5.1f} % by mass'.format(self.CO_v, self.CO_m))
        print('CO2:            {:5.1f} % by vol {:5.1f} % by mass'.format(self.CO2_v, self.CO2_m))
        print('H2:             {:5.1f} % by vol {:5.1f} % by mass'.format(self.H2_v, self.H2_m))
        print('HCl:            {:5.1f} % by vol {:5.1f} % by mass'.format(self.HCl_v, self.HCl_m))
        print('SO2:            {:5.1f} % by vol {:5.1f} % by mass'.format(self.SO2_v, self.SO2_m))
        print('CH4:            {:5.1f} % by vol {:5.1f} % by mass'.format(self.CH4_v, self.CH4_m))
        print('H2O:            {:5.1f} % by vol {:5.1f} % by mass'.format(self.H2O_v, self.H2O_m))
        print('Density:       {:8.3f} kg/m3'.format(self.Gas_density))
        print('Temperature:   {:6.1f} K or {:6.1f} °C'.format(self.T0, self.T0-273.15))
        print('Cp:             {:7.1f} J/kg/K between 0 and {:5.1f} °C'.format(self.gas_cp(273.15, self.T0), self.T0-273.15))
        print('Massflow:       {:6.1f} kg/s'.format(self.Massflow))
        print('Given NCV:      {:5.1f} MJ/kg'.format(self.NCV_given*1.0e-6))
        print('Calculated GCV: {:5.1f} MJ/kg'.format(self.GCV_calc*1.0e-6))
        print('Calculated NCV: {:5.1f} MJ/kg'.format(self.NCV_calc*1.0e-6))
        print('===========================')
