# Introduction to Pandas and Financial Data Handling
# Hello and welcome! In today's lesson, you'll learn how to handle basic financial data using the Pandas library. 
# Specifically, we'll focus on loading and displaying Tesla's ($TSLA) stock data. 
# Understanding how to manipulate data using Pandas is an essential skill in data analysis and can significantly improve your machine-learning models.

# Pandas is a powerful Python library that provides data structures and data analysis tools. 
# It's particularly useful for managing time series data, like stock prices, transaction records, and more.

# Loading Data using the 'datasets' Library
# We'll start by loading the Tesla ($TSLA) dataset using the datasets library - 
# a library that's already built in the CodeSignal IDE. This library simplifies the process of fetching well-known datasets, 
# so you can focus on analyzing and manipulating the data rather than spending time gathering it.

# Here’s how you can load the TSLA dataset:
import datasets

# Load the TSLA dataset using the datasets library
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')
# In this code, we import the datasets library and use its load_dataset function to fetch the Tesla stock prices. 
# The argument 'codesignal/tsla-historic-prices' tells the datasets library exactly which dataset to load.

# Creating a DataFrame in Pandas
# Once we have our data, the next step is to create a DataFrame using Pandas. 
# A DataFrame is a two-dimensional, size-mutable, and heterogeneous tabular data structure with labeled axes (rows and columns). 
# Think of it as an Excel spreadsheet or a SQL table but with much more functionality.

# Here’s how you can create a DataFrame using Pandas:
import pandas as pd

# Create DataFrame from the dataset
tesla_df = pd.DataFrame(tesla_data['train'])

# In this snippet, we import the Pandas library and create a DataFrame called tesla_df using the data we loaded previously. 
# The tesla_data['train'] part extracts the training data from the dataset.

# Displaying Data from a DataFrame: The Head
# Now that we have our DataFrame, it's crucial to know how to display its contents. Displaying data helps us understand its structure and the kind of information it holds.

# To display the first few rows of our DataFrame, we can use the head() method. This method is handy when you want to quickly check the beginning of your DataFrame:

# Display the first few rows of the DataFrame
print(tesla_df.head())
# The output of the above code will be:

         Date      Open      High       Low     Close  Adj Close     Volume
0  2010-06-29  1.266667  1.666667  1.169333  1.592667   1.592667  281494500
1  2010-06-30  1.719333  2.028000  1.553333  1.588667   1.588667  257806500
2  2010-07-01  1.666667  1.728000  1.351333  1.464000   1.464000  123282000
3  2010-07-02  1.533333  1.540000  1.247333  1.280000   1.280000   77097000
4  2010-07-06  1.333333  1.333333  1.055333  1.074000   1.074000  103003500

# This output shows a truncated view of Tesla stock prices starting from its initial public offering (IPO). 
# Each row represents a day with columns for the date, opening price, highest price of the day, lowest price of the day, 
# closing price, adjusted closing price, and the volume of stocks traded.

# Displaying Data from a DataFrame: The Tail
# You can also use the tail() method to view the last few rows of the DataFrame. This can be helpful in different scenarios, such as when checking the most recent stock prices:
            Date        Open        High  ...       Close   Adj Close     Volume
3342  2023-10-09  255.309998  261.359985  ...  259.670013  259.670013  101377900
3343  2023-10-10  257.750000  268.940002  ...  263.619995  263.619995  122656000
3344  2023-10-11  266.200012  268.600006  ...  262.989990  262.989990  103706300
3345  2023-10-12  262.920013  265.410004  ...  258.869995  258.869995  111508100
3346  2023-10-13  258.899994  259.600006  ...  251.119995  251.119995  102073800

[5 rows x 7 columns]

# This output demonstrates the structure of the dataset showing recent trading days. It provides insights into the latest trends, i
# including closing and opening prices, for Tesla stock. Such information is crucial for making informed investment decisions.

# By mastering these functions, you will be able to quickly inspect and understand any dataset you work with, 
# which is a foundational skill in data manipulation and analysis.
# Lesson Summary and Practice
# Learned the basics of loading datasets, creating DataFrames, and displaying data using the Panda's library. 
# These skills are crucial for any financial data analysis and will serve as a foundation for more advanced data manipulation tasks.

