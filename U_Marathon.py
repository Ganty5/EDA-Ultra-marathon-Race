#import libaries I will work with
import pandas as pd

import seaborn as scn

import matplotlib.pyplot as plt



#Load the Ultra Marathon dataset
U_Marathon = pd.read_csv("C:/Users/Chika/Downloads/Python Project/TWO_CENTURIES_OF_UM_RACES.csv")

#To preview some rows of this dataset
U_Marathon.head(10)

#Getting the number of columns and number of records available in the dataset used
U_Marathon.shape

#Displaying the types associated with each of these columns so I know which to amend 
U_Marathon.dtypes

U_Marathon.describe().T

#Data Cleaning 
# In my cleaning process, I will consider criterials I need to specifically work with, owing to the size of the dataset
#I would focus on marathon races within 50km and 50mi, for the country USA in the year 2020

#Using the code below to verify if my dataset contains 50km or 50k in regards to used S.I unit for distance
U_Marathon[U_Marathon['Event distance/length'] == "50km"]

#Checking for 50k (S.I unit), it displayed nothing but headings
U_Marathon[U_Marathon['Event distance/length'] == "50k"]

#checking for 50mi or 50m S.I unit 
U_Marathon[U_Marathon['Event distance/length'] == "50m"]

U_Marathon[U_Marathon['Event distance/length'] == "50mi"]

#I got a result displayed for 50mi unlike 50m. After my individual search for whcih gives me the result I seak for, I would combine 50km and 50mi using isin function.
U_Marathon[U_Marathon['Event distance/length'].isin(['50km','50mi'])]

#Filtering to 2020
U_Marathon[(U_Marathon['Event distance/length'].isin(['50km','50mi'])) & (U_Marathon['Year of event'] == 2020)]

#Filtering to USA 
U_Marathon[U_Marathon['Event name'] == 'Everglades 50 Mile Ultra Run (USA)']

