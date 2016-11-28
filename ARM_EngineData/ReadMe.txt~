Notes:

1. The give data is - Predictive Maintenance for Aircraft Engines
2. Task - To Apply Association Rule Mining optimized using genetic Algorithm
3. PM_Train.csv - The data is about 100 engines and for each engine data has been recorded for each cycle till the machine fails.
4. We first extract the points where the engine failed. Hence we have 100 datapoints in our "scrapedData.csv" file that were extracted using the code "scrape.py"
5A. In the scraped data we have 25 classes, but out of these, values for 8 classes throughout the datapoint does not change. Hence we remove these classes.
5B. For the remaining 17 classes, all the given data points are numerical and we need to convert them into categorical. Here, for each class we found the max and min point and catagorized the data in one of the 8 catagories. The nomenclature of these catagories is "catagory+class_name" example, "5RUL" means the data has been put into 5th catagory out of the 8 created for the Cycle_of_Fracture class.
5C. The above has been done using the script "categorize.py" using "scrape.csv" and the resultant catagories has been put in "catagorizedData.csv" and the useful classes in "ARMData.csv". This "ARMData.csv" serves as the raw data where we apply our main Apriori+GA algorithm.

6. "aprioriGA.py" - 
-- We encoded the categories in 8-bit format for each class
-- We found the items + transactions and their support values initially
-- We generated a population of 100, each in the form (cycle, setting1, setting2, setting3, s1, s2, ... s21) [14 classes total]
-- For each person in this population, we selected a few classes and divided them into two parts - antecedent and consequent 
-- For a selected fitness function, we found fitness of each individual in this populated and segragated the individuals with less fitness
-- Then we used this population to generate another generation where we repeated the whole process. 
-- The best rules accumulated over numerous generations are presented



Typical output for population size 100 and number of generations 50- 
Rule [space] Confidence [space] Lift

['5s2', '5s7', '2s8', '4s9', '3s11'] ['3s17'] 1.0 100.0
***********************************************************************************
['4setting1'] ['3s2', '4s8', '1s9', '5s11', '1s14', '4s17'] 0.0344827586207 3.44827586207
***********************************************************************************
['4setting2', '4s3'] ['4s8', '1s9', '5s11', '6s12', '1s14', '6s20'] 1.0 100.0
***********************************************************************************
['3setting1', '3setting2', '8s2'] ['6s7'] 1.0 12.5
***********************************************************************************
['3RUL', '4setting2', '4s3'] ['4s13', '4s17'] 1.0 11.1111111111
***********************************************************************************
['3RUL', '3s2'] ['3s4', '4s8', '1s14', '2s21'] 0.142857142857 7.14285714286
***********************************************************************************
['4s3', '3s4', '4s8', '6s12'] ['4s13'] 1.0 4.54545454545
***********************************************************************************
['3s2', '4s7', '4s13'] ['3s15', '4s17', '2s21'] 0.5 50.0
***********************************************************************************
['8setting2', '4s4'] ['3s17', '5s21'] 1.0 100.0
***********************************************************************************
['4s7', '5s11'] ['6s20'] 0.2 1.42857142857
***********************************************************************************
['3RUL', '4s3', '3s4'] ['4s8', '6s12', '3s15'] 0.333333333333 33.3333333333
***********************************************************************************
['4s4', '5s7'] ['5s12', '4s14'] 0.25 12.5
***********************************************************************************
['3setting2', '5s4'] ['7s9'] 0.2 4.0
***********************************************************************************
['4s2', '6s11'] ['2s20'] 0.25 1.66666666667
***********************************************************************************
['4setting1', '4s8', '1s9'] ['5s11', '6s12', '3s15', '4s17'] 0.125 12.5
***********************************************************************************
['6RUL', '4s4', '3s11', '4s14'] ['3s17'] 1.0 100.0
***********************************************************************************
['6RUL', '4s4'] ['4s9', '3s11', '6s13'] 0.333333333333 33.3333333333
***********************************************************************************
['3s4', '4s8', '1s9'] ['2s21'] 0.333333333333 3.33333333333
***********************************************************************************
['8setting2', '5s7', '4s9'] ['3s17', '5s21'] 1.0 100.0
***********************************************************************************
['6RUL', '8setting2'] ['4s9', '3s17'] 1.0 100.0
***********************************************************************************
['3RUL'] ['4s3', '6s20'] 0.0526315789474 1.75438596491
***********************************************************************************
['2RUL', '1s8', '2s15'] ['6s17', '4s20'] 1.0 100.0
***********************************************************************************
['6s7', '1s8'] ['7s9', '7s14', '2s15'] 0.333333333333 33.3333333333
***********************************************************************************

