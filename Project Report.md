# University of Delaware MATH-219 Data Science Project

#### Data Provided by: Department of Education
#### Dataset Owner: Delaware Open Data
#### Link to Data Set: https://data.delaware.gov/Education/Student-Assessment-Performance/ms6b-mt82/about_data

This file contains the number of tested students, proficient students, and the corresponding proficiency rate for the key annual assessments administered during a given school year. Each row represents the proficiency rate for a specified group of students within a school, its district, or the state as a whole. 

## Introduction

In this report, I wanted to use a large, detailed dataset of Delaware students' performance over the span of 8 years to analyze various aspects of the data. My overall objective was to collect the values of the quantitative fields, view the summary statistics, and determine if there are any correlations between these values and the categories I elected to keep. I reduced the general scope of this report by choosing 2 categories and 5 quantitative fields out of the 18 columns in the original dataset:

* Content Area (categorical)- Statewide summative assessment subject (or content area). Valid values include: CMP – EL Annual ACCESS Composite Score; ELA – English Language Arts/Reading; ESSAY – Essay Component of SAT assessment; MATH – Mathematics; SCI – Science; SOC – Social Studies;
* Grade (categorical)- Represents the grade level of the unique group of students within a school/district (Ex. 1st grade, 2nd grade, etc.)
* School Year (semi-quantitative)- School year for which record is applicable (Ex. 2016 = school year which ended in June 2016)
* Tested (quantitative)- The number of students who completed the statewide summative assessment listed with a valid score
* Proficient (quantitative)- The number of students who earned a proficient achievement level (i.e. a score of 3 or above)
* PctProficient (quantitative)- The percent of students who earned an achievement level considered proficient. This is the number of students who earned a proficient achievement level divided by the number of students who tested
* ScaleScoreAvg (quantitative)- The average scale score for the specified group of students


## Preprocessing

In order to begin my analyses, I had to clean and sort the data, remove columns that I did not intend to work with, and remove outliers to prevent the skewing of results and to allow for clearer graphs. This process resulted in the removal of approximately 1 million out of the initial 1.24 million rows and 11 out of the initial 18 columns. The removal of many categorical columns was for the purpose of staying within the scope of my desired endgoal and to maintain a much larger, more complex analysis.


## Summary data analysis

The first analysis I performed to gain a general understanding of the data was a simple description of the summary statistics for the Tested, Proficient, PctProficient, and ScaleScoreAvg columns. Next, I wanted to look at the total counts and proportions of the unique values in the ContentArea and Grade categories. 

Next is the graphical data, which I chose to examine the histograms of the Tested, Proficient, PctProficient, and ScaleScoreAvg columns to better understand how the values are distributed. These graphs show a count (y-axis) of the total number of samples that lie within various ranges along the x-axis. For example, the histogram of the Tested column displays its largest bar furthest to the left, meaning there are approximately 60,000 samples in which the value of the Tested columns is between approximately 0 and 20. 

The next set of graphs will be barplots that incorporate the School Year column to compare how the Tested, Proficient, PctProficient, and ScaleScoreAvg columns differ from the years 2015 to 2023. 

Now, the ContentArea and Grade categories will be utilized for analysis in boxen plots and correlations. Here, I chose to work with the PctProficient and ScaleScoreAvg columns and group by ContentArea and Grade to create 4 separate boxen plots. This allowed for further insight into the distributions of the PctProficient and ScaleScoreAvg when comparing between the different school subjects and grades. 

Lastly, I intended to find the numerical values of the correlations School Year against PctProficient and ScaleScoreAvg overall, including when they are grouped by ContentArea and Grade for a total of 6 correlations. The overall correlations produced a single value of a Pearson correlation, whereas the correlations that were grouped by ContentArea and Grade produced a unique Pearson correlations value for each subject and grade respectively. This was done to determine how these unique correlations differ and if they were significant.


## Discussion

This dataset leaves open a wide array of questions to be asked and further analyses to be explored that could not be investigated for this particular project. Here are a few questions I pose for potential further analysis or simply reflecting on:

Does school year (time), number of tested students, percent of proficient students, and the scale score average of students' assessments impact the special demographics of students, such as low-income or homeless students?

Can factors such as assessment type, race, gender, school year (time), number of tested students, number of proficient students, and the percent of proficiency influence the scale score average of students' assessments?
