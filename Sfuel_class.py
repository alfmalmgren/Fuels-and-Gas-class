"""
Created on Thu Jul 16 09:08:23 2020

@author: AMalmgren

Classes:
    Sfuel
Methods:
    __init__
    ar_to_db
    populate_proxult
    populate
    print_fuel
"""
import pandas as pd
from Elements_class import *
from NASA_coeff_class import *

class Sfuel(Elements, NASA_coeff):
    '''
    This class holds the analysis data for proximate and ultimate analysis
    '''
    def __init__(self):
        '''
        Initiate the variables for proximate and ultimate analysis
        '''
        #
        # Initiate the variables
        # Elements on as received, air dried, dry and dry ash free base
        self.C_ar    =  0.0
        self.C_ad    =  0.0   
        self.C_db    =  0.0
        self.C_daf   =  0.0
        self.H_ar    =  0.0
        self.H_ad    =  0.0
        self.H_db    =  0.0
        self.H_daf   =  0.0
        self.N_ar    =  0.0
        self.N_ad    =  0.0
        self.N_db    =  0.0
        self.N_daf   =  0.0
        self.S_ar    =  0.0
        self.S_ad    =  0.0
        self.S_db    =  0.0
        self.S_daf   =  0.0
        self.Cl_ar   =  0.0
        self.Cl_ad   =  0.0
        self.Cl_db   =  0.0
        self.Cl_daf  =  0.0
        self.O_ar    =  0.0
        self.O_ad    =  0.0
        self.O_db    =  0.0
        self.O_daf   =  0.0
        
        # Elements moles per kg as received
        self.C_molesperkgar  =  0.0
        self.H_molesperkgar  =  0.0
        self.N_molesperkgar  =  0.0
        self.S_molesperkgar  =  0.0
        self.Cl_molesperkgar =  0.0
        self.O_molesperkgar  =  0.0
        
        # Proximate analysis
        self.Ash_ar  =  0.0
        self.Ash_ad  =  0.0
        self.Ash_db  =  0.0
        self.NCV_ar  =  0.0
        self.NCV_ad  =  0.0
        self.NCV_db  =  0.0
        self.NCV_daf =  0.0
        self.GCV_ar  =  0.0
        self.GCV_ad  =  0.0
        self.GCV_db  =  0.0
        self.GCV_daf =  0.0
        self.VM_ar   =  0.0
        self.VM_ad   =  0.0
        self.VM_db   =  0.0
        self.VM_daf  =  0.0
        self.H2O_ar  =  0.0
        self.H2O_inh =  0.0
        self.Swelling = 0.0
        self.HGI      = 0.0
        self.FR       = 0.0
        self.FC_ar    = 0.0
                
        # Ash
        self.SiO2  =  0.0
        self.Al2O3 =  0.0
        self.Fe2O3 =  0.0
        self.TiO2  =  0.0
        self.CaO   =  0.0
        self.MgO   =  0.0
        self.Na2O  =  0.0
        self.K2O   =  0.0
        self.MnO   =  0.0
        self.Mn3O4 =  0.0
        self.P2O5  =  0.0
        self.SO3   =  0.0
        self.BaO   =  0.0
        self.ZnO   =  0.0
        self.CuO   =  0.0
        self.NiO   =  0.0
        self.PbO   =  0.0
        self.WO3   =  0.0
        self.ZrO2  =  0.0
        self.V2O5  =  0.0
        self.Cr2O3 =  0.0
        self.SrO   =  0.0
        
        # Trace elements
        self.Al        = 0.0
        self.Sb        = 0.0
        self.Arsenic   = 0.0
        self.Ba        = 0.0
        self.Be        = 0.0
        self.Bo        = 0.0
        self.Cd        = 0.0
        self.Cr        = 0.0
        self.Ca        = 0.0
        self.Co        = 0.0
        self.Cu        = 0.0
        self.F         = 0.0
        self.Fe        = 0.0
        self.Pb        = 0.0
        self.Mg        = 0.0
        self.Mn        = 0.0
        self.Hg        = 0.0
        self.Mo        = 0.0
        self.Ni        = 0.0
        self.P         = 0.0
        self.K         = 0.0
        self.Se        = 0.0
        self.Si        = 0.0
        self.Ag        = 0.0
        self.Na        = 0.0
        self.Th        = 0.0
        self.Sn        = 0.0
        self.Ti        = 0.0
        self.U         = 0.0
        self.V         = 0.0
        self.Zn        = 0.0
        self.Sr        = 0.0
        self.Te        = 0.0
        self.Asbestos  = 0.0
            
        #mol per kg dry fuel
        self.molC   =  0.0
        self.molH   =  0.0
        self.molN   =  0.0
        self.molS   =  0.0
        self.molCl  =  0.0
        self.molO   =  0.0
        self.molH2O =  0.0  # total moisture as received
        
        self.molAl       = 0.0
        self.molTi       = 0.0
        self.molFe       = 0.0
        self.molP        = 0.0
        self.molSi       = 0.0
        self.molMg       = 0.0
        self.molNa       = 0.0
        self.molCa       = 0.0
        self.molK        = 0.0
        self.molMn       = 0.0
        self.molZn       = 0.0
        
        self.molSb       = 0.0
        self.molArsenic  = 0.0
        self.molBa       = 0.0
        self.molBe       = 0.0
        self.molBo       = 0.0
        self.molCd       = 0.0
        self.molCr       = 0.0
        self.molCo       = 0.0
        self.molCu       = 0.0
        self.molF        = 0.0
        self.molPb       = 0.0
        self.molHg       = 0.0
        self.molMo       = 0.0
        self.molNi       = 0.0
        self.molSe       = 0.0
        self.molAg       = 0.0
        self.molTh       = 0.0
        self.molSn       = 0.0
        self.molU        = 0.0
        self.molV        = 0.0
        self.molSr       = 0.0
        self.molTe       = 0.0
        self.molAsbestos = 0.0
        
        # Ash fusion temperatures
        self.IDT_ox  = 0.0
        self.ST_ox   = 0.0
        self.HT_ox   = 0.0
        self.FT_ox   = 0.0
        self.IDT_red = 0.0
        self.ST_red  = 0.0
        self.HT_red  = 0.0
        self.FT_red  = 0.0

        #Variables for indices
        self.SCl          = 0.0
        self.WI           = 0.0
        self.SA           = 0.0
        self.BA           = 0.0
        self.BA2          = 0.0
        self.Na2O         = 0.0
        self.CaO          = 0.0
        self.KCl          = 0.0
        self.S            = 0.0
        self.Cl           = 0.0
        self.SiO2         = 0.0
        self.alkali_ratio = 0.0
        self.SlagIndex1   = 0.0
        self.SlagIndex2   = 0.0
        self.SlagIndexRS  = 0.0
        self.StoAlkali    = 0.0
        self.AN           = 0.0
        self.SiAl         = 0.0
        self.ST           = 0.0
        self.KT           = 0.0
        self.CT           = 0.0
        self.Glass        = 0.0
        self.Salt1        = 0.0
        self.Salt2        = 0.0
        self.Feldspar     = 0.0
        self.Tad          = 0.0   # Adiabatic flame temp

        self.massflow     = 0.0   # [kg/s]
        self.temperature  = 0.0   # [K]
        
        # Lists
        self.content = []
        self.explode = []
        self.labels  = []
        # Flags
        self.flags    = {'trace':0, 'ash':0, 'fusion':0}

