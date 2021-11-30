# Statistics Write Up

## Part 1: Regression

All questions in this section pertain to the `bike-sharing.csv` dataset.

#### 1. (5 points)
**Question**:
Interpret the co-efficient for `weathersit` according to simple linear regression. Using plain English, what does this coefficient mean? (one or two sentences should be sufficient)

**Answer**:
Coefficient for 'weathersit' was -621 means that the count decreases by 621 for every unit the 'weathersit' increases.

#### 2. (9 points)
**Question**:
Compare the co-efficient on `weathersit` in a simple regression model (only one independent variable) and the coefficient in the multiple regression model that includes all variables.
- Did the coefficient go up or down?
- Why do you think this is the case?
 
**Answer**:
The coeffient weight went up (down in the sense that the number is less than the previous one) to -1083.
This makes sense because since 'weathersit' is the only value that matters now, every change to count is solely the result of 'weathersit' rather than other variables

#### 3. (9 points)
**Question**:
Which variable would you say is the "most important" for predicting bike usage? Defend your choice.

**Answer**:
I think that season might be the most important for predicting bike usage because its P value is 0 which means that there is strong correlation between that and count

#### 4. (9 ponts)
**Question**:
- In plain English, what is R-squared value?
- What does the R-squared value imply about multiple linear regression models when compared to simple linear regression models?
- Does higher R-squared value always mean that a model is better? Why? How should you best utilize R-squared to examine the goodness of fit for your linear model?

**Answer**:
R squared is a measure of of how much the variance can be predicted by the regression. High R squared means that the variance of data from the fitted line is minimal. Whereas high R squared is bad and there's a lot of variance in the data.
R squared for multiple linear models will be higher than for simple linear regression models because the added variables means that more variance of the dependent variable can be explained by the other variables.
R squared does not always mean that a model is better as overfitting can lead to high R squared value. Additionally, high R squared does not mean that much when doing linear regression with many variables.

#### 5. (8 points)
**Question**:
Is there a difference between training and testing MSE? Why is comparing this important?

**Answer**:
There is a difference between training and testing MSE. Your model tries to minimize training MSE and therefore it should be the lower of the two. You want to compare the test MSE to the training MSE because the training MSE acts like a baseline measurement. 

## Part 2: Statistical Tests

All questions in this section pertain to the `college-data.csv` dataset. For each of the scenarios below, you are expected to answer the following questions:
- What is your null hypothesis? What is your alternative hypothesis?
- What test do we use to answer this question? Why?
- Can we reject the null hypothesis? Why? Be sure to mention the numbers that are part of your reasoning.

We will use the significance level α = 0.05 for all the scenarios.

**Note**: We acknowledge that the binary framework of gender in this dataset does not remotely represent all the possible gender identities that people may have.

### Scenario One (12 points)
In our sample data, students reported their typical time to run a mile, and whether or not they were an athlete. We want to know whether the average time to run a mile is different for athletes versus non-athletes.

**Answer**:
Null hypothesis: Mean mile time of athletes is the same as mean of non-athletes
Alternative hypothesis: Mean mile time of athletes is probably lower than mean of non-athletes
Test: Used a two sample t-test because there are two means that we are trying to compare. Not paired since potentially different amount of athletes and non-athletes
Analysis: The p-value < 0.05 therefore we can reject the null hypothesis. Since the tstat is -13, we can conclude that the athlete times are lower than non-athlete times

### Scenario Two (12 points)
The mean height of U.S. adults ages 20 and older is about 66.5 inches (69.3 inches for males, 63.8 inches for females). In our sample data, we have a sample of 435 college students from a single college. We want to determine whether the mean height of students at this college is significantly different than the mean height of U.S. adults ages 20 and older.

**Answer**:
Null hypothesis: Mean height of college students is the same as mean adult height
Alternative hypothesis: Mean college student height is higher than than mean adult height
Test: Used a one sample t-test because we are just comparing one sample to a known median value
Analysis: The p-value < 0.05 therefore we can reject the null hypothesis. The tstat is 5.8 so we can conclude that the mean college studnent height is higher than mean adult height

### Scenario Three (12 points)
In the sample data, the students also reported their class quartile (1,2,3,4 for the first, second, third and fourth quartile), as well as whether they live on campus. We want to test if there is a relationship between one's class quartile and whether they live on campus.

Note: Their class quartile is denoted in the dataset as "Rank".

**Answer**:
Null hypothesis: No relationship between on or off campus for ranks
Alternative hypothesis: On campus has higher ranks than off campus
Test: Used a chi-squared test because we are comparing relationship of two independent vars
Analysis: The p-value < 0.05 therefore we can reject the null hypothesis. The tstat is 148 which means that there is very a lot of correlation between living on or off campus and quartile results

