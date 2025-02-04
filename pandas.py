
# create emtpy sereis 
import pandas as pd
print (pd.series())

# create series from array 
data = np.array(['g','g','t','y'])
print(pd.Series(data))

# create sereis from eeat with custome index
data = np.array(['d','r','p'])
ser = pd.Series(data,index=[1,2,3])
print(ser)

# series from list 
list = ['t','i','a']
print(pd.Series(list))

#create list from dict 
dict = {"gee":10,"age":54,"happy":54}
print(pd.Series(dict))

#create series from sclaer vlaue 
ser = pd.Series(10,index=[0,1,2,3])
print(ser)

#create sereis from range function
print(pd.Series(range(5)))

#create sereis with list comprehension
ser = pd.Series(range(1,2,3))
index = [x for x in "dfgfhnb"]
print(ser)

#shallow copy 
# where indices & data are not cpoided
#copy only reference to indices & data
ser.copy(deep=False)

#deep copy
# own indeices & data 
#change made in object will not reflect on orignal series 
ser.copy(deep=True)

# ========================================= #

# creare df from list 
list = ["geeks","for","geks"]
df = pd.DataFrame(list)
print(df)

# from ndarray lsit 
data = {'name':["tom","happy"],"age":[20,43]}
df = pd.DataFrame(data)
print(df)

# from list useing dict 
dict = {"name":['aprana',"jano"],
        "degree":["mba","doctor"],
        "score":[80,53]}

df = pd.DataFrame(dict)
print(df)

#decribe  ereis of df 
df = df["column_name"].describe(
)

# dropping passed columns
data.drop(["Team", "Weight"], axis = 1, inplace = True)
 

## simply concatenate both dataframes
df = pd.concat([new_row, df]).reset_index(drop = True)

# dropping passed values
data.drop(["Avery Bradley", "John Holland", "R.J. Hunter",
                            "R.J. Hunter"], inplace = True)

#apply function to rows
# Function to add
def add_values(row):
    return row['A'] + row['B'] + row['C']
   # Apply the user-defined function to every row
    df['add'] = df.apply(add_values, axis=1)

#Normalizing DataFrame Column Values Using Custom Function in Pandas
def normalize(x, y):
    x_new = ((x - np.mean([x, y])) /
             (max(x, y) - min(x, y)))
  df['X'] = df.apply(lambda row: normalize(row['X'],
                                             row['Y']), axis=1)

# get coulmens name
data = pd.DataFrame({
    'Name': ['Avery Bradley', 'Jae Crowder', 'John Holland'],
    'Team': ['Boston Celtics'] * 3,
    'Number': [0.0, 99.0, 30.0],
})  
# Get column names
column_names = data.columns
print(column_names)

# sorted columns
sorted_columns = sorted(df.columns)
print(sorted_columns)

#How to rename columns in Pandas DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
df.rename(columns={'A': 'X', 'B': 'Y', 'C': 'Z'}, inplace=True)
print(df)

#rename column using set axis
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df = df.set_axis(['Alpha', 'Beta'], axis=1)
df

#Drop Columns Using df.iloc[] for Index-Based Ranges
df = data.drop(data.iloc[:, 1:3], axis=1)
print(df)

# Drop columns from 'B' to 'C'
df = data.drop(columns=data.loc[:, 'B':'C'].columns)
print(df)

#drop based on condition
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, None, None, 4],
    'C': [1, 2, 3, 4]
})
threshold = len(df) * 0.5
df = df.dropna(thresh=threshold, axis=1)
print(df)

#Convert a column to row name/index in Pandas
df = pd.DataFrame(data)
# pivoting the dataframe
df.pivot(index ='Result', columns ='name')
 

# get smallest vlaue in column
df.nsmallest(10, ['Weight'])

#for largest
# five largest values in column age 
df.nlargest(5, ['Age'])

#select loc 
Dataframe.loc[["row1", "row2"], ["column1", "column2", "column3"]]

# Select all rows and specific columns
first = data.loc[:, ["Team", "Number", "Position"]]
print(first)

# Select multiple rows by position
row2 = data.iloc[[3, 5, 7]]
display(row2)

# Select all rows and specific columns
row2 = data.iloc[:, [1, 2]]
print(row2)

# removing null values to avoid errors  
data.dropna(inplace = True)  
  
  
# converting to string data type 
data["Salary"]= data["Salary"].astype(str) 

   

# slicing till 2nd last element 
start, stop, step = 0, -2, 1
data["Salary (int)"]= data["Salary"].str.slice(start, stop, step) 

# =============================================== #

#operations on pandas

