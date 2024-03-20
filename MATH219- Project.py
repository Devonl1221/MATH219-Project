import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
#import numpy as np


## Preprocessing

url = 'https://www.dropbox.com/scl/fi/megbhgphwhpe6ke3b4xy5/Student_Assessment_Performance_20240311.csv?rlkey=n40grd4fw04j9d5585p3x84zu&dl=1'

# Read the CSV file into a pandas DataFrame
raw_data = pd.read_csv(url)

# Clean the data by dropping rows with missing values
df = raw_data.dropna()

# Remove unnecessary columns from the data and fix column types as needed
columns_to_remove = ["District Code", "District", "School Code", "Organization", "Assessment Name", 
                     "Race", "Gender", "SpecialDemo", "Geography", "SubGroup", "RowStatus"]
df = df.drop(columns = columns_to_remove)
df["School Year"] = pd.to_numeric(df["School Year"], errors = "coerce")

# Detect outliers in the columns involving testing scores using z-scores
columns_to_test = ["Proficient", "PctProficient", "ScaleScoreAvg"]

for column in columns_to_test:
    z_scores = stats.zscore(df[column])
    outliers = (z_scores > 3) | (z_scores < -3)


## Summary Data Analysis

# Numerical summary statistics for quantitative columns involving testing scores
tested_summary = df["Tested"].describe()
proficient_summary = df["Proficient"].describe()
pct_proficient_summary = df["PctProficient"].describe()
scale_score_avg_summary = df["ScaleScoreAvg"].describe()

# Count and percentages of unique values for qualitiative columns: Content Area and Grade
# (may not need)
content_area_counts, content_area_percentages = df["ContentArea"].value_counts(), df["ContentArea"].value_counts(normalize = True)
grade_counts, grade_percentages = df["Grade"].value_counts(), df["Grade"].value_counts(normalize = True)


## Histograms for the quantitative columns

# Histograms of Tested, Proficient, Percent Proficient, and Scale Scores Avg
fig, ax = plt.subplots()
tested_histogram = sns.histplot(data = df, x = "Tested", binwidth = 20, kde = False, ax = ax)
ax.set_xlim(0,1000)
#plt.show()

fig, ax = plt.subplots()
proficient_histogram = sns.histplot(data = df, x = "Proficient", binwidth = 20, kde = False, ax = ax)
ax.set_xlim(0,1000)
#plt.show()
# can see that proficiency histogram is skewed even more to the right than tested

fig, ax = plt.subplots()
pct_proficient_histogram = sns.histplot(data = df, x = "PctProficient", binwidth = 5, kde = False, ax = ax)
ax.set_xlim(0,100)
#plt.show()
# has small right skew, meaning there are a larger proportion of schools with lower proficiency rates

fig, ax = plt.subplots()
scale_score_avg_histogram = sns.histplot(data = df, x = "ScaleScoreAvg", binwidth = 100, kde = False, ax = ax)
ax.set_xlim(0,2800)
#plt.show()
# scale score avg is bimodal, meaning a large proportion of schools have either low (around 500) or (around 2500) high scale scores



# School Year against Tested, Proficient, Percent Proficient, and Scale Score Avg
tested_school_year_histogram = sns.histplot(data = df, x = "School Year", y = "Tested")
proficient_school_year_histogram = sns.histplot(data = df, x = "School Year", y = "Proficient")
pct_proficient_school_year_histogram = sns.histplot(data = df, x = "School Year", y = "PctProficient")
scale_score_avg_school_year_histogram = sns.histplot(data = df, x = "School Year", y = "ScaleScoreAvg")

# Content Area against Tested, Proficient, Percent Proficient, and Scale Score Avg
tested_content_area_histogram = sns.histplot(data = df, x = "ContentArea", y = "Tested")
proficient_content_area_histogram = sns.histplot(data = df, x = "ContentArea", y = "Proficient")
pct_proficient_content_area_histogram = sns.histplot(data = df, x = "ContentArea", y = "PctProficient")
scale_score_avg_content_area_histogram = sns.histplot(data = df, x = "ContentArea", y = "ScaleScoreAvg")

# Grade against Tested, Proficient, Percent Proficient, and Scale Score Avg
tested_grade_histogram = sns.histplot(data = df, x = "Grade", y = "Tested")
proficient_grade_histogram = sns.histplot(data = df, x = "Grade", y = "Proficient")
pct_proficient_grade_histogram = sns.histplot(data = df, x = "Grade", y = "PctProficient")
scale_score_avg_grade_histogram = sns.histplot(data = df, x = "Grade", y = "ScaleScoreAvg")











## Violin plots for quantitative columns against categories
# (adjust paramters to make the plots more readable)

# Assessment Name category against quantitative columns
assessment_name_tested_violin = sns.catplot(data = df, x = "Assessment Name", y = "Tested", kind = "violin")
assessment_name_proficient_violin = sns.catplot(data = df, x = "Assessment Name", y = "Proficient", kind = "violin")
assessment_name_pct_proficient_violin = sns.catplot(data = df, x = "Assessment Name", y = "PctProficient", kind = "violin")
assessment_name_scale_score_avg_violin = sns.catplot(data = df, x = "Assessment Name", y = "ScaleScoreAvg", kind = "violin")

# Content Area category against quantitative columns
content_area_tested_grade_violin = sns.catplot(data = df, x = "ContentArea", y = "Tested", kind = "violin")
content_area_proficient_violin = sns.catplot(data = df, x = "ContentArea", y = "Proficient", kind = "violin")
content_area_pct_proficient_violin = sns.catplot(data = df, x = "ContentArea", y = "PctProficient", kind = "violin")
content_area_scale_score_avg_violin = sns.catplot(data = df, x = "ContentArea", y = "ScaleScoreAvg", kind = "violin")

# Grade category against quantitative columns
grade_tested_violin = sns.catplot(data = df, x = "Grade", y = "Tested", kind = "violin")
grade_proficient_violin = sns.catplot(data = df, x = "Grade", y = "Proficient", kind = "violin")
grade_pct_proficient_violin = sns.catplot(data = df, x = "Grade", y = "PctProficient", kind = "violin")
grade_scale_score_avg_violin = sns.catplot(data = df, x = "Grade", y = "ScaleScoreAvg", kind = "violin")


## Correlations

# corr 1


# corr 2


# ...

