import pandas
import sys
import glob
import os


postAnalysisDirectory = sys.argv[1]
programName = sys.argv[2]

try:
     aiCsvFileName = postAnalysisDirectory + programName + "_Filter_with_config.csv"
     aiCsv = pandas.read_csv(aiCsvFileName)
     print(aiCsvFileName)
     
     filterCsv = aiCsv #save the whole csv to find the median
     aiCsv = aiCsv.nlargest(10,"time(MS)")
     aiCsv = aiCsv.drop(aiCsv.columns[[0]], axis=1) # delete the unnamed column 
    # print(aiCsv)
     
     for i in range(9, 66): 
           print(aiCsv.columns[[i]])

     #from X01 to X67, it has an extra column which need to delete then it will be 9 to 67#
     for i in range(9, 66): 
           colname = aiCsv.columns[i]
           print(colname)
           median = filterCsv[colname].median()
           newCsv = aiCsv[aiCsv[colname] > median] #select those rows out of 10 which are > median
           count_greater = newCsv["X01"].count()
           if count_greater >= 5 :  # select the column if it has more that 5 rows out of 10 rows
              print(str(colname) + " : " + str(count_greater))
           
except Exception as e: 
     print(e)
     print("no file")