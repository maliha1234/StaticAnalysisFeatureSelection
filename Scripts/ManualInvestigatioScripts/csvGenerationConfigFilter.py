import pandas
import sys
import glob
import os


postAnalysisDirectory = sys.argv[1]
programName = sys.argv[2]

try:
     aiCsvFileName = postAnalysisDirectory + programName + ".csv"
     aiCsv = pandas.read_csv(aiCsvFileName)
     print(aiCsvFileName)
     
    
  
     
     filterCsv = aiCsv[(aiCsv["C1"] == "BU") | (aiCsv["C1"] == "TD+BU")| (aiCsv["C2"] == "SO") | (aiCsv["C4"] == "ALLOCATION") | (aiCsv["C5"] == "POLY") ]
     filterCsv = filterCsv.sort_values(by=['time(MS)'], na_position='first')
     filterCsv = filterCsv.drop(filterCsv.columns[[0]], axis=1)

     outputCsvFileName = postAnalysisDirectory + programName + "_Filter_with_config.csv"
     filterCsv.to_csv(outputCsvFileName) 
 

     for i in range(9, 66): 
           print(filterCsv.columns[[i]])

  #   print(filterCsv)
     count_greater = filterCsv["X01"].count()
     print(count_greater)

except Exception as e: 
     print(e)
     print("no file")