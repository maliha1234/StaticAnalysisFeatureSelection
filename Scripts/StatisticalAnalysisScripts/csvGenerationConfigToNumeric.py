import pandas
import sys
import glob
import os
from collections import defaultdict


postAnalysisDirectory = sys.argv[1]
programName = sys.argv[2]

try:
    
     aiCsvFileName = postAnalysisDirectory + programName + ".csv"
     aiCsv = pandas.read_csv(aiCsvFileName)
     print(aiCsvFileName)
     

     # Create the dictionary with 1,2,3 random values
     c1_dictionary ={'TD' : 1, 'BU' : 2, 'TD+BU' : 3} 
     c2_dictionary ={'AP' : 1, 'SO' : 2, 'AP+SO' : 3} 
     c3_dictionary ={'1-CFA' : 1, 'CI' : 2, '1-TYPE' : 3}   
     c4_dictionary ={'ALLOCATION' : 1, 'SMUSH_STRING' : 2, 'TYPE' : 3}    
     c5_dictionary ={'BOX' : 1, 'POLY' : 2}  
     


  
     # Add new columns
     aiCsv['C1*'] = aiCsv['C1'].map(c1_dictionary) 
     aiCsv['C2*'] = aiCsv['C2'].map(c2_dictionary)
     aiCsv['C3*'] = aiCsv['C3'].map(c3_dictionary)  
     aiCsv['C4*'] = aiCsv['C4'].map(c4_dictionary)
     aiCsv['C5*'] = aiCsv['C5'].map(c5_dictionary)

    
     aiCsv = aiCsv.drop(aiCsv.columns[[0]], axis=1) # delete the unnamed column 
     outputCsvFileName = postAnalysisDirectory + programName + "Config_to_numeric.csv"
     aiCsv.to_csv(outputCsvFileName) 


     for i in range(9, 71): 
           print(aiCsv.columns[[i]])
except Exception as e: 
     print(e)
     print("no file")