###############################################################################
    def ar_to_db(self, element, moisture):
        '''
        Convert analysis from as received base to dry base
        element  = % of element on ar base
        moisture = total moisture content, but total - inherent will give ad base
        returns concentration on dry base
        '''
        if element>0.0 and element <= 100.0:
            if moisture>0.0 and moisture<=100.0:
                element = element * 100 / (100 - moisture)
            elif moisture == 0.0:
                element = element     # 0% moisture => no change
            else:
                print('Moisture out of range')
                element = -2000.0
        elif element == 0.0:
            element = 0.0
        else:  #test_ar_to_db
            print('Element out of range')
            element = -1000.0
        return element
###############################################################################
    def populate_proxult(self,base,C=0,H=0,N=0,S=0,Cl=0,O=0,Ash=0,moist=0,\
                         VM=0,FC=0,NCV=0,GCV=0):
        '''
        NCV     Given in MJ/kg converted to J/kg for internal use
        '''
        if base=='ar':
            # Ultimate
            self.C_ar    =  C
            self.H_ar    =  H
            self.N_ar    =  N
            self.S_ar    =  S
            self.Cl_ar   =  Cl
            if O==0.0:
                self.O_ar = 0.0
            else:
                self.O_ar = O
            # Proximate
            self.Ash_ar = Ash
            self.H2O_ar = moist
            self.VM_ar  = VM
            self.FC_ar  = FC
            self.NCV_ar = NCV * 1.0e6
###############################################################################
    def populate_masstemp(self, massflow, temperature):
        self.massflow  = massflow     # [kg/s]
        self.T0        = temperature   # [K]
###############################################################################
    def populate_ashfusion(self,IDT_ox=0,ST_ox=0,HT_ox=0,FT_ox=0,IDT_red=0,\
                           ST_red=0,HT_red=0,FT_red=0):
        
        self.IDT_ox_C  = IDT_ox
        self.ST_ox_C   = ST_ox
        self.HT_ox_C   = HT_ox
        self.FT_ox_C   = FT_ox
        self.IDT_red_C = IDT_red
        self.ST_red_C  = ST_red
        self.HT_red_C  = HT_red
        self.FT_red_C  = FT_red

