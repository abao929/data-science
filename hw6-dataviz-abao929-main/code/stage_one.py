import pandas as pd
from matplotlib.colors import rgb_to_hsv
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('../data/ri_traffic_stops.csv', delimiter=',')

#Bar Graph of Age vs. Arrested or Not
age_groups = ['15-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89']
arrested_counts = []
not_arrested_counts = []
fig, ax = plt.subplots(figsize =(16, 9))

for age in age_groups:
    low, high = age.split('-')
    data = df.loc[(df['driver_age'] >= int(low)) & (df['driver_age'] <= int(high))]
    counts = data['is_arrested'].value_counts().to_list()
    if len(counts) > 1:
        arrested_counts.append(counts[1])
    else:
        arrested_counts.append(0)
    not_arrested_counts.append(counts[0])

br1 = np.arange(len(arrested_counts))
br2 = [x + .33 for x in br1]
ax.set_title('Number of People Pulled Over by Age', loc ='left')
plt.bar(br1, arrested_counts, color ='r', width = .33, edgecolor ='grey', label ='Arrested')
plt.bar(br2, not_arrested_counts, color ='g', width = .33, edgecolor ='grey', label ='Not Arrested')
plt.xlabel('Age', fontweight ='bold', fontsize = 15)
plt.ylabel('People Pulled Over', fontweight ='bold', fontsize = 15)
plt.xticks([r + .33 for r in range(len(arrested_counts))],  age_groups)
plt.legend()
plt.savefig('../graphs/s1q1.png')

#Bar Graph of Month vs. # of ppl pulled over
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_counts = []
fig, ax = plt.subplots(figsize =(16, 9))

for x in range(1, 13):
    month_counts.append(len(df.loc[df['stop_month'] == x]))

ax.set_title('Number of People Pulled Over by Month', loc ='left')
ax.bar(months, month_counts)
plt.xlabel('Month', fontweight ='bold', fontsize = 15)
plt.ylabel('People Pulled Over', fontweight ='bold', fontsize = 15)
plt.legend()
plt.savefig('../graphs/s1q2.png')

#Pie Chart of Race vs. Arrested
races = df['driver_race'].unique()
races_count = []
races_count2 = []
for race in races:
    races_count.append(len(df.loc[df['driver_race'] == race]))
    races_count2.append(len(df.loc[(df['is_arrested'] == True) & (df['driver_race'] == race)]))
fig, ax = plt.subplots(nrows=1, ncols=2, figsize =(16, 9))
ax[0].pie(races_count, labels=races, autopct='%1.1f%%', startangle=90)
ax[0].set_title('Percentage Breakdown of Traffic Stops by Race', loc ='left')
ax[1].pie(races_count2, labels=races, autopct='%1.1f%%', startangle=90)
ax[1].set_title('Percentage Breakdown of Arrests by Race', loc ='left')
plt.legend(loc='upper right', bbox_to_anchor=(0, 1))
plt.savefig('../graphs/s1q3.png')