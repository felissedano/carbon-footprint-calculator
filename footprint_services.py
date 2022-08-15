# COMP 202 A1: Part 2
# Footprint of utilities & university
# Author: Felis Sedano Luo  ID:260897013

import doctest
from unit_conversion import * 

INCOMPLETE = -1

######################################### Utilities

def fp_from_gas(monthly_gas):
    '''(num) -> float
    Calculate metric tonnes of CO2E produced annually
    based on monthly natural gas bill in $.

    Source: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852
        B.) Multiply your monthly gas bill by 105 [lbs, to get annual amount] 

    >>> fp_from_gas(0)
    0.0
    >>> round(fp_from_gas(100), 4)
    4.7627
    >>> round(fp_from_gas(25), 4)
    1.1907
    '''
    Pound = monthly_gas * 105  #simple math plus function from conversion

    KG = pound_to_kg(Pound) 
                               
    T = kg_to_tonnes(KG)       #T = tonnes
                            
    #at first I finished the function within a single line to show that I am
    #smart and economical(I am sorry Felis but you are neither smart nor
    #economical), but then the TA told me that it makes the codes hard to read
    #and I would lose marks for that so I changed my codes to what it's like
    #right now :)
    return T



def fp_from_hydro(daily_hydro):
    '''(num) -> float
    Calculate metric tonnes of CO2E produced annually
    based on average daily hydro usage.

    To find out your average daily hydro usage in kWh:
        Go to https://www.hydroquebec.com/portail/en/group/clientele/portrait-de-consommation
        Scroll down to "Annual total" and press "kWh"

    Source: https://www.hydroquebec.com/data/developpement-durable/pdf/co2-emissions-electricity-2017.pdf
        0.6 kg CO2E / MWh

    >>> fp_from_hydro(0)
    0.0
    >>> round(fp_from_hydro(10), 4)
    0.0022
    >>> round(fp_from_hydro(48.8), 4)
    0.0107
    '''
    #the stradegy is the sane as above 

    Day_KG = daily_hydro * 0.0006

    Annual_KG = daily_to_annual(Day_KG)

    T = kg_to_tonnes(Annual_KG)        

    return T

   #writing everything in one line really gave me a sense
   #of accomplishment QAQ (why are you so obssesed with coding in one line?)

def fp_of_utilities(daily_hydro, monthly_gas):
    '''(num, num, num) -> float
    Calculate metric tonnes of CO2E produced annually from
    daily hydro (in kWh) and gas bills (in $).

    >>> fp_of_utilities(0, 0)
    0.0
    >>> round(fp_of_utilities(100, 0), 4)
    0.0219
    >>> round(fp_of_utilities(0, 100), 4)
    4.7627
    >>> round(fp_of_utilities(50, 20), 4)
    0.9635
    '''

    #just have to add the two functions together  
    
    Total = fp_from_hydro(daily_hydro) + fp_from_gas(monthly_gas)  
    
    return Total     
    

#################################################


def fp_of_studies(annual_uni_credits):
    '''(num, num, num) -> flt
    Return metric tonnes of CO2E from being a student, based on
    annual university credits.

    Source: https://www.mcgill.ca/facilities/files/facilities/ghg_inventory_report_2017.pdf
        1.12 tonnes per FTE (30 credit) student

    >>> round(fp_of_studies(0), 4)
    0.0
    >>> round(fp_of_studies(30), 4)
    1.12
    >>> round(fp_of_studies(18), 4)
    0.672
    '''
    #use division to figure out tonnes per credit

    T = annual_uni_credits * (1.12/30)

    return T


#################################################

if __name__ == '__main__':
    doctest.testmod()
