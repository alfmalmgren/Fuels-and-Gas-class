#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:54:31 2021

@author: alf
"""
class NASA_coeff():
    '''
    Coefficients for the following gases are available:
        CO2, CO, H2O, O2, N2, SO2, H2, CH4, HCl.
    
    Coefficients to add: C2H4, C2H6
    '''
    def __init_(self):
        self.coeff = []   # A list for the coefficients
        
  #  def coefficients(self, compound):
        
###############################################################################
    def CP_coeff_NASA(self,gas):
        '''
        Input: (self,gas)
        This routine defines the polynomial coefficients for Cp of a number
        of gases at atmospheric pressure and at the temperature T in degrees C.
        The return value is Cp/R and is dimensionless. Multiplywith R=8.31451
        gives Cp in J/kg/K.
        
        The Cp/R at the temperature T is calculated as:
        
        Cp/R = A+T(B+T(C+T(D+T*E)))
        
        The average Cp between T1 and T2 can be calculated as:
        
                     B           C  (T2^3-T1^3)    D  (T2^4-T1^4)    E  (T2^5-T1^5)
     Cp(ave)/R = A + - (T2-T1) + - (-----------) + - (-----------) + - (-----------)
                     2           3    (T2-T1)      4    (T2-T1)      5    (T2-T1)
        
        Input:
            gas    -    A string defining which gas that is requested. Allowed strings 
                        are: 'CO2', 'H2O', 'O2', 'N2' or 'SO2'
        
        Output:
            AL,BL,CL,DL,EL=The polynomial coefficients for the chosen gas for >1000K
            AH,BH,CH,DH,EH=The polynomial coefficients for the chosen gas for <1000K
            MW      -   The moleqular weight for the gas
            flag    -   flag=0 success
                        flag=1 could not find coefficients for this gas
        
        Example: AL,BL,CL,DL,EL,AH,BH,CH,DH,EH,MW,flag = CP_coeff_NASA('CO2')
                        
        By Alf Malmgren on 2015/02/17.
        Update and N2 corrected 2020-11-20 by alf Malmgren
        '''
        flag=0
        #CO2     checked 2020-11-20
        if gas=='CO2':
            #Valid 200-6000K
            #Coeff A-E for <=1000K
            AL=2.35677352           #<=1000K
            BL=8.98459677e-3        #<=1000K
            CL=-7.12356269e-6       #<=1000K
            DL=2.45919022e-9        #<=1000K
            EL=-1.43699548e-13      #<=1000K
            
            AH=4.63659493           #>1000K
            BH=2.74131991e-3        #>1000K
            CH=-9.95828531e-7       #>1000K
            DH=1.60373011e-10       #>1000K
            EH=-9.16103468e-15      #>1000K
            
            MW=44.0098              #Molecular weight
        
            #CO     checked 2020-11-20
        elif gas=='CO':
            #Valid 200-6000K
            #Coeff A-E for <=1000K
            AL=3.57953347           #<=1000K
            BL=-6.1035368e-4        #<=1000K
            CL=1.01681433e-6        #<=1000K
            DL=9.07005884e-10       #<=1000K
            EL=-9.04424499e-13      #<=1000K
            
            AH=3.04848583           #>1000K
            BH=1.35172818e-3        #>1000K
            CH=-4.85794075e-7       #>1000K
            DH=7.88536486e-11       #>1000K
            EH=-4.69807489e-15      #>1000K
            
            MW=28.0104              #Molecular weight
            
        #H2O     checked 2020-11-20
        elif gas=='H2O':
    #        #Valid 200-6000K
    #        #Coeff A-E for <=1000K
            AL=4.19864056       #<=1000K
            BL=-2.0364341e-3    #<=1000K
            CL=6.52040211e-6    #<=1000K
            DL=-5.48797062e-9   #<=1000K
            EL=1.77197817e-12   #<=1000K
            
            AH=2.67703787       #>1000K
            BH=2.97318329e-3    #>1000K
            CH=-7.7376969e-7    #>1000K
            DH=9.44336689e-11   #>1000K
            EH=-4.26900959e-15  #>1000K
            
            MW=18.01528         #Molecular weight
            
        #O2     checked 2020-11-20
        elif gas=='O2':
            AL=3.78245636       #<=1000K
            BL=-2.99673415e-3   #<=1000K
            CL=9.847302e-6      #<=1000K
            DL=-9.68129508e-9   #<=1000K
            EL=3.24372836e-12   #<=1000K
            
            AH=3.66096083       #>1000K
            BH=6.56365523e-4    #>1000K
            CH=-1.41149485e-7   #>1000K
            DH=2.05797658e-11   #>1000K
            EH=-1.29913248e-15  #>1000K
            
            MW=31.9988          #Molecular weight
        
        #N2     checked 2020-11-20
        elif gas=='N2':
            AL=3.53100528       #<=1000K
            BL=-1.23660987e-4   #<=1000K
            CL=-5.02999437e-7   #<=1000K
            DL=2.43530612e-9    #<=1000K
            EL=-1.40881235e-12  #<=1000K
            
            AH=2.95257626       #>1000K
            BH=1.39690057e-3    #>1000K
            CH=-4.92631691e-7   #>1000K
            DH=7.86010367e-11   #>1000K
            EH=-4.60755321e-15  #>1000K
            
            MW=28.01293         #Molecular weight
        
        #SO2     checked 2020-11-20
        elif gas=='SO2':
            AL=3.2665338        #<=1000K
            BL=5.3237902e-3     #<=1000K
            CL=6.8437552e-7     #<=1000K
            DL=-5.2810047e-9    #<=1000K
            EL=2.5590454e-12    #<=1000K
            
            AH=5.2451364        #>1000K
            BH=1.9704204e-3     #>1000K
            CH=-8.0375769e-7    #>1000K
            DH=1.5149969e-10    #>1000K
            EH=-1.0558004e-14   #>1000K
            
            MW=64.0648          #Molecular weight
    
        #H2     checked 2020-11-20
        elif gas=='H2':
            AL=2.34433112        #<=1000K
            BL=7.98052075e-3     #<=1000K
            CL=-1.94781510e-5    #<=1000K
            DL=2.01572094e-8     #<=1000K
            EL=-7.37611761e-12   #<=1000K
            
            AH=2.93286579        #>1000K
            BH=8.26607967e-4     #>1000K
            CH=-1.46402335e-7    #>1000K
            DH=1.54100359e-11    #>1000K
            EH=-6.88804432e-16   #>1000K
            
            MW=2.01588           #Molecular weight
    
        #CH4     checked 2020-11-20
        elif gas=='CH4':
            AL=5.14987613        #<=1000K
            BL=-1.36709788e-2    #<=1000K
            CL=4.91800599e-5     #<=1000K
            DL=-4.84743026e-08   #<=1000K
            EL=1.66693956e-11    #<=1000K
            
            AH=1.63552643        #>1000K
            BH=1.00842795e-02    #>1000K
            CH=-3.36916254e-06   #>1000K
            DH=5.34958667e-10    #>1000K
            EH=-3.15518833e-14   #>1000K
            
            MW=16.04276          #Molecular weight
        #HCl     checked 2020-11-25
        elif gas=='HCl':
            AL=3.5248171         #<=1000K
            BL=2.9984862e-5      #<=1000K
            CL=-8.6221891e-7     #<=1000K
            DL=2.0979721e-09     #<=1000K
            EL=-9.8658191e-13    #<=1000K
            
            AH=2.7665884         #>1000K
            BH=1.4381883e-3      #>1000K
            CH=-4.6993e-07       #>1000K
            DH=7.3499408e-11     #>1000K
            EH=-4.3731106e-15    #>1000K
            
            MW=36.46064          #Molecular weight   
        else:
            flag=1
        
        return (AL,BL,CL,DL,EL,AH,BH,CH,DH,EH,MW,flag)
###############################################################################
    def polyAveNASA (self,T0,T1,AL,BL,CL,DL,EL,AH,BH,CH,DH,EH):
        '''
        Input: (self,T0,T1,AL,BL,CL,DL,EL,AH,BH,CH,DH,EH)
        This function calculates the average value of the dependent variable, V,
        between two gas temperatures, calculated using the integrated form of the
        polynomial based on coefficients from NASA. There are two sets of 
        coefficients for temperatures over and under 1000 K.
        
        Input: T0, T1  =independent variable (for example the lowest and highest
        temperatures in the interval studied (in degrees C))
        
        AL,BL,CL,DL,EL and AH,BH,CH,DH,EH are the polynomial coefficients for 
        low temperatures (<1000 K) and high (>1000K) of the form 
               
                                      3    3           4    4           5    5
               B               C   (T1 - T0 )   D   (T1 - T0 )   E   (T1 - T0 )
           A + - * (T1 + T0) + - * ---------- + - * ---------- + - * ----------
               2               3    (T1 - T0)   4    (T1 - T0)   5    (T1 - T0)
                 
        Last edited by Alf Malmgren on 2015/01/16
        '''
       # T0 = T0-273.15
       # T1 = T1-273.15
        #Same start and end temperature below 1000 K
        if T0==T1 and T0<1000.0:
            V=AL+BL*T0+CL*T0**2+DL*T0**3+EL*T0**4
        #Same start and end temperature above 100 K
        elif T0==T1 and T0>=1000.0:
            V=AH+BH*T0+CH*T0**2+DH*T0**3+EH*T0**4
        #Both below 1000 K
        elif T0<1000.0 and T1<=1000.0:
            V=AL+BL/2.0*(T1+T0)+CL/3.0*((T1**3-T0**3)/(T1-T0))+DL/4.0*\
              ((T1**4-T0**4)/(T1-T0))+EL/5.0*((T1**5-T0**5)/(T1-T0))
        #One below and one above 1000 K
        elif T0<1000.0 and T1>1000.0:
            V1=(AL+BL/2.0*(1000.0+T0)+CL/3.0*((1000.0**3-T0**3)/(1000.0-T0))+DL/4.0*((1000.0**4-T0**4)/(1000.0-T0))+EL/5.0*((1000.0**5-T0**5)/(1000.0-T0)))*(1000.0-T0)
            V2=(AH+BH/2.0*(T1+1000.0)+CH/3.0*((T1**3-1000.0**3)/(T1-1000.0))+DH/4.0*((T1**4-1000.0**4)/(T1-1000.0))+EH/5.0*((T1**5-1000.0**5)/(T1-1000.0)))*(T1-1000.0)
            V=(V1+V2)/(T1-T0)
        #Both above 1000 K
        else:  #T0>=1000.0 and T1>=1000.0
            V=AH+BH/2.0*(T1+T0)+CH/3.0*((T1**3-T0**3)/(T1-T0))+DH/4.0*((T1**4-T0**4)/\
              (T1-T0))+EH/5.0*((T1**5-T0**5)/(T1-T0))
    #    print('V=',V)
        return V
###############################################################################
    def gas_cp (self, T0, T1):
        '''
        Input: (self, T0, T1)
        
        Calculates the lower and higher temperature CP coefficients from NASA
        calling CP_coeff_NASA
        
        By Angus Malmgren
        On 2015/02/18
        '''
        CO2 = self.CO2_v
        H2O = self.H2O_v
        O2  = self.O2_v
        N2  = self.N2_v
        SO2 = self.SO2_v
        CO  = self.CO_v
        H2  = self.H2_v
        CH4 = self.CH4_v
        HCl = self.HCl_v
        
        
        if abs(CO2+H2O+O2+N2+SO2+CO+H2+CH4+HCl-100)>0.1:
            print('Sum of element percentages not 100% +/- 0.1%')
            N2vt = 100.0-(CO2+H2O+O2+SO2+CO+H2+CH4+HCl)
            N2t = N2vt - N2
            print('N2 has been changed by ', N2t, 'from', N2)
            N2 = N2vt
            print('N2 is now ', N2)
        ALCO2,BLCO2,CLCO2,DLCO2,ELCO2,AHCO2,BHCO2,CHCO2,DHCO2,EHCO2,MWCO2,flag = self.CP_coeff_NASA('CO2')
        ALCO,BLCO,CLCO,DLCO,ELCO,AHCO,BHCO,CHCO,DHCO,EHCO,MWCO,flag            = self.CP_coeff_NASA('CO')
        ALO2,BLO2,CLO2,DLO2,ELO2,AHO2,BHO2,CHO2,DHO2,EHO2,MWO2,flag            = self.CP_coeff_NASA('O2')
        ALH2O,BLH2O,CLH2O,DLH2O,ELH2O,AHH2O,BHH2O,CHH2O,DHH2O,EHH2O,MWH2O,flag = self.CP_coeff_NASA('H2O')
        ALN2,BLN2,CLN2,DLN2,ELN2,AHN2,BHN2,CHN2,DHN2,EHN2,MWN2,flag            = self.CP_coeff_NASA('N2')
        ALSO2,BLSO2,CLSO2,DLSO2,ELSO2,AHSO2,BHSO2,CHSO2,DHSO2,EHSO2,MWSO2,flag = self.CP_coeff_NASA('SO2')
        ALH2,BLH2,CLH2,DLH2,ELH2,AHH2,BHH2,CHH2,DHH2,EHH2,MWH2,flag            = self.CP_coeff_NASA('H2')
        ALCH4,BLCH4,CLCH4,DLCH4,ELCH4,AHCH4,BHCH4,CHCH4,DHCH4,EHCH4,MWCH4,flag = self.CP_coeff_NASA('CH4')
        ALHCl,BLHCl,CLHCl,DLHCl,ELHCl,AHHCl,BHHCl,CHHCl,DHHCl,EHHCl,MWHCl,flag = self.CP_coeff_NASA('HCl')
    
        MWAve=(CO2*MWCO2+CO*MWCO+O2*MWO2+H2O*MWH2O+N2*MWN2+SO2*MWSO2+H2*MWH2+CH4*MWCH4)/100.0
        
        AL = (CO2*ALCO2+CO*ALCO+H2O*ALH2O+O2*ALO2+N2*ALN2+SO2*ALSO2+H2*ALH2+CH4*ALCH4+HCl*ALHCl)/100
        AH = (CO2*AHCO2+CO*AHCO+H2O*AHH2O+O2*AHO2+N2*AHN2+SO2*AHSO2+H2*AHH2+CH4*AHCH4+HCl*AHHCl)/100
        BL = (CO2*BLCO2+CO*BLCO+H2O*BLH2O+O2*BLO2+N2*BLN2+SO2*BLSO2+H2*BLH2+CH4*BLCH4+HCl*BLHCl)/100
        BH = (CO2*BHCO2+CO*BHCO+H2O*BHH2O+O2*BHO2+N2*BHN2+SO2*BHSO2+H2*BHH2+CH4*BHCH4+HCl*BHHCl)/100
        CL = (CO2*CLCO2+CO*CLCO+H2O*CLH2O+O2*CLO2+N2*CLN2+SO2*CLSO2+H2*CLH2+CH4*CLCH4+HCl*CLHCl)/100
        CH = (CO2*CHCO2+CO*CHCO+H2O*CHH2O+O2*CHO2+N2*CHN2+SO2*CHSO2+H2*CHH2+CH4*CHCH4+HCl*CHHCl)/100
        DL = (CO2*DLCO2+CO*DLCO+H2O*DLH2O+O2*DLO2+N2*DLN2+SO2*DLSO2+H2*DLH2+CH4*DLCH4+HCl*DLHCl)/100
        DH = (CO2*DHCO2+CO*DHCO+H2O*DHH2O+O2*DHO2+N2*DHN2+SO2*DHSO2+H2*DHH2+CH4*DHCH4+HCl*DHHCl)/100
        EL = (CO2*ELCO2+CO*ELCO+H2O*ELH2O+O2*ELO2+N2*ELN2+SO2*ELSO2+H2*ELH2+CH4*ELCH4+HCl*ELHCl)/100
        EH = (CO2*EHCO2+CO*EHCO+H2O*EHH2O+O2*EHO2+N2*EHN2+SO2*EHSO2+H2*EHH2+CH4*EHCH4+HCl*EHHCl)/100
        
    #    AL,BL,CL,DL,EL,AH,BH,CH,DH,EH,MW,flag = CP_coeff_NASA('CO2')
    
        cp= self.polyAveNASA (T0,T1,AL,BL,CL,DL,EL,AH,BH,CH,DH,EH)     #(actually cp/R)        #(Tin,Tout,A,B,C,D,E)
        cp*=8.31451*1000.0/MWAve #(J/kg/K)          [R=8.31451]            REINSTATE FOR NASA COEFF
        #print 'MWAve=',MWAve
        return cp    # [J/kg/K]

################################################################################