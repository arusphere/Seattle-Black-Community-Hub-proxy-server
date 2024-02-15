import pandas as pd

# Define the data types for specific columns


# Load the CSV file with specified data types
data1 = pd.read_csv('data/Black_owned_restaurants.csv')
data2 = pd.read_csv('data/Black owned stores.csv') # all strings 
data3 = pd.read_csv('data/Black owned services .csv') # all strings besides lat long 
data4 = pd.read_csv('data/Black historical cites.csv')#all strings 

# Check the data types again
print(data1.dtypes)
print(data2.dtypes)
print(data3.dtypes)
print(data4.dtypes)