# In this lesson, you specifically covered:

# What Pandas is and its importance in financial data analysis
# How to load a dataset using the datasets library
# How to create a DataFrame in Pandas
# How to display data from a DataFrame using head() and tail()
# Next, we will move on to practice exercises where you can solidify these concepts. 
# Practice is essential for improving your skills, ensuring you can confidently manipulate and interpret financial data. Let's get started with some hands-on tasks!

# Sample Code ------->
import datasets
import pandas as pd

# Load the TSLA dataset using the datasets library
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')

# Create DataFrame from the dataset
tesla_df = pd.DataFrame(tesla_data['train'])

# Display the first few rows of the DataFrame
print(tesla_df.head())

# Output -------------------->
         Date      Open      High       Low     Close  Adj Close     Volume
0  2010-06-29  1.266667  1.666667  1.169333  1.592667   1.592667  281494500
1  2010-06-30  1.719333  2.028000  1.553333  1.588667   1.588667  257806500
2  2010-07-01  1.666667  1.728000  1.351333  1.464000   1.464000  123282000
3  2010-07-02  1.533333  1.540000  1.247333  1.280000   1.280000   77097000
4  2010-07-06  1.333333  1.333333  1.055333  1.074000   1.074000  103003500

import datasets
import pandas as pd

# Load the TSLA dataset using the datasets library
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')

# Create DataFrame from the dataset
tesla_df = pd.DataFrame(tesla_data['train'])

# Display the first few rows of the DataFrame
print(tesla_df.tail())

# Output ---------------------------------------------------------->
 Date        Open        High  ...       Close   Adj Close     Volume
3342  2023-10-09  255.309998  261.359985  ...  259.670013  259.670013  101377900
3343  2023-10-10  257.750000  268.940002  ...  263.619995  263.619995  122656000
3344  2023-10-11  266.200012  268.600006  ...  262.989990  262.989990  103706300
3345  2023-10-12  262.920013  265.410004  ...  258.869995  258.869995  111508100
3346  2023-10-13  258.899994  259.600006  ...  251.119995  251.119995  102073800


import pandas as pd
import datasets

# Load the TSLA dataset using the datasets library
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')

# Create DataFrame from the dataset
tesla_df = pd.DataFrame(tesla_data['train'])

# Display the first few rows of the DataFrame
print(tesla_df.head())

# Display the last few rows of the DataFrame
print(tesla_df.tail())

# Output ------------------------------------------------------->
Date      Open      High       Low     Close  Adj Close     Volume
0  2010-06-29  1.266667  1.666667  1.169333  1.592667   1.592667  281494500
1  2010-06-30  1.719333  2.028000  1.553333  1.588667   1.588667  257806500
2  2010-07-01  1.666667  1.728000  1.351333  1.464000   1.464000  123282000
3  2010-07-02  1.533333  1.540000  1.247333  1.280000   1.280000   77097000
4  2010-07-06  1.333333  1.333333  1.055333  1.074000   1.074000  103003500
            Date        Open        High  ...       Close   Adj Close     Volume
3342  2023-10-09  255.309998  261.359985  ...  259.670013  259.670013  101377900
3343  2023-10-10  257.750000  268.940002  ...  263.619995  263.619995  122656000
3344  2023-10-11  266.200012  268.600006  ...  262.989990  262.989990  103706300
3345  2023-10-12  262.920013  265.410004  ...  258.869995  258.869995  111508100
3346  2023-10-13  258.899994  259.600006  ...  251.119995  251.119995  102073800

[5 rows x 7 columns]


import pandas as pd
import datasets

# TODO: Load the TSLA dataset using the datasets library
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')

# TODO: Create DataFrame from the dataset
tesla_df = pd.DataFrame(tesla_data['train'])

# Display the first few rows of the DataFrame
print("First few rows of the dataset:")
print(tesla_df.head())

# Display the last few rows of the DataFrame
print("\nLast few rows of the dataset:")
print(tesla_df.tail())


# Output -------------------------------------------------------------->
First few rows of the dataset:
         Date      Open      High       Low     Close  Adj Close     Volume