###############################################################################
    def populate(self):
        '''
        Populate the solid fuel object
        Calculate proximate and ultimate analysis on all bases
        Calculate moles per kg of all elements and also all ash components

        '''                
#        if not self.H2O_ar>0.0:             # If no total moisture assume it is the same as inherent.
#            if not self.H2O_inh>0.0:        # If no inherent moisture assume it is zero
#                self.H2O_inh = 0.0
#            self.H2O_ar = self.H2O_inh
        
        base = []
        if self.C_ar > 0.0:    # Check if as received
            base.append('ar')
            if not self.O_ar>0.0:
                self.O_ar=100-(self.C_ar + self.N_ar + self.H_ar + self.S_ar + self.Cl_ar + self.H2O_ar + self.Ash_ar)
            Tot_ar = self.C_ar + self.N_ar + self.H_ar + self.S_ar + self.Cl_ar + self.O_ar + self.H2O_ar + self.Ash_ar
        
        if (self.C_db > 0.0):  # Check dry base
            # Dry basis
            base.append('db')
            if not self.O_db>0.0:
                self.O_db=100-(self.C_db + self.N_db + self.H_db + self.S_db + self.Cl_db + self.Ash_db)
            Tot_db = self.C_db + self.N_db + self.H_db + self.S_db + self.Cl_db + self.O_db + self.Ash_db
            
        if (self.C_ad > 0.0): # Check if air dry base
            # Air dried basis
            base.append('ad')
            if not self.O_ad>0.0:
                self.O_ad=100-(self.C_ad + self.N_ad + self.H_ad + self.S_ad + self.Cl_ad + self.H2O_inh + self.Ash_ad)
            Tot_ad = self.C_ad + self.N_ad + self.H_ad + self.S_ad + self.Cl_ad + self.O_ad + self.H2O_inh + self.Ash_ad
        
        if (self.C_daf > 0.0): # Check if daf
            # Dry ash free basis
            base.append('daf')
            if not self.O_daf>0.0:
                self.O_daf=100-(self.C_adf + self.N_daf + self.H_daf + self.S_daf + self.Cl_daf)
            Tot_daf = self.C_daf + self.N_daf + self.H_daf + self.S_daf + self.Cl_daf + self.O_daf
        
      #  print('base = ',base)
        if ('ar' in base) and ('db' not in base):  # If as received, convert to dry base
            # Calculate db
            base.append('db')
            Tot_db = Tot_ar - self.H2O_ar #
            self.C_db    = self.C_ar   / Tot_db * Tot_ar
            self.N_db    = self.N_ar   / Tot_db * Tot_ar
            self.H_db    = self.H_ar   / Tot_db * Tot_ar
            self.S_db    = self.S_ar   / Tot_db * Tot_ar
            self.Cl_db   = self.Cl_ar  / Tot_db * Tot_ar
            self.O_db    = self.O_ar   / Tot_db * Tot_ar
            self.Ash_db  = self.Ash_ar / Tot_db * Tot_ar
            Tot_db = self.C_db + self.N_db + self.H_db + self.S_db + self.Cl_db + self.O_db + self.Ash_db
    
        if ('ad' in base) and ('db' not in base):  # If air dried, convert to dry base
            # Calculate db
            base.append('db')
            Tot_db = Tot_ad - self.H2O_inh #
            self.C_db    = self.C_ad   / Tot_db * Tot_ad
            self.N_db    = self.N_ad   / Tot_db * Tot_ad
            self.H_db    = self.H_ad   / Tot_db * Tot_ad
            self.S_db    = self.S_ad   / Tot_db * Tot_ad
            self.Cl_db   = self.Cl_ad  / Tot_db * Tot_ad
            self.O_db    = self.O_ad   / Tot_db * Tot_ad
            self.Ash_db  = self.Ash_ad / Tot_db * Tot_ad
            Tot_db = self.C_db + self.N_db + self.H_db + self.S_db + self.Cl_db + self.O_db + self.Ash_db        
            
        if ('daf' in base) and ('db' not in base):  # If dry ash free, convert to dry base
            # Calculate db
            base.append('db')
            if self.Ash_db > 0.0:
                self.Ash_db   = self.Ash_db
            Tot_db = Tot_daf + self.Ash_db #
            self.C_db    = self.C_daf   / Tot_db * Tot_daf
            self.N_db    = self.N_daf   / Tot_db * Tot_daf
            self.H_db    = self.H_daf   / Tot_db * Tot_daf
            self.S_db    = self.S_daf   / Tot_db * Tot_daf
            self.Cl_db   = self.Cl_daf  / Tot_db * Tot_daf
            self.O_db    = self.O_daf   / Tot_db * Tot_daf
            Tot_db = self.C_db + self.N_db + self.H_db + self.S_db + self.Cl_db + self.O_db + self.Ash_db
    
        # Calculate daf from db
        if ('daf' not in base) and ('db' in base):
            base.append('daf')
            Tot_daf = Tot_db - self.Ash_db #
            self.C_daf    = self.C_db   / Tot_daf * Tot_db
            self.N_daf    = self.N_db   / Tot_daf * Tot_db
            self.H_daf    = self.H_db   / Tot_daf * Tot_db
            self.S_daf    = self.S_db   / Tot_daf * Tot_db
            self.Cl_daf   = self.Cl_db  / Tot_daf * Tot_db
            self.O_daf    = self.O_db   / Tot_daf * Tot_db
            
        #if base!='daf':
        # Convert from dry base to as received
        if ('ar' not in base) and ('db' in base):
            base.append('ar')
           # if self.H2O_ar > 0.0: 
            #    self.H2O_ar = self.H2O_ar    NEED TO DEAL WITH IF TOT MOIST IS MISSING<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            Tot_ar = Tot_db + self.H2O_ar   #
            self.C_ar    = self.C_db   / Tot_ar * Tot_db
            self.N_ar    = self.N_db   / Tot_ar * Tot_db
            self.H_ar    = self.H_db   / Tot_ar * Tot_db
            self.S_ar    = self.S_db   / Tot_ar * Tot_db
            self.Cl_ar   = self.Cl_db  / Tot_ar * Tot_db
            self.O_ar    = self.O_db   / Tot_ar * Tot_db
            self.Ash_ar  = self.Ash_db / Tot_ar * Tot_db
            self.C_ar=self.C_ar

        self.molCl = self.Cl_db*10.0/35.453     # mol/kg dry fuel
        self.molS = self.S_db*10.0/32.065       # ------ " ------
        self.molC = self.C_db*10.0/12.0107      # ------ " ------
        self.molH = self.H_db*10.0/1.00794      # ------ " ------
        self.molN = self.N_db*10.0/14.0067      # ------ " ------
        self.molO = self.O_db*10.0/15.9994      # ------ " ------
        self.molH2O = self.H2O_ar*10.0/18.01528 # ------ " ------

        if self.H2O_ar>0.0:
            self.H2O_ar  =  self.H2O_ar
            #self.H2O_ad  =  self.H2O_inh
        
        #mol of elements in 1 kg dry fuel
        self.molAl = self.Al2O3*2.0*10.0/101.9582*self.Ash_db/100.0
        self.molTi = self.TiO2  *   10.0/79.8658 *self.Ash_db/100.0
        self.molFe = self.Fe2O3*2.0*10.0/159.6882*self.Ash_db/100.0
        self.molP  = self.P2O5 *2.0*10.0/141.9445*self.Ash_db/100.0
        self.molSi = self.SiO2 *    10.0/ 60.0843*self.Ash_db/100.0
        self.molMg = self.MgO  *    10.0/40.3044 *self.Ash_db/100.0
        self.molS  = self.SO3  *    10.0/80.0632 *self.Ash_db/100.0
        self.molNa = self.Na2O*2.0* 10.0/61.9789 *self.Ash_db/100.0
        self.molCa = self.CaO   *   10.0/56.0774 *self.Ash_db/100.0
        self.molK  = self.K2O*2.0 * 10.0/94.196  *self.Ash_db/100.0
        self.molMn = self.Mn3O4*3.0*10.0/228.8116*self.Ash_db/100.0

    # Trace elements
        self.molAl = self.Al/1000/26.981538  # mg/kg dry fuel
        self.molTi = self.Ti/1000/47.867     # mg/kg dry fuel
        self.molFe = self.Fe/1000/55.845     # mg/kg dry fuel
        self.molP  = self.P /1000/30.973761  # mg/kg dry fuel
        self.molSi = self.Si/1000/28.0855    # mg/kg dry fuel
        self.molMg = self.Mg/1000/24.305     # mg/kg dry fuel
        self.molNa = self.Na/1000/22.98977   # mg/kg dry fuel
        self.molCa = self.Ca/1000/40.078     # mg/kg dry fuel
        self.molK  = self.K /1000/39.0983    # mg/kg dry fuel
        self.molMn = self.Mn/1000/54.938049  # mg/kg dry fuel
        #self.molCl = self.Cl/1000/35.453    # mg/kg dry fuel
        #self.molS  = self.S /1000/32.065    # mg/kg dry fuel
        self.molZn = self.Zn/1000/65.409     # mg/kg dry fuel
            