# apply
s = pd.read_csv("stock.csv", squeeze = True)
def fun(num):

    if num<200:
        return "Low"

    elif num>= 200 and num<400:
        return "Normal"

    else:
        return "High"

new = s.apply(fun)
print(new.head(3))

# apply to evry row & column

def add_values(row):
    return row['A'] + row['B'] + row['C']
    df['add'] = df.apply(add_values, axis=1)

# apply wit hlambda
def add(a, b, c):
    return a + b + c

 df['add'] = df.apply(lambda row: add(row['A'],
                                         row['B'], row['C']), axis=1)


#aggregate 
# We are going to find aggregation for these columns 
df.aggregate({"Number":['sum', 'min'], 
              "Age":['max', 'min'], 
              "Weight":['min', 'sum'],  
              "Salary":['sum']}) 


#mean
# skip the Na values while finding the mean
df.mean(axis = 1, skipna = True)

#vlaue conuts
# find the value counts 
sr.value_counts() 

# Calculate the standard error of  
# the mean of all the rows in dataframe 
df.sem(axis = 1, skipna = False) 

# To find the mean absolute deviation
# skip the Na values when finding the mad value
df.mad(axis = 1, skipna = True)

# using .merge() function
res = pd.merge(df, df1, on='key')

# using keys from right frame
res1 = pd.merge(df, df1, how='right', on=['key', 'key1'])
 
# getting union  of keys
res2 = pd.merge(df, df1, how='outer', on=['key', 'key1'])
 
# getting intersection of keys
res3 = pd.merge(df, df1, how='inner', on=['key', 'key1'])
 
# getting union
res1 = df.join(df1, how='outer')

# using on argument in join
res2 = df.join(df1, on='Key')

# to append df2 at the end of df1 dataframe df2
print(df1.append(df2))

# for appending df2 at the end of df1
df1 = df1.append(df2, ignore_index = True)

# add new row at top

new_row = pd.DataFrame({'Name':'Geeks', 'Team':'Boston', 'Number':3,
                        'Position':'PG', 'Age':33, 'Height':'6-2',
                        'Weight':189, 'College':'MIT', 'Salary':99999},
                                                            index =[0])
# simply concatenate both dataframes
df = pd.concat([new_row, df]).reset_index(drop = True)


# dropping null value columns to avoid errors 
data.dropna(inplace = True) 
    
# splitting string and overwriting  
data["Team"]= data["Team"].str.split("t") 
  
# joining with "_" 
data["Team"]= data["Team"].str.join("_") 

#2 text column in 1 column
df['Name']= df["First"].astype(str) +" "+ df["Last"]

# ======================== on text data ========================

# converting and overwriting values in column 
df["Name"]= df["Name"].str.lower()

# converting and overwriting values in column 
data["Team"]= data["Team"].str.upper() 


#replace string
df['text'] = df['text'].str.replace(' ', '_')

# overwriting column with replaced value of age
data["Team"]= data["Team"].str.replace("boston", "New Boston", case = False)

# replace the old ones in the list with  the new values
result = sr.replace(to_replace = ['New York', 'Rio'], value = ['London', 'Brisbane'])

# ========================== csv ===============================#

# saving the dataframe
df.to_csv('file2.csv', header=False, index=False)
df.to_csv('Users.csv', sep='\t', index=False,header=True)
new_df = pd.read_csv('Users.csv')

#with excel
require_cols = [0, 3]  
required_df = pd.read_excel('SampleWork2.xlsx', usecols = require_cols) 

#visulaziation 
# plotting points as a scatter plot 
x = df["Observation Value"] 
y = df["Time period"] 
plt.scatter(x, y, label= "stars", color= "m",  
            marker= "*", s=30) 

# filling value of one column 
dframe['For'].fillna(value = dframe['For'].mean(), 
                                    inplace = True) 

# Apply groupby and aggregate function  max to find max value of column  
print(dframe.groupby(['eks']).max())


# Simplest pivot table
table = pd.pivot_table(df, index =['A', 'B']) 

# Creates a pivot table dataframe 
table = pd.pivot_table(df, values ='A', index =['B', 'C'], columns =['B'], aggfunc = np.sum) 

# Filter groups where the average Salary is >= 5 million
filtered_df = df.groupby('Team').filter(lambda x: x['Salary'].mean() >= 1000000)
print(filtered_df)
  
  aggregated_data = df.groupby(['Team', 'Position']).agg(
    total_salary=('Salary', 'sum'),
    avg_salary=('Salary', 'mean'),
    player_count=('Name', 'count')
)


# skip the Na values while finding the mean
df.mean(axis = 1, skipna = True)