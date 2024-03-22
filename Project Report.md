# MATH-219 Data Science Project

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

The first analysis I performed to gain a general understanding of the data was a simple description of the summary statistics for the Tested, Proficient, PctProficient, and ScaleScoreAvg columns. 


## Preprocessing



## Summary data analysis



## Discussion
### Pose two questions about this dataset that you could explore in future projects. One question should be about the prediction of a categorical outcome. For example:

Do the occurrence rates of these 50 words predict whether an email is marked as spam?
Do diagnosis, age, zip code, income, race, and gender predict whether cancer treatment is successful, as measured by 5-year survival rate?
Do family size, income, postal code, GPA, and parents' education levels and occupations predict whether someone goes to college?





### The other question should be about the prediction of a quantitative outcome, such as:

Can last year's team points scored, points allowed, and record, combined with this year's player retention and injury data, predict this year's record?
Do a movie's length, genre, and release date, along with the popularity of its director and stars, predict its box office take?  

### Note that these questions are not necessarily about cause and effect, simply about whether knowing some information allows you to deduce other information.

## Some considerations:

Your questions should be plausible and not propose nonsensical or impossible correlations.
The proposed  predictions should be based on at least 4 quantitative features (i. e., dataset columns).
Stay away from questions based on progression over time, such as stock prices. These often require different methods than the ones we will study. However, a before/after question might work, e. g., effects of the COVID-19 pandemic.
Good questions are often about using mundane or readily available information to deduce something that is interesting and not obvious. But even a common-sense proposal could be worthwhile if it means quantifying an effect that "everybody knows."