###############################################################################
    def print_fuel(self):
        #Add output on all bases to list that will be returned
        print("\n\n==================== Fuel analysis ====================")
        print("\nULTIMATE:")
        print("    as recieved    Dry base    Dry ash free")
        print("C:     %6.2f       %6.2f        %6.2f   %%" % (self.C_ar,self.C_db,self.C_daf))
        print('N:     %6.2f       %6.2f        %6.2f   %%' % (self.N_ar, self.N_db, self.N_daf))
        print('H:     %6.2f       %6.2f        %6.2f   %%' % (self.H_ar, self.H_db, self.H_daf))
        print('S:     %6.2f       %6.2f        %6.2f   %%' % (self.S_ar, self.S_db, self.S_daf))
        print('Cl:    %6.2f       %6.2f        %6.2f   %%' % (self.Cl_ar, self.Cl_db, self.Cl_daf))
        print('O:     %6.2f       %6.2f        %6.2f   %%' % (self.O_ar, self.O_db, self.O_daf))
        print("H2O:   %6.2f        -----         -----   %%" % (self.H2O_ar))
        print("ash:   %6.2f       %6.2f         -----   %%" % (self.Ash_ar, self.Ash_db))
        print("------------------------------------------")
  #      print("Total: %6.2f       %6.2f        %6.2f   %%\n\n" % (self.Tot_ar,self.Tot_db,self.Tot_daf))
        print("")
        print("Inherent moisture: %6.2f  %%" % (self.H2O_inh))
        print("")
        
        self.FC_ar = 100.0 - self.VM_ar - self.Ash_ar - self.H2O_ar
        print("PROXIMATE:")
     #   print("Total moisture:     %5.1f %%" % (self.H2O_ar))
        if self.FC_ar > 0.0:  print('Fixed Carbon:       %5.1f %% as rec.' % self.FC_ar)
        if self.VM_ar > 0.0:  print('Volatile matter:    %5.1f %% as rec.' % self.VM_ar)
        if self.H2O_ar > 0.0: print("Total moisture:     %5.1f %% as rec." % (self.H2O_ar))
        if self.Ash_ar > 0.0: print("Ash:                %5.1f %% as rec." % (self.Ash_ar))
        print("------------------------------------")
        print("Total:              %5.1f %%\n" % (self.FC_ar+self.VM_ar+self.H2O_ar+self.Ash_ar))
        print("")
        if self.NCV_ar > 0.0: print('NCV:                % 4.2f [MJ/kg as rec.]' % (self.NCV_ar/1.0e6))
        if self.GCV_ar > 0.0: print('GCV:                % 4.2f [MJ/kg as rec.]\n' % (self.GCV_ar/1.0e6))
        print("")

        if self.VM_ar>0.0:
            self.FR = self.FC_ar/self.VM_ar
            print('Fuel ratio (FR):    % 4.2f %% as rec.\n' % (self.FR))
            if self.FR>1.5:
                print('FR=%.2f>1.5 means that this fuel can be milled in air\n' % (self.FR))
            elif self.FR>1.0:
                print('1.0<FR=%.2f<1.5 means that causion is required when milling this fuel, explosion mitigation, ' % (self.FR))
                print('like mill inertion or explosion suppression should be considered\n')
            else:
                print('FR=%.2f<1.0 means that this fuel should not be milled without explosion mitigation like' % (self.FR))
                print('mill inertion or explosion suppression in service\n')
            
        else:
            print('Not possible to calculate Fuel ratio (FR) as VM = 0.0.\n')
      #  else:
       #     print('NOT POSSIBLE TO CALCULATE ANALYSIS ON AS RECEIVED BASIS WITHOUT TOTAL MOISTURE\n\n')
            

        bulkDensity = (1.534-((0.05196*self.H_daf)+(0.007375*self.O_daf)-(0.02472*self.N_daf)+(0.003853*self.S_daf)))*1000.0
       # print ('The bulk density is estimated to: %5.0f kg/m3 (uncertain estimation only valid for coal)' % bulkDensity)
        
        print('\n')
        print('The bulk density is estimated to: %5.0f kg/m3 (uncertain estimation only valid for coal)\n' % bulkDensity)
        
        # Ash
        sum=self.Al2O3+self.Fe2O3+self.SiO2+self.TiO2+self.CaO+self.MgO+self.Na2O+self.K2O+self.MnO+self.P2O5+self.SO3
        
        print('  ASH COMPOSITION')    #Ash composition
        print('Al2O3 = %5.2f %% %8.4f moles/kg fuel ' % (self.Al2O3,self.molAl/2))
        print('Fe2O3 = %5.2f %% %8.4f moles/kg fuel ' % (self.Fe2O3,self.molFe/2))
        print('SiO2  = %5.2f %% %8.4f moles/kg fuel ' % (self.SiO2,self.molSi))
        print('TiO2  = %5.2f %% %8.4f moles/kg fuel ' % (self.TiO2,self.molTi))
        print('CaO   = %5.2f %% %8.4f moles/kg fuel ' % (self.CaO,self.molCa))
        print('MgO   = %5.2f %% %8.4f moles/kg fuel ' % (self.MgO,self.molMg))
        print('Na2O  = %5.2f %% %8.4f moles/kg fuel ' % (self.Na2O,self.molNa/2))
        print('K2O   = %5.2f %% %8.4f moles/kg fuel ' % (self.K2O,self.molK/2))
        print('MnO   = %5.2f %% %8.4f moles/kg fuel ' % (self.MnO,self.molMn))
        print('P2O5  = %5.2f %% %8.4f moles/kg fuel ' % (self.P2O5,self.molP/2))
        print('SO3   = %5.2f %% %8.4f moles/kg fuel ' % (self.SO3,self.molS))
        print('--------------------------------------')
        print('Sum   =  %5.2f %% ' % (sum))
        print('\n')
        
        if (self.IDT_ox!=0 or self.ST_ox!=0 or self.HT_ox!=0 or self.FT_ox!=0 or\
            self.IDT_red!=0 or self.ST_red!=0 or self.HT_red!=0 or self.FT_red!=0):
            print('\nASH FUSION TEMPERATURES')
            print('      Oxidising    Reducing')
            print('IDT   %5.0f       %5.0f  (°C)' % (self.IDT_ox, self.IDT_red))
            print('ST    %5.0f       %5.0f  (°C)' % (self.ST_ox, self.ST_red))
            print('HT    %5.0f       %5.0f  (°C)' % (self.HT_ox, self.HT_red))
            print('FT    %5.0f       %5.0f  (°C)' % (self.FT_ox, self.FT_red))
