
class Elements():
    '''
    Methods:
        __init__
        molar_weight
        molesperkg
    '''
    def __init__(self):
        self.x = 1.0

#==============================================================================
#   RETURN MOLAR WEIGHT OF AN ELEMENT OF MOLEQULE
#==============================================================================
    def molar_weight(self, element):
        '''
        Input (self, element)
        A dictionary containing molar weights of most elements, and additional
        made up elements to make it possible to use in fuel analysis. These
        are ash, VM and FC, and each has been given the molecular weight of 
        0.0. H2O is also present.
        
        By Angus Malmgren on 2015/02/06
        Updated by Alf Malmgren 2020-11-20, added CO, CO2, H2, CH4 and SO2
        '''
        elmolweightdict = {"H": 1.00794, "He": 4.002602, "Li":6.941,\
        "Be":9.01218,\
        "B":10.811, "C":12.0107, "N":14.0067, "O":15.9994, "F":18.9984,\
        "Ne":20.1797, "Na":22.990, "Mg":24.305, "Al":26.982, "Si":28.085,\
        "P":30.974, "S":32.065, "Cl":35.453, "Ar":39.948, "K":39.098,\
        "Ca":40.078, "Sc":44.956, "Ti":47.867, "V":50.942, "Cr":51.996,\
        "Mn":54.938, "Fe":55.845, "Co":58.933, "Ni":58.693, "Cu":63.546,\
        "Zn":65.38, "Ga":69.723, "Ge":72.630, "As":74.922, "Se":78.971,\
        "Br":79.904, "Kr":83.798, "Rb":85.468, "Sr":87.62, "Y":88.906,\
        "Zr":91.224, "Nb":92.906, "Mo":95.95,  "Tc":98, "Ru":101.07,\
        "Rh":102.906,\
        "Pd":106.42, "Ag":107.868, "Cd":112.414, "In": 114.818, "Sn":118.710,\
        "Sb":121.760, "Te":127.60, "I":126.904, "Xe":131.293, "Cs":132.905,\
        "Ba":137.327, "La": 138.905, "Hf":178.49, "Ta": 180.948, "W":183.84,\
        "Re":186.207, "Os":190.23, "Ir": 192.217, "Pt":195.084, "Au":196.967,\
        "Hg":200.592, "Tl":204.38, "Pb":207.2, "Bi": 208.9804, "Po":209,\
        "At":210, "Rn":222, "H2O": 18.01528, "ash": 0.0, "VM":0.0, "FC":0.0,\
        "NCV":0.0,"GCV":0.0, "SiO2": 60.0838, "Al2O3": 101.9622, "Fe2O3": 159.6882,\
        "TiO2": 79.8658, "CaO": 56.0774, "MgO": 40.3044, "Na2O": 61.9794,\
        "K2O": 94.1954, "Mn3O4": 228.8116, "P2O5": 141.945, "SO3": 80.0632,\
        "H2O": 18.01528, "CO":28.0102,"H2":2.01588,"CO2":44.0095, "CH4":16.04246,\
        "O2":31.9988,"N2":28.0134,"SO2":64.0638,"HCl":36.46064,"C2H4":28.05316,\
        "C2H6":30.06904,"NO":30.0061,"NO2":46.0055,"N2O":44.0128}
        
        return elmolweightdict[element]

###############################################################################
    def molesperkg(self, analysis):
        '''
        molesperkg - calculates the number of moles there is of each element in 
                     a kg of fuel
        input:
            analysis - This is a library contining the analysis of the fuel
                        of the form: analysis = {'C':inData['C']}
        output:
            moles - This is a library contining the number of moles of each 
                    element per kg: 
                    moles = {'C':inData['C']*10/molar_weight['C']}
        
        By Angus Malmgren on 2015/02/06
        '''
        moles = {}         #Create an empty dictionary called moles
        for i in analysis: # Step through all components in dictionary analysis
            if self.molar_weight(i) > 0.0:   # check so no division by 0
                moles[i] =analysis[i]*10/self.molar_weight(i)
            else:
                moles[i] = 0.0
        return moles
###############################################################################