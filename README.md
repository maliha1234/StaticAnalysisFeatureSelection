# Program Characteristics Selection
## Data Files  :
For the CSV files go to the [link](https://utdallas.box.com/s/vw5qa9b46adagfl4em9l5vdyuow9vvcl) and download the programs 


##



## Manual Investigation

1. Run below script to filter the slower optioned rows
```python 
python csvGenerationConfigFilter.py CSV_FILE_DIRECTORY PROGRAM_NAME
```



2. Find 10 most timed rows and out of that find those columns which has atleast half rows>= median

```python 
python csvGenerationFindMedian.py CSV_FILE_DIRECTORY PROGRAM_NAME
```
3. For each exceptional feature run 2nd level filter
```python 
python csvGeneration2ndLevel.py CSV_FILE_DIRECTORY PROGRAM_NAME FEATURE_NAME 
```

##


## Statistical Analysis


1. Run the script to map Configuration to Numeric value

```python 
python csvGenerationConfigToNumeric.py CSV_FILE_DIRECTORY PROGRAM_NAME
```

2. Generate a combination of Program Characteristics and Design Choice 

```python 
python csvGenerationConfigFeatureCombination.py CSV_FILE_DIRECTORY PROGRAM_NAME
```



For the statistical table, generation run the following code on [Matlab](https://www.mathworks.com/products/matlab.html)
```python 
 nohup matlab -nodisplay -nosplash < gradiant_decent.m > output.txt 2> error.txt & 
```


For statistical graph generation run the [R](https://www.r-project.org/) script

```python
>Rscript graphGeneration.R foldername programname featurenumber axisabel
```
