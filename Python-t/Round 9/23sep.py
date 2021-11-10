import pandas as pd


data = pd.read_csv('StudentsPerformance.csv')

## DataFrame
#m * n matrix capable of handling mixed data types

# print(data.head())
# print(data.tail())


## High level overview
# data.info()

## Mathematical overview
# print(data.describe())





##########
# min, max, sum, count, std, mean
#print(list(data.columns))

# print(dataframe[column])
# print(dataframe[[col1, col2, col3]])


#print(data['math score'].sum())

# Does writing have a higher mean score than reading?

#print(abs(data['writing score'].mean() - data['reading score'].mean()))

#print(data[['gender', 'lunch']])

##############

#### Accessing Rows:

# iloc: accessing by 'where' they are
# loc: accessing by 'what' the data is


#print(data.iloc[rows, columns])

# print(data.iloc[500])
# print(data.iloc[:10])
# print(data.iloc[55:75])

# print(data.iloc[65:80, :3])

### last 10 rows, first 2 columns
#print(data.iloc[-10:,:2])

# Middle row, columns 1 onwards
#print(data.iloc[len(data) // 2, 1:])


#print(data.iloc[[5,6,100], [0,2,5]])


# for i in range(50):
#   print(data.iloc[i, 0])



##### Iterate through the the gender column, and count the number
# of males, females in a dictionary??

gender = dict.fromkeys(['male', 'female'], 0) 



for i in range(len(data)):
  if data.iloc[i, 0] == 'male': 
    gender['male'] += 1 
  else: 
    gender['female'] += 1 

#print(gender)


#print(data['col'].method())

# .value_counts()
# .unique()
# .nunique()

# print(data['gender'].value_counts())
# print(data['gender'].unique())
# print(data['gender'].nunique())


#################################

### loc
## 'Return the entire row, when the following rule applies'

#### df.loc[Condition & Condition]


top_maths = data.loc[data['math score'] > 90]
#print(top_maths.describe())


top_math_boys = data.loc[(data['math score'] > 90) & (data['gender'] == 'male')]
#print(top_math_boys)


### Take the average reading score first
# .mean()


## Find all below average readers, who have a free lunch

average_readers = data['reading score'].mean()
# print(average_readers)

below_average_readers = data.loc[(data['reading score'] > average_readers) & (data['lunch'] == 'free/reduced')]

#print(below_average_readers)

# above_average_readers = data.loc[~(data['reading score'] > average_readers) & (data['lunch'] == 'free/reduced')]
# print(above_average_readers)


#df['new'] = (df['colx'] + df['coly']) / 2

## Literacy Column: (Reading + Writing) / 2

data['literacy'] = data['reading score'] + data['writing score'] / 2

#print(data.head())


new_data = data.drop(columns=['lunch',
                              'race/ethnicity',
                              'parental level of education',
                              'test preparation course'])


def grader(value):
  if value >= 80:
    return 'A'
  elif value >= 60 and value < 80:
    return 'B'
  else:
    return 'C'

new_data['math_grade'] = new_data['math score'].apply(grader)

#print(new_data)
new_data.to_csv('CleanedScores.csv', index=False)

##### Kaggle -> Tons of datasets!!
### Seaborn!