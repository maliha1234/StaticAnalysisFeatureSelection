import pandas
import sys
import glob
import os


postAnalysisDirectory = sys.argv[1]
programName = sys.argv[2]
featureName = sys.argv[3]

try:
     aiCsvFileName = postAnalysisDirectory + programName + ".csv"
     aiCsv = pandas.read_csv(aiCsvFileName)
     print(aiCsvFileName)
    # print(aiCsv.columns[1])
     aiCsv = aiCsv[(aiCsv["C1"] == "BU") | (aiCsv["C1"] == "TD+BU")| (aiCsv["C2"] == "SO") | (aiCsv["C4"] == "ALLOCATION") | (aiCsv["C5"] == "POLY") ]
     aiCsv = aiCsv.sort_values(by=[featureName], na_position='first')
     aiCsv = aiCsv.drop_duplicates(subset= aiCsv.columns[[1]], keep="last")
     aiCsv = aiCsv.nlargest(50,featureName)
     aiCsv = aiCsv.drop(aiCsv.columns[[0]], axis=1)
 #    print(counter)
     outputCsvFileName = postAnalysisDirectory + programName + featureName + "Filter.csv"
     aiCsv.to_csv(outputCsvFileName) 

except Exception as e: 
     print(e)
     print("no file")