###############################################################################
    def flue_gas(self, percO2, FG, oxidiser, NCV, verbose=0):
        '''
        This function calculates the fluegas composition, volume and mass of 
        flue gas produced from combustion of one kg fuel and the amount of 
        air required both as volume and mass.
        
        This is done for both the stoichiometric case (0% O2 in flue gas) and 
        for a flue gas with the O2 concentration given in the input parameters.
        
        Input:
            self          An onject of the Sfuel class containing the 
                          composition of the fuel
            percO2    -   Percent O2 in the flue gas
            FG        -   gas object for the flue gas

            NCV       -   Net Calorific Value [J/kg fuel]
            verbose   -   0 = no printout, 1=some printout, 2=all printout
      #      Ash       -   Ash content in the fuel [%]
      #      S         -   S content in the fuel [%]
      #      extra_H2O -   Additional water [moles/kg fuel]
        
        Output:
            listfg    -    The results of the calculations are returned in a list
                           of strings that can be added to a master list of strings
                           for later saving to file or printing to screen.
            The results of the calculations are printed to the screen.
            
            
        By: 
        Latest update: 2015-02-13
        '''
   #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<     
        extra_H2O = 0.0    # For now add in later
        
        #  moles CO2 in flue gas => moles C in coal
        molesCO2 = self.molC
        #  moles HCl in flue gas = moles Cl
        molesHCl = self.molCl
        #  H2O in flue gas = H2O in coal + 2*H + O - HCl
        molesH2O = self.molH2O+(self.molH-molesHCl)/2.0+extra_H2O
        #  moles SO2 in flue gas = moles S in coal
        molesSO2 = self.molS
        #Oxygen required
        # O2 + C => CO2
        # 4 * H + O2 => 2 * H2O
        # O2 + S => SO2

        #Required oxygen for stoichiometric combustion minus oxygen in the fuel
        O2_req = molesCO2 + self.molH/4.0 + molesSO2 - self.molO/2.0
        #Required air to provide this oxygen
        air_req = O2_req/0.21
        #Nitrogen in the added air and in the fuel
        molesN2 = air_req * 0.79 + self.molN/2.0
        #Convert to volume %
        moles_tot = molesCO2+molesH2O+molesSO2+molesHCl+molesN2+molesHCl
        #CO2 = molesCO2/moles_tot*100.0
        #H2O = molesH2O/moles_tot*100.0
        #SO2 = molesSO2/moles_tot*100.0
        #HCl = molesHCl/moles_tot*100.0
        #N2  = molesN2/moles_tot*100.0
        #tot = CO2+H2O+SO2+N2+HCl
        
        #Calculate the flue gas composition with percO2 % O2
        # moles O2 that needs to be added
        nmolesO2 = percO2 * moles_tot / (100 - percO2*100/21)
        #moles N2 in the extra air
        nmolesN2 = nmolesO2*79/21
        #Total moles in the flue gas
        nmoles_tot = moles_tot + nmolesO2 + nmolesN2
        #Total moles in dry flue gas
        dry_nmoles_tot = nmoles_tot - molesH2O
        
        smolesCO = 0.0
        
        #Flue gas volume per kg of fuel
        FGvolume     = nmoles_tot * 0.0224136
        FGvolume_dry = dry_nmoles_tot * 0.0224136
        nair_req     = (nmolesO2 + nmolesN2 + air_req) * 0.0224136
        airmass      = nair_req * 1.29304  #1.29304 = air density at 0C and 1 atm. [kg/m3]
        FG.Massflow  = airmass + 1.0 + extra_H2O * 18.0 / 1000.0 # Added air, fuel and water [kg FG/kg fuel]
        
        # NCV
        FG.NCV_given = self.massflow * self.NCV_ar / FG.Massflow
        
        #Ash concentration in flue gas wet   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        AshInFG       = self.Ash_ar*10000.0/FGvolume               #[mg ash/Nm3 flue gas]
        CleanAshInFG  = AshInFG*0.01
        Ashpertonne   = self.Ash_ar*10.0                           #[kg ash/t fuel]
        AshperGJ      = self.Ash_ar*10.0/NCV*1.0e6                 #[kg ash/GJ fuel]
        CleanAshPert  = 20.0e-3 * FGvolume * 1000.0                #[g ash/t fuel]
        CleanAshPerGJ = 20.0e-3 * FGvolume * 1.0e9/NCV             #[g ash/GJ fuel]
        
        #Ash concentration in dry flue gas
        AshInFG_dry = self.Ash_ar*10000.0/FGvolume_dry
        CleanAshInFG_dry=AshInFG_dry*0.01
        
        #Required efficiecy of Fields
        oneField    = 1.0-(20./AshInFG)
        twoFields   = 1.0-(20./AshInFG)**(1.0/2.0)
        threeFields = 1.0-(20./AshInFG)**(1.0/3.0)
        fourFields  = 1.0-(20./AshInFG)**(1.0/4.0)
        fiveFields  = 1.0-(20./AshInFG)**(1.0/5.0)
        
        #Concentration SO2 in the flue gas wet
        SO2InFG = self.S_ar*10000.0/FGvolume/32.064*64.0628     #mg SO2/Nm3 flue gas
        
        #Concentration SO2 in the flue gas dry
        SO2InFG_dry = self.S_ar*10000.0/FGvolume_dry/32.064*64.0628
    
        #Concentration NOx in the flue gas wet
        NO2InFG = self.N_ar*10000.0/FGvolume/14.0067*46.0055     #mg NO2/Nm3 flue gas
        
        #Concentration NOx in the flue gas dry
        NO2InFG_dry = self.N_ar*10000.0/FGvolume_dry/14.0067*46.0055
    
        #Percent flue gas composition wet
        nCO2 = molesCO2/nmoles_tot*100.0
        nO2  = nmolesO2/nmoles_tot*100.0
        nH2O = molesH2O/nmoles_tot*100.0
        nSO2 = molesSO2/nmoles_tot*100.0
        nHCl = molesHCl/nmoles_tot*100.0
        nN2  = (molesN2+nmolesN2)/nmoles_tot*100.0
        ntot = nCO2+nH2O+nSO2+nN2+nHCl+nO2
    
        #Percent flue gas composition dry
        dry_nCO2 = molesCO2/dry_nmoles_tot*100.0   
        dry_nO2  = nmolesO2/dry_nmoles_tot*100.0
        dry_nH2O = 0.0
        dry_nSO2 = molesSO2/dry_nmoles_tot*100.0
        dry_nHCl = molesHCl/dry_nmoles_tot*100.0
        dry_nN2  = (molesN2+nmolesN2)/dry_nmoles_tot*100.0
        dry_ntot = dry_nCO2+dry_nSO2+dry_nN2+dry_nHCl+dry_nO2
    
     #   percentGasDict={'CO2':nCO2,'O2':nO2,'H2O':nH2O,'SO2':nSO2,'HCl':nHCl,'N2':nN2, 'CO':0.0}
        massflow = self.massflow * (1 + nair_req)
        if verbose>0:
            print('Populating FG with massflow:',massflow)
        FG.populate(Name='',CO2=nCO2,O2=nO2,H2O=nH2O,SO2=nSO2,HCl=nHCl,N2=nN2,CO=0.0,massflow=massflow,NCV=NCV)
        
        Temp0=20.0+273.15
        
        # NCV given per kg of solid fuel, must be converted to per kg of gas  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
        
        self.Tad = FG.Tad(NCV, airmass)   # Calculate the adiabatic flame temperature
        Cp = FG.gas_cp(Temp0,self.Tad)

        #CO2 emissions inkg/t fuel
        CO2pertonne = molesCO2*44.0095
        if verbose>0: 
            print("\n\n==================== Flue gas at %6.2f %% O2 (wet gas) ====================" % percO2 )
            print("\n\nFLUE GAS COMPOSITION")
            print("         (wet)     (dry)")
            print('CO2:    %6.2f %%  %6.2f %%' % (nCO2, dry_nCO2))
            print('H2O:    %6.2f %%  %6.2f %%' % (nH2O, dry_nH2O))
            print('SO2:    %6.2f %%  %6.2f %%' % (nSO2, dry_nSO2))
            print('HCl:    %6.2f %%  %6.2f %%' % (nHCl, dry_nHCl))
            print('N2:     %6.2f %%  %6.2f %%' % (nN2, dry_nN2))
            print('O2:     %6.2f %%  %6.2f %%' % (nO2, dry_nO2))
            print('Tot:    %6.2f %%  %6.2f %%\n' % (ntot, dry_ntot))
        
            print("Flue gas volume per kg fuel:       %7.2f Nm3" % FGvolume)
            print("Flue gas mass per kg fuel:         %7.2f kg" % FG.Massflow)
            print("Air requirement per kg fuel:       %7.2f Nm3" % nair_req)
            print("Required air mass per kg fuel:     %7.2f kg" % airmass)
            print("")
            print("Adiabatic temperature:             %7.2f degrees C" % (self.Tad-273.15))
            print("Cp of the flue gas:                %7.2f J/kg/K\n" % (Cp))
            
        if verbose>1:    
            print("Concentration ash in wet flue gas:    %.0f mg/Nm3 or %.0f mg/Nm3 in dry gas" % (AshInFG,AshInFG_dry))
            print("or: %.1f kg ash/t fuel or: %.4f kg ash/GJ fuel" % (Ashpertonne,AshperGJ))
            
            print("Flue gas cleaned to 20 mg particulate per Nm3, would produce: %.2f g ash/t fuel or %.2f g ash/GJ fuel\n" % (CleanAshPert,CleanAshPerGJ))
            print("99%% filter efficiency would give: %.0f mg/Nm3 or %.0f mg/Nm3 in dry gas\n" % (CleanAshInFG,CleanAshInFG_dry))
            print('1 ESP field would have to be %4.1f %% efficient to achieve 20 mg/Nm3 particulate in the flue gas ' % (oneField*100.0))
            print('2 ESP fields would have to be %3.0f %% efficient each to achieve 20 mg/Nm3 particulate in the flue gas ' % (twoFields*100.0))
            print('3 ESP fields would have to be %3.0f %% efficient each to achieve 20 mg/Nm3 particulate in the flue gas ' % (threeFields*100.0))
            print('4 ESP fields would have to be %3.0f %% efficient each to achieve 20 mg/Nm3 particulate in the flue gas ' % (fourFields*100.0))
            print('5 ESP fields would have to be %3.0f %% efficient each to achieve 20 mg/Nm3 particulate in the flue gas ' % (fiveFields*100.0))
            print("\n")
            print("Concentration SO2 in wet flue gas:    %.0f mg/Nm3 or %.0f mg/Nm3 in dry gas" % (SO2InFG , SO2InFG_dry))
            print("Assuming 100% conversion of fuel S to SO2 and no capture.")
            print("Concentration fuel NOx in wet flue gas:    %.0f mg/Nm3 or %.0f mg/Nm3 in dry gas" % (NO2InFG , NO2InFG_dry))
            print("Assuming 100% conversion of fuel N to NO2 and no reduction of other NOx sources.")

        #CO2 emissions in kg/GJ
            if FG.NCV_given>0.0:
                CO2emission = molesCO2/FG.NCV_given*44.0095e6
                print("\nEmissions of CO2 will be %.2f kg/GJ fuel and %.2f kg/t fuel" % (CO2emission, CO2pertonne))
        print("\n")

        
#        plt.figure()
#        ax = plt.axes()
#        x = np.linspace(0, 200, 50)
#        y = FGmass * x / proxult1.NCV_ar  * 1e6
#        yy = airmass * x / proxult1.NCV_ar * 1e6
#        xlabel  = 'Flue gas flow at {}% O2'.format(percO2)
#        xxlabel = 'Air requirement at {}% O2'.format(percO2)
#        ax.plot(x,  y, label = xlabel )  #'Stoichiometric flue gas flow')
#        ax.plot(x, yy, label = xxlabel)  #'Stoichiometric air requirement')
        
#        ax.set(xlim = (0,200), ylim = (0, FGmass * 200 / proxult1.NCV_ar * 1e6), xlabel='Load [MWth]', 
#               ylabel='FG mass flow [kg FG/s]', title='Air and flue gas flow')
#        ax.legend(loc = 'lower right')
        #fig.show()
#        plt.show()
            
        return nair_req