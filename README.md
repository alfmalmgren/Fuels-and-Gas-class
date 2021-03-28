A project for a fuels and a gas class

# Classes:<br/>
> **Elements**<br/>
> **NASA_coeff**<br/>
> **Sfuel**<br/>
> **Ggas**<br/>
# Methods:<br/>
## Elements:<br/>
> **molar_weight:** Returne the molar weight of an element.<br/>
> **molesperkg:** Returns the number of moles in a kg of an element.<br/>
## NASA_coeff:<br/>
> **cp_coeff_NASA**<br/>
> **polyaveNASA**<br/>
> **gas_cp:** Returns the average Cp for a gas in a given temperature interval.<br/>
## Sfuel:<br/>
> **ar_to_db:** Convert from as received base to dry base.<br/>
> **populate_proxult**<br/>
> **populate_masstemp**<br/>
> **populate_ashfusion**<br/>
> **populate**<br/>
> **print_fuel:** Print the held properties of a solid fuel.<br/>
> **flue_gas:** Calculate the composition of the flue gas from combustion of a solid fuel with a given oxidiser.<br/>
## Ggas:<br/>
> **populate**<br/>
> **update**<br/>
> **mix:** Mix two gas object.<br/>
> **CV_gas:** Return the calorific value of aa given gas.<br/>
> **burn:** Calculate the result of the combustion of a given solid fuel and oxidiser with given mass flows.<br/>
> **burn_stoich:** Calculate the result of the combustion of a given solid fuel and oxidiser at stoichiometric proportions.<br/>
> **Tad:** Calculate the adiabatic flame temperature for a given fuel and oxidiser.<br/>
> **print:** Print the held properties of a gas.<br/>
