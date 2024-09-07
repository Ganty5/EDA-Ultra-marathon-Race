It is generally known that Races longer than the 42.195-kilometer standard marathon distance are called ultra-marathons, this likewise has gone viral, all over the world, drawing competitors who are looking for the most extreme challenges and pushing the
limits of human endurance. This dataset presents an extensive compilation of ultramarathon race records from 1798 to 2022, which spans more than two centuries. This large dataset offers a rare chance to examine the patterns and changes in ultra-marathon
running over time. To gain important insights into a variety of facets related to this endurance sport, I conducted a thorough analysis of the ultra-marathon running dataset in this report. The goal is to investigate variables like racial outcomes, participant 
demographics, race distances, and race locations. Using cutting-edge analytical methods and visualization software, capturing trends, connections, and underlying dynamics in the dataset.

Our analysis offers useful insights for race organizers, sponsors, and sports science researchers in addition to serving athletes and enthusiasts curious about the intricacies of ultra-marathon running. This dataset and report are expected to add to the continuing
conversation about endurance sports while also illuminating the fascinating world of ultra-marathon running. The dataset is made up of over 7 million records and contains 13 columns, namely; Year of event, Event dates, Event name, Event distance/length,
Event number of finishers, Athlete performance, Athlete club, Athlete country, Athlete year of birth, Athlete gender, Athlete age category, Athlete average speed and Athlete ID.


RESEARCH QUESTION
The following outlined below are questions my dataset analysis answers, helping to pinpoint insights and trends and answering different questions that can enhance decision-making processes and problem-solving for future sports activities in this track.
1. What age group is the best in terms of the number of races performed, in the
distance of 50 mi (Taking into consideration people only in their 20s)
2. What age group is the worst in terms of the number of races performed, in the
distance of 50 mi (Taking into consideration people only in their 20s)
3. How many racing events took place in the USA in the year 2020?
4. What is the number of participants in each kind of race (i.e. event name)
5. What is the number of races categorized by gender?
6. Determine the co-relationship between the distances in the race and Gender
7. Determine the difference in the racing speed between both sex
   
METHODOLOGIES
The Ultra-Marathon running dataset used in this analysis was obtained and downloaded from Kaggle, the world’s largest data science community with powerful tools and resources. With the use of the dataset downloaded and analyzed, I was able to perform 
certain analytical tasks and derive meaningful insights that aided my understanding and view of the sporting industry. Understanding the information in the dataset shared is very essential in making accurate decisions. Exploratory Data Analysis (EDA) 
techniques form the basis of the methodology for the codes in the dataset. Find below the methodological approaches:

Data Collection:
Gathered and collected data from Kaggle covering registrations from 1798 to 2022.
Library Installation and importation:
Before I commenced importation of the CSV dataset into my working environment, I installed the needed libraries I would be working with such as pandas, seaborn, and matplotlib.

Data Importation and Synopsis:
I loaded my essential libraries such as Pandas, Seaborn, and Matplotlib. These libraries would enhance my visualization interfaces, analysis, cleaning, exploration, and data manipulation. It would also improve my static creation.
I used the read_csv function to import my data into my IDE (Visual Studio Code). Displayed the number of rows and columns available in my dataset, data type, and statistical summaries of my data like mean, etc.

Data Preprocessing and Cleaning:
➢ Because I have a dataset that has two distances via different S.I unit race measurements, and owing to the large dataset, I needed to determine what exactly the S.I units of measurements were used in the dataset. I ran some checks to determine if it
was specifically in km and mi or k and m or kilo and mil.
➢ Also, I filtered my data to specifically display only races from the year 2020.
➢ Filtered data to the USA only6
➢ I ran a code to split USA from being attached to the event names column.
➢ Finally, I combined all filtered conditions and allocated it to a new string.
➢ After this filtering exercise, the dataset which was over 7 million drastically reduced to 26000 and some fractions. This is best to be worked with. I also cleaned some columns, changed data types to correct ones, removed unnecessary columns,
improved the dataset appearance, cleaned up duplicates and null values, dropped null values, corrected the indexing, and renamed the column.

Exploratory Data Analysis (EDA):
➢ Conducted descriptive statistics to understand the dataset's basic characteristics, such as the distribution of race distances, participant demographics, and geographical locations.
➢ Visualized key variables using bar charts, histograms, Violin plots, scatterplots, and heat maps, to identify patterns and outliers.

Transitioning: Using the available data and information on my dataset, I created new Features such as Athlete Age and race duration such that I can improve my performance and analysis.

Statistical Analysis:
Perform statistical tests to analyze relationships between variables, such as the correlation between race distance, gender, runners' average speed, and age.
Comprehensive Analysis (based on Dataset Content):
➢ Performing particular analyses
➢ Generating deeper insights

Documentation and Reporting
I made a report that details the steps taken, the observations made my conclusions, and further information during the analysis.