0  2010-06-29  1.266667  1.666667  1.169333  1.592667   1.592667  281494500
1  2010-06-30  1.719333  2.028000  1.553333  1.588667   1.588667  257806500
2  2010-07-01  1.666667  1.728000  1.351333  1.464000   1.464000  123282000
3  2010-07-02  1.533333  1.540000  1.247333  1.280000   1.280000   77097000
4  2010-07-06  1.333333  1.333333  1.055333  1.074000   1.074000  103003500

Last few rows of the dataset:
            Date        Open        High  ...       Close   Adj Close     Volume
3342  2023-10-09  255.309998  261.359985  ...  259.670013  259.670013  101377900
3343  2023-10-10  257.750000  268.940002  ...  263.619995  263.619995  122656000
3344  2023-10-11  266.200012  268.600006  ...  262.989990  262.989990  103706300
3345  2023-10-12  262.920013  265.410004  ...  258.869995  258.869995  111508100
3346  2023-10-13  258.899994  259.600006  ...  251.119995  251.119995  102073800

[5 rows x 7 columns]


import pandas as pd
import datasets

# TODO: Load the TSLA dataset (`codesignal/tsla-historic-prices`) using the `datasets` library
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')
# TODO: Create a DataFrame from the loaded dataset
tesla_df = pd.DataFrame(tesla_data['train'])
# TODO: Display the first few rows of the DataFrame
print("First few rows of the dataset:")
print(tesla_df.head())
# TODO: Display the last few rows of the DataFrame
print("\nLast few rows of the dataset:")
print(tesla_df.tail())

# Introduction to Data Inspection ----------------------------------------------------------------------------|
# Hello! In this lesson, we will explore the fundamental techniques for inspecting financial data using the Pandas library in Python. 
# Our goal is to enable you to load financial data, inspect its structure, and perform basic data analysis. Let's get started!
# Loading and Displaying Data
# First, let's recap how to import the necessary libraries and load the dataset. In this scenario, we'll use Tesla (TSLA) historical stock prices.

# Import Libraries: We need to import pandas for data manipulation and the datasets library to load our data.
# Load the Dataset: We use the load_dataset function from the datasets library to load the Tesla dataset.
# Convert to DataFrame: We convert the loaded dataset into a Pandas DataFrame.
# Display Data: Using the head() and tail() methods, we can view the first few and last few rows of the dataset, respectively.
# Here's the code to achieve this:

import pandas as pd
import datasets

# Load TSLA dataset
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla_data['train'])

# Display first 5 rows of the DataFrame
print(tesla_df.head())
# This code snippet loads the TSLA dataset and displays the first 5 rows to help us get a quick look at the data.

# Inspecting Data Structure
# Next, we want to understand the structure of our dataset. This involves examining the columns, data types, and the number of non-null entries. 
# The info() method of a Pandas DataFrame provides a concise summary of these details.

# Data Structure Information: The info() method reveals important aspects such as:
# Column names and data types
# Non-null counts for each column
# Here's the code to inspect the data structure:

# Print basic information about the dataset
print(tesla_df.info())
# The output will be:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3347 entries, 0 to 3346
Data columns (total 7 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   Date       3347 non-null   object 
 1   Open       3347 non-null   float64
 2   High       3347 non-null   float64
 3   Low        3347 non-null   float64
 4   Close      3347 non-null   float64
 5   Adj Close  3347 non-null   float64
 6   Volume     3347 non-null   int64  
dtypes: float64(5), int64(1), object(1)
memory usage: 183.2+ KB
None
# This output summarizes the dataset structure, showing that it consists of 3347 entries with 7 different columns. 
# It also highlights that there are no missing values in the dataset, and it provides the data type of each column, 
# which is essential to understand before performing any data manipulation or analysis.

# Summary Statistics
# To gain preliminary insights into our data, we can use the describe() method, which provides summary statistics such as mean, standard deviation, minimum, and maximum values, and quartiles.

# Descriptive Statistics: The describe() method presents these key statistics for all numerical columns in the DataFrame, helping us understand data distribution and identify any anomalies.
# Here's the code to generate summary statistics:

# Display summary statistics
print(tesla_df.describe())
# The output will be:

              Open         High  ...    Adj Close        Volume
count  3347.000000  3347.000000  ...  3347.000000  3.347000e+03
mean     67.901248    69.413435  ...    67.886520  9.643192e+07
std     100.209872   102.472746  ...   100.136888  8.058132e+07
min       1.076000     1.108667  ...     1.053333  1.777500e+06
25%      10.152000    10.432000  ...    10.081333  4.540425e+07
50%      16.793333    17.000000  ...    16.771334  8.011650e+07
75%      66.069336    67.129334  ...    65.896000  1.230548e+08
max     411.470001   414.496674  ...   409.970001  9.140820e+08

[8 rows x 6 columns]
# This concise summary details the distribution of Tesla's stock prices, including the mean, standard deviation, minimum, 
# and maximum values across various metrics such as opening price, high, low, close, adjusted close, and volume. 
# It provides a snapshot of the stock's volatility and trading volume, which are critical for financial analysis.

# Conclusion and Summary
# In this lesson, you have learned the basics of data inspection using Pandas. We have covered how to:

# Load a dataset and convert it into a DataFrame.
# Display the data using the head() method.
# Inspect the data structure using the info() method.
# Generate summary statistics using the describe() method.

# These fundamental skills are crucial for analyzing financial data and making informed trading decisions. 
# Practice exercises will follow to reinforce your understanding and improve your data handling proficiency. 
# Let's keep up the momentum and continue mastering financial data handling in Pandas!

import pandas as pd
import datasets

# Load TSLA dataset
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla_data['train'])

# Display the first 5 rows of the DataFrame
print(tesla_df.head())

# Print basic information about the dataset
print(tesla_df.info())

# Display summary statistics
print(tesla_df.describe())

# Introduction to Time Series Data Handling
# Hello, and welcome back! In today's lesson, we'll dive into the fundamentals of handling time series data using the Pandas library. 
# Specifically, we'll focus on working with Tesla's ($TSLA) stock data. The primary goal is to make you proficient in loading, converting, 
# and sorting time series data, which is a critical skill for financial analysis and trading.

# By the end of this lesson, you'll be able to load stock data, convert it into a datetime format, set it as an index, and sort it for future analysis.

# Loading the Tesla Dataset
# Let's quickly revise how to load Tesla's historical stock data and convert it into a Pandas DataFrame for easier manipulation:


import pandas as pd
import datasets

# Load TSLA dataset
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla_data['train'])

# Display the first few rows
print(tesla_df.head())
The output will look like this:


         Date      Open      High       Low     Close  Adj Close     Volume
0  2010-06-29  1.266667  1.666667  1.169333  1.592667   1.592667  281494500
1  2010-06-30  1.719333  2.028000  1.553333  1.588667   1.588667  257806500
2  2010-07-01  1.666667  1.728000  1.351333  1.464000   1.464000  123282000
3  2010-07-02  1.533333  1.540000  1.247333  1.280000   1.280000   77097000
4  2010-07-06  1.333333  1.333333  1.055333  1.074000   1.074000  103003500

# Now that you've loaded the Tesla dataset and displayed the first few rows let's move on to handling the Date column.

# Understanding Date and Time in Pandas
# The Date column is crucial for time series data analysis. It's currently in string format, so we'll need to convert it to a datetime object. 
# By converting it, you can leverage Pandas’ powerful date-time functionalities, such as resampling and shifting.

# Here's how to convert the Date column:


# Convert the Date column to datetime type
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

# Display the first few rows to verify the change
print(tesla_df.head())

Output:


        Date      Open      High       Low     Close  Adj Close     Volume
0 2010-06-29  1.266667  1.666667  1.169333  1.592667   1.592667  281494500
1 2010-06-30  1.719333  2.028000  1.553333  1.588667   1.588667  257806500
2 2010-07-01  1.666667  1.728000  1.351333  1.464000   1.464000  123282000
3 2010-07-02  1.533333  1.540000  1.247333  1.280000   1.280000   77097000
4 2010-07-06  1.333333  1.333333  1.055333  1.074000   1.074000  103003500

# Now, the Date column has been converted to datetime format, enabling us to perform further time series operations.