### Scenario Four (12 points)
The students in the sample completed all 4 placement tests for four subject areas - English, Reading, Math, and Writing - when they enrolled in the university. The scores are out of 100 points, and are present in the dataset. We want to test if there was a significant difference between the average of the English test scores and that of the Math test scores.

**Answer**:
Null hypothesis: No difference between English and Math test scores
Alternative hypothesis: English scores are lower than Math scores
Test: Used a paired t-test because all students have values for both and you are trying to compare them.
Analysis: The p-value < 0.05 therefore we can reject the null hypothesis. The tstat is 36 so English scores higher than Math

### Scenario Five (12 points)
In the sample dataset, respondents were asked their gender and whether or not they were a cigarette smoker. There were three answer choices: Nonsmoker, Past smoker, and Current smoker. We want to test the relationship between smoking behavior (nonsmoker, current smoker, or past smoker) and gender (male or female).

**Answer**:
Null hypothesis: No correlation between gender and smoking
Alternative hypothesis: Correlation between gender and smoking
Test: Used chi-squared because comparing the relationship between two vars
Analysis: The p-value > 0.05 meaning we can not reject the null hypothesis, therefore there is probably no correlation between gender and smoking.



## Part 3: Socially Responsible Computing

#### 1. (5 points)
**Question**
Explain how Simpson's Paradox occurs in the context of the exercise vs. disease example. Why should we choose to separate the data into 2 groups for this specific dataset/question?

**Answer**
Simpson's Paradox occurs in that context because for one analysis, you do not separate the data into bins, whereas for another you do separate it. By separating the data into groups, you are able to hold other variables like age constant so that they do not have as much impact on the analysis so that you can just focus on the effectsof exercise.

#### 2. (7 points)
a.
**Question**
In a few sentences, present and justify statistical results supporting the claim that “Democrats are bad for the economy.”

**Answer**
Through looking at democratic governors and their effects on employment, and inflation, we observe that with an increase of democratic governors, the overall economy does worse. The regression has a negative slope and the p value is 0.01, meaning we can reject the null hypothesis and show that democrats are bad for the economy.

b.
**Question**
In a few sentences, present and justify statistical results supporting the claim that “Republicans are bad for the economy.”

**Answer**
Through looking at republican representatives and their effect on GDP, we observe that an increase of republican representatives, the GDP decreases. We can accept this alternative hypothesis and reject the null hypothesis as the p value is 0.01, which is below the 0.05 threshold. 

c.
**Question**
Write a short reflection about your above experiments with different variable combinations and political claims. Whether specific to the data or broadly applicable to statistical analysis of all kinds, what should you avoid or emphasize if you present or publish the results of such an analysis?

**Answer**
Just clicking through the different combinations made me realize how drastically the regression can change. I felt like I could create any narrative through selecting the correct variables. This expereience has made me far more skeptical of statistics I hear now, since not having full context can definitely paint the wrong picture. In the future, I should try and emphasize exactly what I am analyzing and try and reduce the number of variables as much as possible so that the effects of underlying bias can be reduced.



#### 3. (6 points)
a. 
**Question**
What factors might be influencing the `bike-sharing.csv` data that are not being shown in the dataset? List at least 3 possible factors. The factors could be additional variables or factors that are not quantifiable.

**Answer**
Some variables that might be influencing the bike sharing data might be the introduction of other forms of transportation like an added bus route. Antoher could be the number of shared bikes that are put out by the government. Lastly, could be affected by the employment rate as higher employment could mean more people need to commute to work.

b.
**Question**
List one category for which it could be helpful to separate the `bike-sharing.csv` data into groups before analyzing it. This category may or may not be represented in the existing dataset. Describe a context (project, question, goals, etc.) for which separating the data by that category is important and explain why separating the data is the right choice for that context.

**Answer**
Could be helpful to separate the bike sharing data by season, since there exists a strong correlation between the two that might hinder our ability to view the effects of other variables. If we wanted to see how to best allocate bikes on the weekdays, removing the seasonal effect would be important so that we can more clearly see how day of the week affects how much people use the bikes.

c.
**Question**
Explain at least one way that information in the bikeshare reading impacts how you should interpret `bike-sharing.csv` or present your findings.

**Answer**
When doing the regression with all the independent variables, there were numerous that had a P of 0.000 which seemed to indicate high correlation. However, when eliminating them one at a time, it painted a clearer picture of what mattered in terms of bike sharing. Additionally, when presenting findings, it seemed best to remove the variables that had bad correlation so that their overall impact was not carried by another variable.


#### 3. (2 points)

Please fill out this form! [SRC Mid-Semester Feedback Form](https://docs.google.com/forms/d/e/1FAIpQLSempkWgECNhzIHYYiNnCV20eQUU0eZtR6cz7BKiYLr8buIr4w/viewform?usp=sf_link)

890752