import pandas
import sys
import glob
import os


postAnalysisDirectory = sys.argv[1]
programName = sys.argv[2]

try:
    aiCsvFileName = postAnalysisDirectory + programName + "Config_to_numeric.csv"
    aiCsv = pandas.read_csv(aiCsvFileName)

    aiCsv = aiCsv.drop(aiCsv.columns[[0]], axis=1) # delete the unnamed column 

    for i in range(9, 66):
           print(i) 
           print(aiCsv.columns[[i]] + '****')

    for i in range(66, 71):
           print(i) 
           print(aiCsv.columns[[i]])
     
    for i in range(9, 71): 
           colname1 = aiCsv.columns[i]
           for j in range(i+1, 71):
              colname2 = aiCsv.columns[j]
              multipliedcolname = colname1 + '*' + colname2
              aiCsv[multipliedcolname] = aiCsv[colname1]*aiCsv[colname2]
    

    outputCsvFileName = postAnalysisDirectory + programName + "Two_way.csv"
    aiCsv.to_csv(outputCsvFileName) 
    print(len(aiCsv.columns))

except Exception as e: 
     print(e)
     print("no file")