#Splitting to get USA detached from Event name
U_Marathon[U_Marathon['Event name'] == 'Everglades 50 Mile Ultra Run (USA)']['Event name'].str.split('(').str.get(1).str.split(')').str.get(0)
U_Marathon[U_Marathon['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA']

#Combining all filtered results (the result will give us USA events that are in 2020 within 50km and 50mi)
U_Marathon_full = U_Marathon[(U_Marathon['Event distance/length'].isin(['50km','50mi'])) & (U_Marathon['Year of event'] == 2020) & (U_Marathon['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')]
#Preview top 10 rows of U_Marathon_full dataset
U_Marathon_full.head(10)

#Number of records in my datset has reduced to 26090, maintaining still 13 columns
U_Marathon_full.shape

#Remove (USA) from Event name, Splitting by delimiter (
U_Marathon_full['Event name'].str.split('(').str.get(0)

U_Marathon_full['Event name'] = U_Marathon_full['Event name'].str.split('(').str.get(0)

#USA is out 
U_Marathon_full.head(10)

#Clean up the "Athlete Age" column 
U_Marathon_full['athlete_age'] = 2020 - U_Marathon_full['Athlete year of birth']

#Remove h from athlete performance column
U_Marathon_full['Athlete performance'].str.split('(').str.get(0)
U_Marathon_full['Athlete performance'] = U_Marathon_full['Athlete performance'].str.split(' ').str.get(0)

U_Marathon_full.head(5)

#Remove columns not needed (Athlete Club, Athlete Country, Athlete year of birth, athlete age category)
U_Marathon_full = U_Marathon_full.drop(['Athlete club', 'Athlete country', 'Athlete year of birth', 'Athlete age category'], axis = 1)
U_Marathon_full.head(5)

#Clean up null values
U_Marathon_full.isna().sum()

U_Marathon_full[U_Marathon_full['athlete_age'].isna()==1]

#To drop the 233 rows that are null values in athlete_age column
U_Marathon_full = U_Marathon_full.dropna()
U_Marathon_full.shape

#Check for duplicated values
U_Marathon_full[U_Marathon_full.duplicated()== True]

#Reseting index (correcting the indexing/numbering)
U_Marathon_full.reset_index(drop = True)

#Correct data types
U_Marathon_full.dtypes
U_Marathon_full['athlete_age'] = U_Marathon_full['athlete_age'].astype(int)
U_Marathon_full['Athlete average speed'] = U_Marathon_full['Athlete average speed'].astype(float)

U_Marathon_full.dtypes

U_Marathon_full.head(5)

#Edit column names:

#Year of event                  int64
#Event dates                   object
#Event name                    object
#Event distance/length         object
#Event number of finishers      int64
#Athlete performance           object
#Athlete gender                object
#Athlete average speed        float64
#Athlete ID                     int64
#athlete_age                    int32

U_Marathon_full= U_Marathon_full.rename(columns= {'Year of event': 'Year',
                                             'Event dates': 'Race_day',
                                             'Event name': 'Race_Name', 
                                             'Event distance/length': 'Distance',
                                             'Event number of finishers': 'Number_of_finishers', 
                                             'Athlete performance': 'Performances',
                                             'Athlete gender': 'Gender', 
                                             'Athlete average speed': 'Runners_avg_speed', 
                                             'Athlete ID': 'Athlete_ID'
                                            })

U_Marathon_full.head(5)
#To reorder column
U_Mara = U_Mara = U_Marathon_full[['Athlete_ID', 'Race_day', 'Race_Name', 'Distance', 'Number_of_finishers', 'Gender', 'Performances', 'Runners_avg_speed', 'athlete_age']]
U_Mara.head(5)

#Displaying Some results individually based on filtering
U_Mara[U_Mara['Race_Name'] == 'Everglades 50 Mile Ultra Run ']
U_Mara[U_Mara['Gender'] == 'F']
U_Mara[U_Mara['Runners_avg_speed'] > 9]
U_Mara[U_Mara['Athlete_ID'] == 222509]

#Data Visualization
#Displaying the race distance in the year 2020 for races in USA

scn.histplot(U_Mara['Distance'])
plt.title("Race Distance in USA, 2020")
plt.show()
#The result shows more of races with S.I unit of KM, than Mi

#Visuals filtering by gender, the distance of races made by each sex
scn.histplot(U_Mara, x = 'Distance', hue= 'Gender')
plt.title("Distance by sex")
plt.show()

#Displaying a distribution plot that shows Average speed of runners specifically those who covered 50mi distance
# distributions of numeric data using Violin plot
scn.violinplot (data = U_Mara, x='Distance', y = 'Runners_avg_speed', hue = 'Gender', Colors = 'Male: red', 'Female: blue')
plt.title('Violin plot of Race Length')
plt.show()


#Displaying Runners_avg_speed by average age using scattered plots and categorizing it by gender
scn.lmplot(data = U_Mara, x = 'athlete_age', y = 'Runners_avg_speed', hue = 'Gender')
plt.title("Average speed by Age")
plt.show()

#Calculating the difference in the speed for the 50km, 50mi race between both sex 
Dif_U_Mara = U_Mara.groupby(['Distance', 'Gender'])['Runners_avg_speed'].mean()
Dif_U_Mara


#   Research Questions
#What age group are the best in terms of count of races, in the 50 mi races (in their 20's), sorted in descending order
U_Mara.query('Distance == "50mi"').groupby('athlete_age')['Runners_avg_speed'].agg(['mean', 'count']).sort_values('mean', ascending = False).query('count > 19').head(20)

#What age group are the worst in terms of races count, in the 50 mi races (in their 10's), sorted in ascending order
U_Mara.query('Distance == "50mi"').groupby('athlete_age')['Runners_avg_speed'].agg(['mean', 'count']).sort_values('mean', ascending = True).query('count > 9')

#How many events took place in USA in the year 2020
U_Mara['Race_Name'].nunique()

#Number of participants in each kind of race
U_Mara['Race_Name'].value_counts().head(10)

#What is the number of races categorized by gender
Race_gend=pd.crosstab(index=U_Mara['Distance'],columns=U_Mara['Gender'])
Race_gend

#Graphically represent the race distribution by gender
Race_gend.plot(kind='bar',title='Number of race by Gender',ylabel='Count',xlabel='Race Length')
plt.show()

#Calculating for co-relations

U_Mara['Distance'].value_counts()
maping={'50km':1,'50mi':2}
data_cor=U_Mara.copy()
data_cor['Distance']=data_cor['Distance'].map(maping)
maping2={'M':0,'F':1}
data_cor['Gender']=U_Mara['Gender'].map(maping2)

#U_Mara['Distance'].astype('float64')
corelation_table=data_cor[['Distance','Gender','Runners_avg_speed','athlete_age']].corr()
corelation_table

#Plotting the heatmap 
scn.heatmap(corelation_table,annot=True)
plt.title("Corelation Result")
plt.show()

ag=U_Mara.athlete_age.value_counts().head(5)



