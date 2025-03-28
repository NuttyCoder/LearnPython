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

# Setting the Date as the Index
# Setting the Date column as the index is crucial for time series operations. It allows us to sort the data chronologically and makes it easier to slice by specific dates.

# Here's how to set the date as the index:

# Set Date column as the index
tesla_df.set_index('Date', inplace=True)

# Display the first few rows to verify the change
print(tesla_df.head())

Output:
                Open      High       Low     Close  Adj Close     Volume
Date                                                                    
2010-06-29  1.266667  1.666667  1.169333  1.592667   1.592667  281494500
2010-06-30  1.719333  2.028000  1.553333  1.588667   1.588667  257806500
2010-07-01  1.666667  1.728000  1.351333  1.464000   1.464000  123282000
2010-07-02  1.533333  1.540000  1.247333  1.280000   1.280000   77097000
2010-07-06  1.333333  1.333333  1.055333  1.074000   1.074000  103003500

# Now the Date column is set as the index, making our DataFrame easier to work with in time series analysis. 
# The inplace=True argument allows you to modify the DataFrame in-place. This means it directly alters the original 
# DataFrame without creating and returning a new one. Using inplace=True can be more memory efficient and slightly faster, 
# as it avoids the overhead of copying the DataFrame.

# Sorting the DataFrame by Date
# Sorting the data by date ensures chronological order, which is essential for analysis such as plotting, calculating returns, and other time-based computations. 
# To demonstrate sorting clearly, we'll sort the data in descending order.

Here's how to sort the DataFrame based on the index in descending order:

# Sort the DataFrame based on the index in descending order
tesla_df.sort_index(ascending=False, inplace=True)

# Display the first few rows to verify the change
print(tesla_df.head())

# The output of the above code will be:

                  Open        High  ...   Adj Close     Volume
Date                                ...                       
2023-10-13  258.899994  259.600006  ...  251.119995  102073800
2023-10-12  262.920013  265.410004  ...  258.869995  111508100
2023-10-11  266.200012  268.600006  ...  262.989990  103706300
2023-10-10  257.750000  268.940002  ...  263.619995  122656000
2023-10-09  255.309998  261.359985  ...  259.670013  101377900

# This confirms that after setting the Date as the index and sorting in descending order, the DataFrame is now correctly sorted by the date in descending order, 
# starting from the most recent entry in the dataset. It ensures that any analysis conducted on the dataset accounts for the temporal sequence of events.

# Now, the DataFrame is sorted chronologically based on the date index in descending order.

# Verifying the Changes
# Finally, it's essential to verify that all the changes you made have been applied correctly. 
# We can do this by printing the first few rows of the DataFrame again.

# Here’s the complete code to verify all the steps:


import pandas as pd
import datasets

# Load TSLA dataset
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla_data['train'])

# Convert the Date column to datetime type and set as index
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
tesla_df.set_index('Date', inplace=True)

# Sort the DataFrame based on the index in descending order
tesla_df.sort_index(ascending=False, inplace=True)

# Display the first few rows to verify the changes
print(tesla_df.head())

# Output:
                  Open        High  ...   Adj Close     Volume
Date                                ...                       
2023-10-13  258.899994  259.600006  ...  251.119995  102073800
2023-10-12  262.920013  265.410004  ...  258.869995  111508100
2023-10-11  266.200012  268.600006  ...  262.989990  103706300
2023-10-10  257.750000  268.940002  ...  263.619995  122656000
2023-10-09  255.309998  261.359985  ...  259.670013  101377900

# This confirms that our DataFrame is properly loaded, converted, indexed, and sorted in descending order, and it is now ready for further financial analysis.

import pandas as pd
import datasets

# Step 1: Load TSLA dataset
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla_data['train'])

# Step 2: Convert the Date column to datetime type
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

# Step 3: Set the Date column as the index
tesla_df.set_index('Date', inplace=True)

# Step 4: Sort the DataFrame based on the index
tesla_df.sort_index(ascending=True, inplace=True)

# Step 5: Display the first few rows to verify the changes
print(tesla_df.head())


import pandas as pd
import datasets

# Step 1: Load TSLA dataset
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla_data['train'])

# Step 2: Convert the Date column to datetime type
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

# Step 3: Set the Date column as the index
tesla_df.set_index('Date', inplace=True)

# Step 4: Sort the DataFrame based on the index
tesla_df.sort_index(ascending=False, inplace=True)

# Step 5: Display the first few rows to verify the changes
print(tesla_df.head())


# The world of Basic Plotting with Matplotlib. 
# You'll learn how to create basic line plots to visualize Tesla's ($TSLA) stock data. 
# This lesson is essential as visualizing financial data is crucial for identifying trends and making informed trading decisions. 
# By the end of this lesson, you'll be proficient in plotting data using Matplotlib, customizing plots, and interpreting the results.

# Introduction to Matplotlib
# Matplotlib is a powerful plotting library in Python that allows developers to create a wide variety of static, animated, and interactive plots. 
# It's widely used in data visualization because of its simplicity and versatility.

# Why Matplotlib?

# Versatility: Matplotlib can be used to create plots ranging from simple line charts to complex 3D plots.
# Customization: Almost every aspect of a Matplotlib plot can be customized.
#Integration: It works well with Pandas, making it easy to visualize DataFrame data.
#To get started with Matplotlib, you need to import the pyplot module:

import matplotlib.pyplot as plt

# Preparing Data for Visualization
# Before plotting, we need to prepare our Tesla stock data.

# Loading the Tesla Dataset: We'll use the load_dataset function from the datasets library to load Tesla's historic price data:

import pandas as pd
from datasets import load_dataset

# Load TSLA dataset
tesla_data = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla_data['train'])

# Converting Dates to Datetime Objects: To handle the time series data correctly, we need to convert the 'Date' column to datetime format:

tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
# Setting Date as Index: Next, we'll set the 'Date' column as the index of our DataFrame and sort it:

tesla_df.set_index('Date', inplace=True)
tesla_df.sort_index(inplace=True)

# At this point, our DataFrame is ready for plotting.
# Creating Basic Line Plots
# Now that our data is prepared - let's create a basic line plot.

# Using Matplotlib, we can plot the 'Close' prices against dates:


plt.plot(tesla_df.index, tesla_df['Close'])

# In the plt.plot() function:

# tesla_df.index: Represents the x-axis data, which, in this case, is the dates from the DataFrame index.
# tesla_df['Close']: Represents the y-axis data, which are the closing prices from the 'Close' column of the DataFrame.
# It's also essential to add titles and labels to make our plot more informative:


plt.title('TSLA Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')

# On top of that, adding a legend helps identify what the plotted line represents:


plt.legend(['Close Price'])

# Customizing Plots
# Customizing plots improves their readability and aesthetic appeal.

# We can adjust the figure size to ensure that our plots are well-proportioned. 
# The figsize parameter takes a tuple (width, height) in inches. For example, figsize=(10, 5) creates a f
# figure that is 10 inches wide and 5 inches tall. This helps in setting the size of the plot for better visualization:
plt.figure(figsize=(10, 5))

# Customizing line colors and styles makes plots visually appealing:
plt.plot(tesla_df.index, tesla_df['Close'], color='blue', linestyle='-', linewidth=2)

# Grid lines can make it easier to read the plot:
plt.grid(True)

# To render the plotted graph, we use:
plt.show()

# Displaying and Interpreting Plots
# Let's complete our plot and see the final result.

# Here is the final code:


import matplotlib.pyplot as plt
import pandas as pd
from datasets import load_dataset

# Load TSLA dataset
tesla_data = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla_data['train'])

# Convert 'Date' column to datetime
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

# Set 'Date' as index and sort it
tesla_df.set_index('Date', inplace=True)
tesla_df.sort_index(inplace=True)

# Plot the 'Close' prices
plt.figure(figsize=(10, 5))
plt.plot(tesla_df.index, tesla_df['Close'], color='blue', linestyle='-', linewidth=2)

# Add titles and labels
plt.title('TSLA Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')

# Add legend and grid
plt.legend(['Close Price'])
plt.grid(True)

# Display the plot
plt.show()

# How to use Matplotlib to visualize Tesla's ($TSLA) stock data. 
# The basics of importing and setting up Matplotlib, preparing data for visualization, 
# creating basic line plots, and customizing plots for better readability. 
# These skills are crucial for conducting financial analyses and making informed trading decisions.


# Introduction to Date Filtering
# In this lesson, we'll explore how to filter time series financial data by date range using the Pandas library. 
# Filtering data by specific date ranges is vital in financial analysis, allowing us to focus on periods of interest, 
# such as a particular year or month. This skill is essential for traders and analysts who need to examine stock 
# performance during specific periods, such as economic crises or fiscal quarters.


# Converting Date Columns to Datetime Objects ---------------------------------------------------------->
# The first step in filtering data by date is to ensure that the date column is in a suitable format. Let's start by loading the Tesla ($TSLA) stock dataset and converting the "Date" column to datetime objects using pd.to_datetime().


import pandas as pd
import datasets

# Load TSLA dataset
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla_data['train'])

# Convert the Date column to datetime type
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

# Display initial rows to inspect the format
print(tesla_df.head())
# The output of the above code confirms that the 'Date' column is now in datetime format, which is crucial for time series analysis:


        Date      Open      High       Low     Close  Adj Close     Volume
0 2010-06-29  1.266667  1.666667  1.169333  1.592667   1.592667  281494500
1 2010-06-30  1.719333  2.028000  1.553333  1.588667   1.588667  257806500
2 2010-07-01  1.666667  1.728000  1.351333  1.464000   1.464000  123282000
3 2010-07-02  1.533333  1.540000  1.247333  1.280000   1.280000   77097000
4 2010-07-06  1.333333  1.333333  1.055333  1.074000   1.074000  103003500

# Setting the Date Column as Index ------------------------------------------------------------------------->
# Setting the date column as the index of the DataFrame and sorting it simplifies the process of slicing and filtering data based on dates. 
# It also enhances performance during such operations.

# Here’s how to set the "Date" column as the index and sort it:


# Set the Date column as the index
tesla_df.set_index('Date', inplace=True)

# Sort the DataFrame based on the index
tesla_df.sort_index(inplace=True)
print(tesla_df.head())
# The output of the above code will be:

                Open      High       Low     Close  Adj Close     Volume
Date                                                                    
2010-06-29  1.266667  1.666667  1.169333  1.592667   1.592667  281494500
2010-06-30  1.719333  2.028000  1.553333  1.588667   1.588667  257806500
2010-07-01  1.666667  1.728000  1.351333  1.464000   1.464000  123282000
2010-07-02  1.533333  1.540000  1.247333  1.280000   1.280000   77097000
2010-07-06  1.333333  1.333333  1.055333  1.074000   1.074000  103003500
# This output confirms that the Date column has successfully been set as the index of the DataFrame 
# and successfully sorted in chronological order based on this index, ensuring an accurate timeline for subsequent analysis.

#  Filtering Data by Specific Date Range ------------------------------------------------------------------------------------>
# With the date column converted to datetime objects, set as the index, and sorted, we can now filter the DataFrame by a specific date range. 
# This technique is particularly useful when you need to analyze data for a specific year, month, or any custom date range.

# Filtering the dataset for the year 2020
tesla_2020 = tesla_df.loc['2020']
print(tesla_2020.head())
# In this code, loc is a Pandas method used for label-based indexing. 
# It allows you to select rows and columns based on labels, such as dates in this case. 
# Here, we use loc to filter the DataFrame based on the date labels, extracting all rows corresponding to the year 2020.

# The output of the above code will be:

                 Open       High        Low      Close  Adj Close     Volume
Date                                                                        
2020-01-02  28.299999  28.713333  28.114000  28.684000  28.684000  142981500
2020-01-03  29.366667  30.266666  29.128000  29.534000  29.534000  266677500
2020-01-06  29.364668  30.104000  29.333332  30.102667  30.102667  151995000
2020-01-07  30.760000  31.441999  30.224001  31.270666  31.270666  268231500
2020-01-08  31.580000  33.232666  31.215334  32.809334  32.809334  467164500

#This output demonstrates the successful filtering of the DataFrame to show stock prices for the start of 2020. 
# The simplified view focuses on the 'Open' column to display the opening stock prices at the beginning of the year, 
# providing a quick insight into Tesla's stock performance during this period.

# Other Ways to Filter by Date ---------------------------------------------------------------------->
# We can also filter for more specific date ranges, such as a particular month or quarter:

# Filtering data for January 2020
tesla_jan_2020 = tesla_df.loc['2020-01']
print(tesla_jan_2020.head())

# The output of the above code will be:


                 Open       High        Low      Close  Adj Close     Volume
Date                                                                        
2020-01-02  28.299999  28.713333  28.114000  28.684000  28.684000  142981500
2020-01-03  29.366667  30.266666  29.128000  29.534000  29.534000  266677500
2020-01-06  29.364668  30.104000  29.333332  30.102667  30.102667  151995000
2020-01-07  30.760000  31.441999  30.224001  31.270666  31.270666  268231500
2020-01-08  31.580000  33.232666  31.215334  32.809334  32.809334  467164500
# To filter a quarter, the code will look like this:
# Filtering data from January 2020 to March 2020 (Q1)
# Unlike the common Python slicing operator, here, March 2020 (2020-03) is inclusive
tesla_q1_2020 = tesla_df.loc['2020-01':'2020-03']
print(tesla_q1_2020.tail())

The output of the above code will be:

                 Open       High        Low      Close  Adj Close     Volume
Date                                                                        
2020-03-25  36.349998  37.133331  34.074001  35.950001  35.950001  318340500
2020-03-26  36.492668  37.333332  34.150002  35.210667  35.210667  260710500
2020-03-27  33.666668  35.053333  32.935333  34.290668  34.290668  215661000
2020-03-30  34.017334  34.443333  32.748669  33.475334  33.475334  179971500
2020-03-31  33.416668  36.197334  33.133331  34.933334  34.933334  266572500

# Plotting the Filtered Data ------------------------------------------------------------------------------------>
# After filtering the data, visualizing it can help identify patterns and trends over the specified date range.
# We will use Matplotlib, a popular plotting library in Python, to create a time series plot.

# Let's visualize the January 2020 data and the Q1 2020 data for Tesla stock:


import matplotlib.pyplot as plt

# Plotting the filtered data for Q1 2020
tesla_q1_2020 = tesla_df.loc['2020-01':'2020-03']

plt.figure(figsize=(10, 5))
plt.plot(tesla_q1_2020.index, tesla_q1_2020['Close'], marker='o', linestyle='-')
plt.title('Tesla Stock Prices in Q1 2020')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.show()


# By visualizing the data, you can gain insights into stock performance and identify trends over the specified periods,
# thereby enhancing your financial analysis capabilities.

# Learned how to filter time series financial data by date ranges using the Pandas library. 
# We covered converting date columns to datetime objects, setting the date column as the index, sorting the 
# DataFrame chronologically, and filtering data by specific date ranges. These techniques are essential for 
# focusing on specific periods relevant to your financial analysis or trading strategy.

# Convert the Date column to datetime type
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

# Set the Date column as the index
tesla_df.set_index('Date', inplace=True)

# Sort the DataFrame based on the index
tesla_df.sort_index(inplace=True)

# Filtering data for January 2020 to March 2020
tesla_q1_2020 = tesla_df.loc['2020-01':'2020-03']
print(tesla_q1_2020.tail())



import pandas as pd
import datasets

# Load TSLA dataset
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla_data['train'])

# Convert the Date column to datetime type
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

# Set the Date column as the index
tesla_df.set_index('Date', inplace=True)

# Sort the DataFrame based on the index
tesla_df.sort_index(inplace=True)

# TODO: Filter the dataset for the years 2018, 2019, 2020
tesla_2018_2020 = tesla_df.loc['2018-01': '2020-12']
print(tesla_2018_2020.head())


import pandas as pd
import datasets

# TODO: Load the Tesla (TSLA) dataset `codesignal/tsla-historic-prices` and create a DataFrame
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla_data['train'])
# TODO: Convert the 'Date' column to datetime type to handle date calculations
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
# TODO: Set the converted 'Date' column as the DataFrame index to facilitate date-based querying
tesla_df.set_index('Date', inplace=True)
# TODO: Sort the DataFrame based on the date index to ensure it's ordered chronologically
tesla_df.sort_index(inplace=True)
# TODO: Filter the DataFrame to get data from January 2020 to March 2020 (Q1) and print the first few rows
tesla_q1_2020 = tesla_df.loc['2020-01': '2020-03']
print(tesla_q1_2020.head())

# Technical Indicators in Financial Analysis course! In today's lesson, we'll explore how to calculate and visualize the Simple Moving Average (SMA) for Tesla ($TSLA) stock prices using Pandas in Python. The goal is to help you understand how to handle stock price data, compute a key technical indicator (SMA), and interpret the results visually. Here is the lesson plan:

# Introduction to Financial Data Handling.
# Loading and Preprocessing $TSLA Data.
# Calculating the 20-day Simple Moving Average (SMA).
# Visualizing SMA with Stock Prices.
# Summary and Next Steps.
import pandas as pd
import datasets
import matplotlib.pyplot as plt

# Load TSLA dataset
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla_data['train'])

# Convert 'Date' to datetime format and set as index
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
tesla_df.set_index('Date', inplace=True)

# Sort the dataset by date
tesla_df.sort_index(inplace=True)

# Calculate the 20-day Simple Moving Average for the Close Price
tesla_df['SMA_20'] = tesla_df['Close'].rolling(window=20).mean()

# Using a smaller date range for better visualization
tesla_df_small = tesla_df.loc['2018']

# Plotting
tesla_df_small[['Close', 'SMA_20']].plot(figsize=(12, 6), title="TSLA Close Price and 20-day SMA (2018)")
plt.show()

# Print first few rows of the dataframe to check the SMA calculations
print(tesla_df_small.head())

# Introduction to EMA
# Welcome! In today's lesson, we will calculate the Exponential Moving Average (EMA) for Tesla ($TSLA) stock using Pandas. 
# Understanding EMA will allow you to give more weight to recent stock prices, which can help you make smarter trading decisions compared to using a Simple Moving Average (SMA).

# The goal of this lesson is to help you understand how to:

# Handle and preprocess financial data.
# Calculate the EMA.
# Visualize the EMA using Matplotlib.
# Introduction to EMA
# The Exponential Moving Average (EMA) is a type of moving average that places a greater weight and significance on the most recent data points.
# This makes it more responsive to new information.

# In many trading strategies, the EMA is preferred over the SMA because it reacts more quickly to recent price changes, making it a reliable tool for identifying trends.

# The formula for EMA involves:

# Current Price (P): The price at the current time.

# Previous EMA (EMAprevious): The EMA calculated at the previous time.

# Smoothing Constant (α): A constant that is derived from the number of periods. It is calculated as: 
# α=2/N+1
# ​where N is the number of periods.

# The EMA formula is:
# EMAcurrent=(P⋅α)+(EMAprevious⋅(1−α))

# Loading and Preprocessing the Tesla Dataset
# Before we calculate the EMA, we need to load and preprocess the dataset to make it suitable for time series analysis. 
# We will use the load_dataset function from the datasets library to fetch historical Tesla stock prices.

#Here is how you load and preprocess the dataset:

import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset

# Load Tesla dataset
dataset = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(dataset['train'])

# Convert the 'Date' column to datetime
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

# Set 'Date' as index
tesla_df.set_index('Date', inplace=True)

# Sort the data by date
tesla_df.sort_index(inplace=True)
# To get a sense of the data we're working with, let's display the first few rows:

print(tesla_df.head())

# Running this, we should see the first few rows of the Tesla stock historical data, which typically 
# includes columns like Date, Open, High, Low, Close, Volume, etc. This preprocessing ensures our data is in chronological order, essential for time series manipulation.

# Calculating the EMA
# With our data preprocessed, the next step is to calculate the EMA. Pandas makes this task straightforward with its ewm() function, 
# which calculates the Exponential Weighted Moving Average.

# The ewm() function takes parameters like span (the number of periods) and adjust.

# Here, we compute the 20-day EMA for the closing price:

# Calculate the 20-day Exponential Moving Average for the Close Price
tesla_df['EMA_20'] = tesla_df['Close'].ewm(span=20, adjust=False).mean()

# The ewm(span=20, adjust=False).mean() calculates the 20-day EMA. 
# The adjust=False parameter ensures that the smoothing factor is applied only once to the series.

# To verify that the EMA calculation is added to our DataFrame:

print(tesla_df[['Close', 'EMA_20']].head())

# The output of the above code will be:


               Close    EMA_20
Date                          
2010-06-29  1.592667  1.592667
2010-06-30  1.588667  1.592286
2010-07-01  1.464000  1.580068
2010-07-02  1.280000  1.551490
2010-07-06  1.074000  1.506015

# This output demonstrates the initial calculation of the 20-day Exponential Moving Average (EMA) 
# alongside the actual closing prices for the first few days in the dataset. The EMA gives more weight to recent prices, 
# which is evident from how it starts to adjust as new price data comes in.

# Visualizing the EMA
# Visualizing the EMA alongside the closing prices helps in understanding the trend and the impact of recent prices. 
# We will use Matplotlib to plot the data. To make the plot clearer, we will consider data from the year 2018.

# We narrow our dataset to a smaller date range, such as one year, to improve visualization clarity.

import matplotlib.pyplot as plt

# Using a smaller date range for better visualization
tesla_df_small = tesla_df.loc['2018']
# We plot the closing prices and the 20-day EMA using Matplotlib:
# Plotting
tesla_df_small[['Close', 'EMA_20']].plot(figsize=(12, 6), title="TSLA Close Price and 20-day EMA (2018)")
plt.show()

# Lesson Summary
# 1. Load and preprocess Tesla stock price data.
# 2. Calculate the 20-day Exponential Moving Average (EMA) using Pandas.
# 3. Viosualize the EMA alsongside the closing price using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset

# Load Tesla dataset
dataset = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(dataset['train'])

# Convert the 'Date' column to datetime and set it as index
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
tesla_df.set_index('Date', inplace=True)

# Sort the data by date
tesla_df.sort_index(inplace=True)

# Calculate the 200-day Exponential Moving Average for the Close Price
tesla_df['EMA_200'] = tesla_df['Close'].ewm(span=200, adjust=False).mean()

# Print the first few rows to verify the calculations
print(tesla_df[['Close', 'EMA_200']].head())

# Using a smaller date range for better visualization
tesla_df_small = tesla_df.loc['2018']

# Plotting the closing prices and the 20-day EMA
tesla_df_small[['Close', 'EMA_200']].plot(figsize=(12, 6), title="TSLA Close Price and 200-day EMA (2018)")
plt.show()

# Volume -------------------------------->

import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset

# Load Tesla dataset
dataset = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(dataset['train'])

# Convert the 'Date' column to datetime
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

# Set 'Date' as index
tesla_df.set_index('Date', inplace=True)

# Sort the data by date
tesla_df.sort_index(inplace=True)

# TODO: Calculate 50-day EMA for the Volume
tesla_df['EMA_50'] = tesla_df['Volume'].ewm(span=50, adjust=False).mean()
# Using a smaller date range for better visualization
tesla_df_small = tesla_df.loc['2018']

# TODO: Plot the Volume and 50-day EMA
tesla_df_small[['Volume', 'EMA_50']].plot(figsize=(12, 6), title="TSLA Volume Price and 50-day EMA (2018)")
plt.show()

# Comparing Simple Moving Average (SMA) and Exponential Moving Average (EMA) using Tesla ($TSLA) stock data. 
# This lesson will help you revise how to handle financial data with Pandas, calculate both SMA and EMA, and create visualizations 
# to understand and compare these technical indicators.

# Goal: By the end of this lesson, you will be able to load financial data, compute SMA and EMA, and visualize these indicators to make informed trading decisions.
# Lesson Plan:

# Loading and Preparing the Dataset
# Calculating and Comparing SMA and EMA
# Subsetting the Data for Visualization
# Plotting SMA and EMA for Comparison

# Loading and Preparing the Dataset
# Let's start by loading the Tesla dataset and preparing it for analysis. We will convert the 'Date' column to datetime format and set it as the index.


import pandas as pd
from datasets import load_dataset

# Load the Tesla dataset
dataset = load_dataset('codesignal/tsla-historic-prices')

# Convert the dataset into a DataFrame
tesla_df = pd.DataFrame(dataset['train'])

# Convert the 'Date' column to datetime format
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

# Set the 'Date' column as the index
tesla_df.set_index('Date', inplace=True)

# Calculating and Comparing SMA and EMA ------------------------------------------>>>>>>>
# We'll calculate the 20-day Simple Moving Average (SMA) and Exponential Moving Average (EMA) of the closing prices.

# Calculate the 20-day Simple Moving Average
tesla_df['SMA_20'] = tesla_df['Close'].rolling(window=20).mean()

# Calculate the 20-day Exponential Moving Average
tesla_df['EMA_20'] = tesla_df['Close'].ewm(span=20, adjust=False).mean()
# To make the visualization clearer, we'll focus on the year 2018.

# Using a smaller date range for better visualization
tesla_df_small = tesla_df.loc['2018']

# Plotting SMA and EMA for Comparison
# Finally, we will plot the closing prices along with the SMA and EMA to visualize and compare these indicators using Matplotlib.

import matplotlib.pyplot as plt

# Plotting
tesla_df_small[['Close', 'SMA_20', 'EMA_20']].plot(figsize=(12, 6), title="TSLA Close Price, SMA 20, and EMA 20 (2018)")
plt.show()


import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt

# Load and prepare the Tesla dataset
dataset = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(dataset['train'])
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
tesla_df.set_index('Date', inplace=True)

# Calculate the 20-day Simple Moving Average
tesla_df['SMA_20'] = tesla_df['Close'].rolling(window=20).mean()

# Calculate the 20-day Exponential Moving Average
tesla_df['EMA_20'] = tesla_df['Close'].ewm(span=20, adjust=False).mean()

# Using a smaller date range for better visualization
tesla_df_small = tesla_df.loc['2018']

# Plotting
tesla_df_small[['SMA_20', 'EMA_20']].plot(figsize=(12, 6), title="TSLA Close Price, SMA 20, and EMA 20 (2018)")
plt.show()


# Challenge ----------------------------------------------------------------------------------------------------->

import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset

# Step 1: Load and prepare the Tesla dataset
dataset = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(dataset['train'])
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
tesla_df.set_index('Date', inplace=True)

# Step 2: Calculate the 200-day SMA and EMA
# TODO: Calculate the 200-day SMA for the Volume
tesla_df['SMA_200'] = tesla_df['Volume'].rolling(window=200).mean()
# TODO: Calculate the 200-day EMA for the Volume
tesla_df['EMA_200'] = tesla_df['Volume'].ewm(span=200, adjust=False).mean()
# Step 3: Focus on data from the year 2018 for better visualization
tesla_df_small = tesla_df.loc['2018']

# Step 4: Plot the Volume along with SMA and EMA
plt.figure(figsize=(12, 6))
tesla_df_small[['Volume', 'SMA_200', 'EMA_200']].plot(title="TSLA Close Price, SMA 200, and EMA 200 (2018)")
plt.show()

#-------------------------------------------------------------------------------------------------------->>>>>>
import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt

# Load and prepare the Tesla dataset
dataset = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(dataset['train'])
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
tesla_df.set_index('Date', inplace=True)

# Calculate the 20-day Simple Moving Average (SMA)
tesla_df['SMA_20'] = tesla_df['Close'].rolling(window=20).mean()

# Calculate the 20-day Exponential Moving Average (EMA)
tesla_df['EMA_20'] = tesla_df['Close'].ewm(span=20, adjust=False).mean()

# Using a smaller date range for better visualization
tesla_df_small = tesla_df.loc['2018']

# Plotting
# TODO: Plot closing prices along with 20-day SMA and EMA
tesla_df_small[['Close', 'SMA_20', 'EMA_20']].plot(figsize=(12, 6),title="TSLA Closing Price, SMA 20, and EMA 20 (2018)")
plt.show()

# Applying Technical Indicators to Identify Trends using Tesla's ($TSLA) stock data. 
#  You will revisit how to calculate Simple Moving Averages (SMAs), and learn how to identify trend signals
# like Golden Cross and Death Cross, and visualize these trends using pandas and matplotlib.

# Lesson Goal: To understand and implement technical indicators (SMA) and identify trend signals (Golden Cross and Death Cross) in financial data using Python and Pandas.

# Lesson Plan:

# Loading and Preparing Tesla Stock Data
# Calculating Simple Moving Averages (SMAs)
# Identifying Golden Cross and Death Cross
# Visualizing the Results

import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset

# Load the Tesla dataset
dataset = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(dataset['train'])

# Convert 'Date' column to datetime format and set it as the index
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
tesla_df.set_index('Date', inplace=True)
Explanation:

# Import Libraries: We import pandas for data manipulation, matplotlib.pyplot for plotting, and load_dataset to fetch our Tesla stock data.
# Dataset: We use load_dataset to fetch the dataset and convert it to a DataFrame.
# Convert Date Column: The Date column is converted to datetime format for easier manipulation.
# Set Index: We set the Date column as the index to efficiently perform time series operations.
# Calculate 50-day and 200-day SMAs

tesla_df['SMA_50'] = tesla_df['Close'].rolling(window=50).mean()
tesla_df['SMA_200'] = tesla_df['Close'].rolling(window=200).mean()

# SMA_50: We calculate the 50-day SMA by using the rolling method with a window of 50 days on the 'Close' price and then applying the mean function.
# SMA_200: Similarly, we calculate the 200-day SMA by using a rolling window of 200 days.


# --------------------------------------------------------->Identifying Golden Cross and Death Cross<_---------------------------------------------------
# In trading, golden and death crosses are defined as follows:

# Golden Cross: Occurs when a short-term SMA (50-day) crosses above a long-term SMA (200-day), indicating a potential upward trend.
# Death Cross: Occurs when a short-term SMA (50-day) crosses below a long-term SMA (200-day), indicating a potential downward trend.
# Now, let's create signals for these crossover points:

# Identifying the "Golden Cross" and "Death Cross"
tesla_df['Signal'] = 0  # Default value
tesla_df.loc[tesla_df['SMA_50'] > tesla_df['SMA_200'], 'Signal'] = 1
tesla_df.loc[tesla_df['SMA_50'] < tesla_df['SMA_200'], 'Signal'] = -1

# Creating a column to mark crossover points
tesla_df['Crossover'] = tesla_df['Signal'].diff()

# Explanation:

# Signal Column: We create a 'Signal' column to store initial values as 0.
# Golden Cross Signal: When the 50-day SMA crosses above the 200-day SMA, we set the 'Signal' to 1.
# Death Cross Signal: When the 50-day SMA crosses below the 200-day SMA, we set the 'Signal' to -1.
# Crossover Column: We create a 'Crossover' column to store the points where the signal changes (differs from the previous day), indicating a crossover event.

import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset

# Load the Tesla dataset
dataset = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(dataset['train'])

# Convert 'Date' column to datetime format and set it as the index
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
tesla_df.set_index('Date', inplace=True)

# Calculate 50-day and 200-day SMAs
tesla_df['SMA_20'] = tesla_df['Close'].rolling(window=20).mean()
tesla_df['SMA_50'] = tesla_df['Close'].rolling(window=50).mean()

# Identifying the "Golden Cross" and "Death Cross"
tesla_df['Signal'] = 0  # Default value
tesla_df.loc[tesla_df['SMA_20'] > tesla_df['SMA_50'], 'Signal'] = 1
tesla_df.loc[tesla_df['SMA_20'] < tesla_df['SMA_50'], 'Signal'] = -1

# Creating a column to mark crossover points
tesla_df['Crossover'] = tesla_df['Signal'].diff()

# Using a smaller date range for better visualization
tesla_df_small = tesla_df.loc['2019']

# Plot with Golden Cross and Death Cross
fig, ax = plt.subplots(figsize=(12, 6))
tesla_df_small[['Close', 'SMA_20', 'SMA_50']].plot(ax=ax, title="TSLA with Golden Cross and Death Cross (2019)")

# Highlighting Golden Cross and Death Cross points
crosses = tesla_df_small[tesla_df_small['Crossover'] != 0]
for idx, row in crosses.iterrows():
    if row['Crossover'] == 2:
        plt.plot(idx, row['SMA_20'], 'go', markersize=10, label='Golden Cross' if 'Golden Cross' not in [text.get_text() for text in ax.get_legend().get_texts()] else "")
    elif row['Crossover'] == -2:
        plt.plot(idx, row['SMA_20'], 'ro', markersize=10, label='Death Cross' if 'Death Cross' not in [text.get_text() for text in ax.get_legend().get_texts()] else "")

plt.legend()
plt.show()

#------------------------------------------------------------------------------------------------------------------>>>>>>>>>>>>>
import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset

# Load the Tesla dataset
dataset = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(dataset['train'])

# Convert 'Date' column to datetime format and set it as the index
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
tesla_df.set_index('Date', inplace=True)

# TODO: Calculate 20-day and 50-day SMAs for the 'Volume' column using rolling mean
tesla_df['SMA_20'] = tesla_df['Volume'].rolling(window=20).mean()
tesla_df['SMA_50'] = tesla_df['Volume'].rolling(window=50).mean()
# TODO: Identify the "Golden Cross" and "Death Cross" for Volume
tesla_df['Signal'] = 0
tesla_df.loc[tesla_df['SMA_20'] > tesla_df['SMA_50'], 'Signal'] = 1
tesla_df.loc[tesla_df['SMA_20'] < tesla_df['SMA_50'], 'Signal'] = -1
tesla_df['Crossover'] = tesla_df['Signal'].diff()
# TODO: Filter the DataFrame for the year 2019
tesla_df_small = tesla_df.loc['2019']
# TODO: Plot the SMAs along with Volume
fig, ax = plt.subplots(figsize=(12,6))
tesla_df_small[['Volume', 'SMA_20', 'SMA_50']].plot(ax=ax, title="TSLA Volume, SMA 20 & SMA 50 (2019)")
# TODO: Highlight the Golden Cross and Death Cross points
crosses = tesla_df_small[tesla_df_small['Crossover'] != 0]
for idx, row in crosses.iterrows():
    if row['Crossover'] == 2:
        plt.plot(idx, row['SMA_20'], 'go', markersize=10, label='Golden Cross' if 'Golden Cross' not in [text.get_text() for text in ax.get_legend().get_texts()] else "")
    elif row['Crossover'] == -2:
        plt.plot(idx, row['SMA_50'], 'ro', markersize=10, label='Death Cross' if 'Death Cross' not in [text.get_text() for text in ax.get_legend().get_texts()] else"")
        

plt.show()

#------------------------------------------------------------------------------------------------------------------------------------------------------------->>>>>>>>>
# Concept and calculation of Volume Weighted Average Price (VWAP) specifically for Tesla ($TSLA) stock data using Pandas. 
# VWAP is a crucial indicator in trading that helps by providing the average price a security has traded at during the day, 
# weighted by volume. By the end of this lesson, you'll be able to calculate VWAP and visualize it alongside the closing prices of Tesla stock data.

# Introduction to VWAP
# Volume Weighted Average Price (VWAP) is a trading benchmark that gives traders insight into both the price and volume of trades for a particular stock. 
# It represents the average price a stock has traded at throughout the day, weighted by volume.

# VWAP is used by traders to identify the average price at which a stock was traded over a given period, reflecting both the price and the traded volume. 
# It helps in determining the efficiency of stock execution by comparing it against the market's average.

# The VWAP is calculated using the cumulative sum (the running total) of the volume and the volume-weighted prices:

# VWAP=∑i=1n(Pi×Vi)
#         --------
#         ∑=1nVi
# Where Pi is the price of the stock, and Vi is the volume of trades at each i-th period.

# Loading and Preprocessing Tesla Stock Data
# Let's start by importing the necessary libraries and loading the Tesla ($TSLA) stock data. We'll use the load_dataset function from the datasets library.

import pandas as pd
import numpy as np
from datasets import load_dataset

# Load Tesla dataset
dataset = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(dataset['train'])

# Next, we'll preprocess the data by converting the 'Date' column to datetime format and setting it as the index.
# Convert Date column to datetime format and set as index
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
tesla_df.set_index('Date', inplace=True)

# For better visualization, we'll filter the data to focus on the year 2018.
# Filter data for the year 2018
tesla_df_small = tesla_df.loc['2018'].copy()

# Calculating the VWAP --------------------------------------------------------------------------------------------------------->>>>>
# Now that we have our data preprocessed, we can calculate the VWAP. 
# We'll use the cumulative sum (the running total, where each value is added to the sum of previous values) 
# of the product of volume and close price and then divide it by the cumulative sum of the volume.

# Visualizing VWAP with Closing Prices
# Visualization helps in interpreting the financial data more effectively. We'll use Matplotlib to plot the VWAP alongside the closing prices.

import matplotlib.pyplot as plt

# Visualize VWAP with Close Price
tesla_df_small[['Close', 'VWAP']].plot(figsize=(12, 6), title="TSLA Close Price and VWAP (2018)")
plt.show()

# How to calculate and visualize the Volume Weighted Average Price (VWAP) for Tesla stock data using Pandas. 
# We covered the importance of VWAP, loaded and preprocessed the data, performed the VWAP calculation, and created a visualization.


# _______________________________________________________________________________________________________________________
# Introduction to Feature Engineering
# Feature engineering involves creating new input variables (features) from raw data to improve the performance of machine learning models. This process is especially vital in financial markets, where capturing the correct patterns and relationships can significantly impact trading decisions.

# For example, features like price differences, volatility, and moving averages can reveal underlying patterns in stock movements, aiding in more accurate predictions.

# By the end of this lesson, you will understand how to generate meaningful features from stock data, setting a strong foundation for more advanced machine-learning techniques in trading.

Loading Financial Data using Pandas
First, let's load our Tesla stock dataset using Pandas. Using Pandas is essential for handling financial data efficiently, enabling us to load, manipulate, and analyze large datasets with ease.

We'll be using the datasets library to import our dataset. Here's how you can load the dataset and convert it into a Pandas DataFrame:


import pandas as pd
import datasets

# Load the dataset
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])
print(tesla_df.head())
Executing the above code will load the Tesla stock data into a DataFrame called tesla_df. The DataFrame looks like this:

Plain text
Copy to clipboard
         Date      Open      High       Low     Close  Adj Close     Volume
0  2010-06-29  1.266667  1.666667  1.169333  1.592667   1.592667  281494500
1  2010-06-30  1.719333  2.028000  1.553333  1.588667   1.588667  257806500
2  2010-07-01  1.666667  1.728000  1.351333  1.464000   1.464000  123282000
3  2010-07-02  1.533333  1.540000  1.247333  1.280000   1.280000   77097000
4  2010-07-06  1.333333  1.333333  1.055333  1.074000   1.074000  103003500
Our dataset includes columns like 'Open', 'High', 'Low', and 'Close', representing the stock's opening, highest, lowest, and closing prices for each day. Here’s a brief description:

Open: The price at which the stock opened.
High: The highest price reached during the trading day.
Low: The lowest price reached during the trading day.
Close: The price at which the stock closed.

# Creating New Features
# Now, let's create new features from our existing data. We'll generate two new features: High-Low and Price-Open.

# The High-Low feature represents the price range of the stock for each day. It is calculated as the difference between the highest and lowest prices. This feature can be useful to gauge the daily volatility of the stock.

# Creating the High-Low feature
tesla_df['High-Low'] = tesla_df['High'] - tesla_df['Low']
The Price-Open feature represents the difference between the closing and opening prices of the stock for each day. This feature indicates how much the price has moved from the start to the end of the trading day, which is another valuable indicator.

# Creating the Price-Open feature
tesla_df['Price-Open'] = tesla_df['Close'] - tesla_df['Open']

Inspecting and Verifying Features
Let’s inspect the new features we’ve created to ensure they are correct and understand their potential usefulness.

We can use the Pandas head() function to display the first few rows of our newly created features:

# Displaying the new features
print(tesla_df[['High-Low', 'Price-Open']].head())
The output of the above code will be:

Plain text
Copy to clipboard
   High-Low  Price-Open
0  0.497334    0.326000
1  0.474667   -0.130666
2  0.376667   -0.202667
3  0.292667   -0.253333
4  0.278000   -0.259333
# This output demonstrates our newly calculated features for the Tesla stock data. The High-Low column indicates the range between the highest and lowest stock prices each day, serving as a measure of volatility. The Price-Open column shows the difference between the closing and opening prices, providing insight into daily price movement.

# High-Low: A value of 4.50 means the highest price was $4.50 more than the lowest price for that day, indicating the daily range.
# Price-Open: A value of 0.30 means the closing price was $0.30 higher than the opening price, showing how much the stock rose during that day.
import pandas as pd
import datasets

# Load the dataset
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])

# Creating the High-Low feature
tesla_df['High-Low'] = tesla_df['High'] - tesla_df['Low']

# Creating a new feature
tesla_df['Daily Change'] = tesla_df['Close'] - tesla_df['Open']
# Displaying the new features
print(tesla_df[['High-Low', 'Daily Change']].head())

import pandas as pd
import datasets

# Load the dataset
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])

# TODO: Create the Daily Range Percentage feature (what's the percentage of the highest daily price from the lowest)
tesla_df['Daily Range %'] = ((tesla_df['High'] - tesla_df['Low'])  / tesla_df['Low']) * 100

# Creating the Price Change Percentage feature
tesla_df['Price Change %'] = (tesla_df['Close'] - tesla_df['Open']) / tesla_df['Open'] * 100

# TODO: Display the new features of the Tesla dataset
print(tesla_df[['Daily Range %','Price Change %']].head())

import pandas as pd
import datasets

# TODO: Load the dataset 'codesignal/tsla-historic-prices' and transform it into a DataFrame
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])
# TODO: Create the Close-Low feature (Close price minus Low price)
tesla_df['Close-Low'] = tesla_df['Close'] - tesla_df['Low']
# TODO: Create the Adj-Open feature (Adj Close price minus Open price)
tesla_df['Adj-Open'] = tesla_df['Adj Close'] - tesla_df['Open']
# TODO: Print the first 5 rows of the new features 'Close-Low' and 'Adj-Open'
print(tesla_df[['Close-Low', 'Adj-Open']].head())

# How to standardize financial data using the StandardScaler from the sklearn library. Scaling features ensure that 
# all data contribute equally to machine learning models, improving their performance and robustness.

# Revision: Loading and Preprocessing the Dataset
# Let's quickly recall how to load and preprocess the Tesla stock dataset:

import pandas as pd
import datasets

# Load the dataset
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])

# Feature Engineering: creating new features
tesla_df['High-Low'] = tesla_df['High'] - tesla_df['Low']
tesla_df['Price-Open'] = tesla_df['Close'] - tesla_df['Open']
# We've successfully loaded the Tesla dataset and created new features: High-Low and Price-Open.

# Introduction to Feature Scaling
# Feature scaling is crucial for machine learning for several reasons:

# Equal Contribution: Ensures all features contribute equally to the model.
# Improved Convergence: Helps in faster convergence during model training by making gradients less sensitive to feature magnitude.
# Prevent Dominance: Prevents features with larger scales from dominating those with smaller scales.
# Feature scaling is particularly useful in scenarios like:

# Predicting House Prices: Square footage in thousands vs. the number of bedrooms in single digits.
# Stock Market Analysis: Stock price in hundreds vs. trading volume in millions.
# Health Data: Age in the 0-100 range vs. blood pressure in the hundreds.
# Retail Sales Prediction: Number of items sold vs. store rating in single digits.
# These examples highlight the importance of scaling to ensure uniform treatment of features, thereby enhancing model performance.

# Defining Standardization
# Standardization involves transforming your data so that the mean of each feature is 0 and the standard deviation is 1. 
# This process ensures all features on the same scale, improving the performance and robustness of machine learning models. 
# The formula for standardization is:

z=(x−μ)/σ

​# where:


z is the standardized value,

x is the original value,

μ is the mean of the feature, calculated as the average of all values of that feature,

σ is the standard deviation of the feature, which measures the amount of variation or dispersion of the values.

# By applying this formula, each feature will have a mean of 0 and a standard deviation of 1, enabling more stable and 
# faster convergence during the training of machine learning models.

# Implementing StandardScaler on Financial Data
# Let's proceed to scale our features using StandardScaler from sklearn. The StandardScaler standardizes features by removing the mean and scaling to unit variance.

# First, we define our features:


from sklearn.preprocessing import StandardScaler

# Defining features
features = tesla_df[['High-Low', 'Price-Open', 'Volume']].values
# Now, let's initialize the scaler and apply it to our features:


# Scaling
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
# Here, fit_transform computes the mean and standard deviation to scale the data and then returns the transformed version.

# Inspecting Scaled Features
# It's essential to inspect and validate the scaled features to ensure they have been correctly normalized. Let's display the first few rows of the scaled features:

# Displaying the first few scaled features
print("Scaled features (first 5 rows):\n", features_scaled[:5])
# The output of the above code will be:


Scaled features (first 5 rows):
 [[-0.48165383  0.08560547  2.29693712]
 [-0.48579183 -0.02912844  2.00292929]
 [-0.50368231 -0.04721815  0.33325453]
 [-0.51901702 -0.0599476  -0.23997882]
 [-0.52169457 -0.06145506  0.08156432]]

# This output demonstrates that our features have been successfully scaled to have a standardized scale, 
# specifically with mean values hovering around 0 and standard deviation about 1. This scaling ensures equality in feature contribution to the machine learning model.
# Validating Scaled Features
# After scaling your features, it's important to check the mean and standard deviation to ensure they are correctly standardized. 
# You can do this using the following code:

# Checking mean values and standard deviations of scaled features
scaled_means = features_scaled.mean(axis=0)
scaled_stds = features_scaled.std(axis=0)

print("\nMean values of scaled features:", scaled_means)
print("Standard deviations of scaled features:", scaled_stds)
# The output will show that the means are close to 0 and the standard deviations are close to 1:

Mean values of scaled features: [ 3.39667875e-17  5.57267607e-18 -6.79335750e-17]
Standard deviations of scaled features: [1. 1. 1.]
This validation confirms that your features have been successfully scaled.

import pandas as pd
import datasets
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])

# Feature Engineering: creating new features
tesla_df['High-Low'] = tesla_df['High'] - tesla_df['Low']
tesla_df['Price-Open'] = tesla_df['Close'] - tesla_df['Open']

# Defining features
features = tesla_df[['High-Low', 'Price-Open', 'Volume']].values

# Scaling
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Displaying the first few scaled features
print("Scaled features (first 5 rows):\n", features_scaled[:5])

# Checking mean values and standard deviations of scaled features
scaled_means = features_scaled.mean(axis=0)
scaled_stds = features_scaled.std(axis=0)

print("\nMean values of scaled features:", scaled_means)
print("Standard deviations of scaled features:", scaled_stds)

# Problem

# Modify our code to scale only the Volume feature using StandardScaler and include this scaled feature in our dataset as a new column Volume_Scaled. 

import pandas as pd
import datasets
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])

# Feature Engineering: creating new features
tesla_df['High-Low'] = tesla_df['High'] - tesla_df['Low']
tesla_df['Price-Open'] = tesla_df['Close'] - tesla_df['Open']

# Scaling only the 'volume' feature
scaler = StandardScaler()
tesla_df['Volume_Scaled'] = scaler.fit_transform(tesla_df[['Volume']])

# Defining features # Update features to include 'Volume_Scaled'
features = tesla_df[['High-Low', 'Price-Open', 'Volume_Scaled']].values

# Displaying the first few scaled features
print("Scaled features (first 5 rows):\n", tesla_df[['High-Low','Price-Open', 'Volume_Scaled' ]].head())

# Checking mean values and standard deviations of scaled features
scaled_means = tesla_df[['High-Low', 'Price-Open', 'Volume_Scaled']].mean(axis=0)
scaled_stds = tesla_df[['High-Low', 'Price-Open', 'Volume_Scaled']].std(axis=0)

print("\nMean values of scaled features:", scaled_means)
print("Standard deviations of scaled features:", scaled_stds)

# TASK
# Add the missing lines to properly scale the features using StandardScaler and validate that the scaling is correct.

import pandas as pd
from sklearn.preprocessing import StandardScaler
import datasets

# Load the dataset
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])

# Feature Engineering: creating new features
tesla_df['High-Low'] = tesla_df['High'] - tesla_df['Low']
tesla_df['Price-Open'] = tesla_df['Close'] - tesla_df['Open']

# Defining features
features =  tesla_df[['High-Low', 'Price-Open']].values
# Features include new columns and 'Volume' column
features = tesla_df[['High-Low', 'Price-Open', 'Volume']].values

# TODO: Initialize the StandardScaler and scale the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Displaying the first few scaled features
print("Scaled features (first 5 rows):\n", features_scaled[:5])

# Checking mean values and standard deviations of scaled features
scaled_means = features_scaled.mean(axis=0)
scaled_stds = features_scaled.std(axis=0)

print("\nMean values of scaled features:", scaled_means)
print("Standard deviations of scaled features:", scaled_stds)


# Fill in the missing pieces of code to scale the features correctly using StandardScaler and display the first few rows of the scaled features.
import pandas as pd
from sklearn.preprocessing import StandardScaler
import datasets

# Load the Tesla stock dataset
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])

# Feature Engineering: creating new features
# TODO: Create a new feature with a value corresponding to a daily price change
tesla_df['Daily_Change'] = tesla_df['Close'] - tesla_df['Open']
# TODO: Create a new feature with a value equals to mean price during the day
tesla_df['Mean_Price'] = (tesla_df['High'] + tesla_df['Low']) /2

# Defining features
features = tesla_df[['Daily_Change', 'Mean_Price', 'Volume', 'Open']].values

# Scaling the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Displaying the first few scaled features
print("Scaled features (first 5 rows):\n", features_scaled[:5])

# TODO: Check mean values and standard deviations of scaled features
scaled_means = features_scaled.mean(axis=0)
scaled_stds = features_scaled.std(axis=0)

print("\nMean values of scaled features:", scaled_means)
print("Standard deviations of scaled features:", scaled_stds)


# Load the Tesla dataset, create new features, scale them with StandardScaler, and validate the scaled features. Follow the TODOs to complete the implementation.
import pandas as pd
import datasets
from sklearn.preprocessing import StandardScaler

# TODO: Load the Tesla dataset using `datasets.load_dataset`
data = datasets.load_dataset('codesignal/tsla-historic-prices')
# TODO: Convert the dataset to a pandas DataFrame
tesla_df = pd.DataFrame(data['train'])

# TODO: Create new features: 'Volatility' and 'Daily_Average'
# Volatility represents the price fluctuation daily range relative to the opening price.
tesla_df['Volatility'] = (tesla_df['High'] - tesla_df['Low']) / tesla_df['Open']
# Daily_Average represents the average of the daily high and low prices.
tesla_df['Daily_Average'] = (tesla_df['High'] - tesla_df['Low']) / 2

# TODO: Define the features from the DataFrame
# The features will include Volatility, Daily_Average, and Volume
features = tesla_df[['Volatility', 'Daily_Average', 'Volume']].values
# TODO: Initialize the StandardScaler and scale the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
# TODO: Print the first 5 rows of the scaled features
print("Scaled features (first 5 rows):n", features_scaled[:5])
# TODO: Check and print the mean values and standard deviations of the scaled features
scaled_means = features_scaled.mean(axis=0)
scaled_stds = features_scaled.std(axis=0)

print("Standard deviations of scaled features:", scaled_stds)

## learn how to split a dataset into training and testing sets. This is a crucial step in preparing your data for machine learning models 
## to ensure they generalize well to unseen data.
# Revision of Preprocessing Steps
# Before we delve into splitting the dataset, let's briefly review the preprocessing steps we have covered so far. 
# The dataset has been loaded, new features have been engineered, and the features have been scaled.

# Here's the code for those steps for a quick revision:


import pandas as pd
from sklearn.preprocessing import StandardScaler
import datasets

# Loading and preprocessing the dataset (revision)
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])
tesla_df['High-Low'] = tesla_df['High'] - tesla_df['Low']
tesla_df['Price-Open'] = tesla_df['Close'] - tesla_df['Open']

# Defining features and target
features = tesla_df[['High-Low', 'Price-Open', 'Volume']].values
# Target is the column that we are trying to predict
target = tesla_df['Close'].values

# Scaling
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Understanding the Importance of Splitting Datasets
# To avoid overfitting, where a model learns the training data too well and performs poorly on new, unseen data, 
# it's important to evaluate your machine learning model on data it has never seen before. This is where splitting datasets into training and testing sets comes into play.

# Why Split?

# Training Set: Used to train the machine learning model.
# Testing Set: Used to evaluate the model's performance and check its ability to generalize to unseen data.
# This ensures that your model's performance is not just tailored to the training data but can be generalized to new inputs.



# Implementing Dataset Split with 'train_test_split'
# The train_test_split function from sklearn.model_selection helps us easily split the data.

#  -----------------------------------------------Parameters of train_test_split:

# test_size: The proportion of the dataset to include in the test split (e.g., 0.25 means 25% of the data will be used for testing).
# train_size: The proportion of the dataset to include in the train split (optional if test_size is provided).
# random_state: Controls the shuffling applied to the data before the split. Providing a fixed value ensures reproducibility.
# Let's split our scaled features and targets into training and testing sets:


from sklearn.model_selection import train_test_split

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.25, random_state=42)

# The train_test_split function will split our dataset into training and testing sets:

#  features_scaled and target are the inputs.
#  test_size=0.25 means 25% of the data goes to the test set.
#  random_state=42 ensures reproducibility. The state can be any other number, too.

# Verifying Shapes and Contents of the Split Data
# After splitting the dataset, it's important to verify the shapes and the contents of the resulting sets to ensure the split was done correctly.

# Checking Shapes:

# Print the shapes of the training and testing sets to confirm the split ratio is as expected.
# Inspecting Sample Rows:

# Print a few rows of the training and testing sets to visually inspect the data.
# Let's check our split data:

# Verify splits
print(f"Training features shape: {X_train.shape}")
print(f"Testing features shape: {X_test.shape}")

print(f"First 5 rows of training features: \n{X_train[:5]}")
print(f"First 5 training targets: {y_train[:5]}\n")

print(f"First 5 rows of testing features: \n{X_test[:5]}")
print(f"First 5 testing targets: {y_test[:5]}")


# The output of the above code will be:


Training features shape: (2510, 3)
Testing features shape: (837, 3)
First 5 rows of training features: 
[[-4.66075964e-01  6.80184955e-02  3.11378946e-01]
 [ 4.01701510e+00  5.04529577e+00 -4.61555718e-02]
 [ 2.04723437e+00  3.09900603e+00  9.43022378e-04]
 [-5.30579018e-01 -2.30986178e-02 -5.67163058e-01]
 [-4.78854883e-01 -5.79376618e-02 -6.94451021e-01]]
First 5 training targets: [ 17.288    355.666656 222.419998  15.000667  13.092   ]

First 5 rows of testing features: 
[[-0.36226203  0.2087143   0.69346624]
 [ 1.27319589  1.04049732  0.58204785]
 [-0.53556882 -0.03231093 -0.86874821]
 [-0.49029475  0.07773304 -0.51784526]
 [ 3.0026057  -4.41816938 -0.31923731]]
First 5 testing targets: [ 23.209333 189.606674  14.730667  16.763332 325.733337]

# This output confirms that our dataset has been successfully split into training and testing sets, showing the shape of each set 
# and giving us a glimpse into the rows of our features and targets post-split. It's an important validation step to ensure our 
# data is ready for machine learning model training and evaluation.


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import datasets

# Load the dataset
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])

# Create new features
tesla_df['High-Low'] = tesla_df['High'] - tesla_df['Low']
tesla_df['Price-Open'] = tesla_df['Close'] - tesla_df['Open']

# Define features and target
features = tesla_df[['High-Low', 'Price-Open', 'Volume']].values
target = tesla_df['Close'].values

# Scale the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.25, random_state=42)

# Verify splits
print(f"Training features shape: {X_train.shape}")
print(f"Testing features shape: {X_test.shape}")

print(f"First 5 rows of training features: \n{X_train[:5]}")
print(f"First 5 training targets: {y_train[:5]}\n")

print(f"First 5 rows of testing features: \n{X_test[:5]}")
print(f"First 5 testing targets: {y_test[:5]}")

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import datasets

# TODO: Load the dataset 'codesignal/tsla-historic-prices' and convert it to a DataFrame
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])
# TODO: Create new features 'SMA20' (20-day Simple Moving Average) and 'EMA20' (20-day Exponential Moving Average)
tesla_df['SMA20'] = tesla_df['Close'].rolling(window=20).mean()
tesla_df['EMA20'] = tesla_df['Close'].ewm(span=20,).mean()
# TODO: Drop NaN values that were created by moving average
tesla_df.dropna(inplace=True)
# TODO: Define features and target
# `features` include SMA20, EMA20, and Volume, `target` includes Close prices
features = tesla_df[['SMA20', 'EMA20', 'Volume']]
target = tesla_df['Close']
# TODO: Scale features using StandardScaler
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
# TODO: Split the dataset into training and testing sets using train_test_split
X_train, X_test, y_train, y_test = train_test_split(scaled_features, target, test_size=0.25, random_state=42)
# TODO: Verify splits by printing shapes and sample rows of training and testing sets
print("Training Features Shape:", X_train.shape)
print("Testing Features Shape:", X_test.shape)
print("Training Target Shape:", y_train.shape)
print("Testing Target Shape:", y_test.shape)
print("Sample Training Features:\n", X_train[:5])
print("Sample Training Target:\n", y_train[:5])

# How to partition your dataset correctly using TimeSeriesSplit from the sklearn.model_selection library.

# Introduction to Data Leakage in Time Series
# Data leakage occurs when information from outside the training dataset inadvertently makes its way into the model. 
# This is particularly problematic in time series data, where the natural temporal ordering is crucial. Data leakage 
# can lead to overestimation of a model's performance because it allows information from the future to be used in making predictions about the past.

# When dealing with stock market data, using future prices to predict past prices would artificially inflate a model's accuracy 
# and yield unreliable predictions for actual trading strategies. Hence, it's important to ensure that our training and testing 
# sets are separated in a way that respects the temporal nature of the data.

Revisiting Feature Engineering and Scaling (Revision)
Let's quickly revise how to engineer features and scale them. These steps are foundational for preparing your data for machine learning models.


import pandas as pd
import datasets
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])

# Feature Engineering: creating new features
tesla_df['High-Low'] = tesla_df['High'] - tesla_df['Low']
tesla_df['Price-Open'] = tesla_df['Close'] - tesla_df['Open']

# Defining features and target
features = tesla_df[['High-Low', 'Price-Open', 'Volume']].values
target = tesla_df['Close'].values

# Scaling
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
In this snippet, we create two new features, High-Low and Price-Open, and scale these features using StandardScaler.


# Correctly Splitting Time Series Data
# To avoid data leakage in time series, we need to split our data so that future data points are not used to predict past data points. 
         # TimeSeriesSplit from the sklearn.model_selection library helps achieve this.

# The TimeSeriesSplit class helps you create train/test splits that respect the temporal order of your data. One of the key arguments in 
         # TimeSeriesSplit is n_splits, which specifies the number of re-shuffling and splitting iterations. Essentially, 
         # this determines how many different train/test splits will be generated from your data.

from sklearn.model_selection import TimeSeriesSplit

# Initiate TimeSeriesSplit
tscv = TimeSeriesSplit(n_splits=3)

# Splitting with TimeSeriesSplit
for fold, (train_index, test_index) in enumerate(tscv.split(features_scaled)):
    print(f"Fold {fold + 1}")
    print(f"TRAIN indices (first 5): {train_index[:5]}, TEST indices (first 5): {test_index[:5]}")
    
    # Splitting the features and target
    X_train, X_test = features_scaled[train_index], features_scaled[test_index]
    y_train, y_test = target[train_index], target[test_index]
    
    # Print a small sample of the data
    print(f"X_train sample:\n {X_train[:2]}")
    print(f"y_train sample:\n {y_train[:2]}")
    print(f"X_test sample:\n {X_test[:2]}")
    print(f"y_test sample:\n {y_test[:2]}")
    print("-" * 10)


# To elaborate, TimeSeriesSplit generates indices for multiple train/test splits, where the training set for each split 
# consists of all data points up to a specific point in time, and the test set includes the subsequent data points in time. 
# This sequential process respects the chronological order of the data. As a result, no future data points are included in 
# the training set of any fold, which effectively prevents data leakage. This method ensures that our model training and 
# evaluation simulate real-world scenarios more accurately, thereby providing reliable performance metrics.

Analyzing Fold Results
Let's analyze the output from each fold to ensure correct data splitting. The output of the above code will be:


Fold 1
TRAIN indices (first 5): [0 1 2 3 4], TEST indices (first 5): [839 840 841 842 843]
X_train sample:
 [[-0.48165383  0.08560547  2.29693712]
 [-0.48579183 -0.02912844  2.00292929]]
y_train sample:
 [1.592667 1.588667]
X_test sample:
 [[-0.4714307  -0.11890593  0.26304787]
 [-0.42092366  0.03234206  1.43036618]]
y_test sample:
 [10.857333 10.964667]
----------
Fold 2
TRAIN indices (first 5): [0 1 2 3 4], TEST indices (first 5): [1675 1676 1677 1678 1679]
X_train sample:
 [[-0.48165383  0.08560547  2.29693712]
 [-0.48579183 -0.02912844  2.00292929]]
y_train sample:
 [1.592667 1.588667]
X_test sample:
 [[-0.46169462 -0.13046308  1.57995793]
 [-0.47447336  0.07639316  0.32446706]]
y_test sample:
 [17.066    17.133333]
----------
Fold 3
TRAIN indices (first 5): [0 1 2 3 4], TEST indices (first 5): [2511 2512 2513 2514 2515]
X_train sample:
 [[-0.48165383  0.08560547  2.29693712]
 [-0.48579183 -0.02912844  2.00292929]]
y_train sample:
 [1.592667 1.588667]
X_test sample:
 [[-0.27268857 -0.19528365  0.41906266]
 [-0.34291165 -0.09059793 -0.01236106]]
y_test sample:
 [66.726669 66.288002]
----------
This output confirms the correct operation of TimeSeriesSplit, showing how each set of training and testing indices progresses through the data without overlap, respecting the temporal order. This ensures that no future data is used when training the model.


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import TimeSeriesSplit
from datasets import load_dataset

# Load Tesla stock data
dataset = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(dataset['train'])

# Feature Engineering
tesla_df['High-Low'] = tesla_df['High'] - tesla_df['Low']
tesla_df['Price-Open'] = tesla_df['Close'] - tesla_df['Open']

# Define features and target
features = tesla_df[['High-Low', 'Price-Open', 'Volume']].values
target = tesla_df['Close'].values

# TODO: Create a TimeSeriesSplit instance and fill in the gaps in the next lines
tscv = TimeSeriesSplit(n_splits=3)
for fold, (train_index, test_index) in enumerate(tscv.split(features)):
    print(f"Fold {fold + 1}")
    print(f"TRAIN indices (first & last 5): {train_index[:5]}, {train_index[-5:]}")
    print(f"TEST indices (first 5): {test_index[:5]}")
    
    # Splitting the features and target
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = target[train_index], target[test_index]
    
    # TODO: Create a scaler for each fold
    # to prevent data leakage and fit the training data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    # TODO: Use the fitted scaler to transform the test data
    X_test_scaled = scaler.transform(X_test)
    
    # Print a small sample of the data
    print(f"X_train sample:\n {X_train_scaled[:2]}")
    print(f"y_train sample:\n {y_train[:2]}")
    print(f"X_test sample:\n {X_test_scaled[:2]}")
    print(f"y_test sample:\n {y_test[:2]}")
    print("-" * 10)



import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import TimeSeriesSplit
from datasets import load_dataset

# Load the dataset
tesla_df = load_dataset('codesignal/tsla-historic-prices', split='train').to_pandas()

# Feature Engineering: creating new features
tesla_df['High-Low'] = tesla_df['High'] - tesla_df['Low']
tesla_df['Price-Open'] = tesla_df['Close'] - tesla_df['Open']

# Defining features and target
features = tesla_df[['High-Low', 'Price-Open', 'Volume']].values
target = tesla_df['Close'].values

# TODO: Scale the features using StandardScaler
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
# Initiate TimeSeriesSplit
tscv = TimeSeriesSplit(n_splits=3)

# Splitting with TimeSeriesSplit
for fold, (train_index, test_index) in enumerate(tscv.split(features_scaled)):
    print(f"Fold {fold + 1}")
    print(f"TRAIN indices (first 5): {train_index[:5]}, TEST indices (first 5): {test_index[:5]}")
    
    # TODO: Split into features and target
    X_train, X_test = features_scaled[train_index], features_scaled[test_index]
    y_train, y_test = target[train_index], target[test_index]
    
    
    # Print a small sample of the data
    print(f"X_train sample:\n {X_train[:2]}")
    print(f"y_train sample:\n {y_train[:2]}")
    print(f"X_test sample:\n {X_test[:2]}")
    print(f"y_test sample:\n {y_test[:2]}")
    print("-" * 10)



import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import TimeSeriesSplit
import datasets

# TODO: Load the dataset 'codesignal/tsla-historic-prices' using `datasets` library and convert to a DataFrame
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])
# TODO: Engineer new features such as 'Moving_Average_10' and 'Returns'
# 'Moving_Average_10' is a 10-day SMA
# 'Returns' is the difference between the closing price and the open price
tesla_df['SMA10'] = tesla_df['Close'].rolling(window=10).mean()
tesla_df['Returns'] = tesla_df['Close'] - tesla_df['Open']

# TODO: Define features arrays with 'Moving_Average_10', 'Returns', and 'Volume', and the target array as 'Close'
features = tesla_df[['SMA10', 'Returns', 'Volume']]
target = tesla_df['Close']
# TODO: Scale the features using StandardScaler
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
# TODO: Initiate TimeSeriesSplit with 3 splits and print indices and samples for each fold
tscv = TimeSeriesSplit(n_splits=3)

for fold, (train_index, test_index) in enumerate(tscv.split(features_scaled)):
    print(f"Fold {fold +1}")
    print(f"TRAIN indices (first 5): {train_index[:5]}, TEST indices (first 5): {test_index[:5]}")
    
    X_train, X_test = features_scaled[train_index], features_scaled[test_index]
    y_train, y_test = target[train_index], target[test_index]
    
    print(f"X_train sample:\n {X_train[:2]}")
    print(f"y_train sample:\n {y_train[:2]}")
    print(f"X_test sample:\n {X_test[:2]}")
    print(f"y_test sample:\n {y_test[:2]}")
    print("-" * 10)

# Reviewing Dataset and Basic Feature Creation
# First, let's load the dataset and create new features based on existing columns such as High-Low and Price-Open.


import pandas as pd
import datasets

# Loading the dataset (revision)
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])

# Creating basic features (revision)
tesla_df['High-Low'] = tesla_df['High'] - tesla_df['Low']
tesla_df['Price-Open'] = tesla_df['Close'] - tesla_df['Open']

# Displaying the DataFrame structure
print(tesla_df.head())
# Here, we calculate High-Low (the difference between the highest and lowest price of the day) and Price-Open 
        # (the difference between the closing and opening price) to create new features.

#  Introduction to Lag Features
## Lag features are essential in time series prediction as they help capture temporal patterns in the data by generating new features 
        ##from past values. Essentially, these features allow us to use past values to predict future ones.

# For instance, predicting today's closing price of Tesla stock might depend on the previous day's closing price. 
        # Here, the previous day's closing price would be a lagged feature.

# ------Creating and Implementing Lag Features
# Let's see how to create lag features using the shift() method in Pandas. We will add a new column, Close_lag1, to capture the previous day’s closing price.


# Creating a lag feature
tesla_df['Close_lag1'] = tesla_df['Close'].shift(1)

# Displaying a sample of the DataFrame with the lag feature
print(tesla_df[['Close', 'Close_lag1']].head())
# --The output of the above code will be:

Plain text
Copy to clipboard
      Close  Close_lag1
0  1.592667         NaN
1  1.588667    1.592667
2  1.464000    1.588667
3  1.280000    1.464000
4  1.074000    1.280000

        
# This output shows how the Close_lag1 column shifts the Close column values down by one row, making the first row's Close_lag1 
        # value NaN because there is no previous row to shift from.

# By using shift(1), we shift the closing price values down by one row, effectively capturing the previous day's closing price in a new column.      

        
        # Handling NaN Values Resulting from Lag Features
# Introducing lag features usually results in NaN values since the first row doesn't have a previous day to refer to. Let's handle these NaN values by dropping them.


# Dropping NaN values
tesla_df.dropna(inplace=True)

# Verifying the removal of NaN values
print(tesla_df[['Close', 'Close_lag1']].head())
# ------The output of the above code will be:

      Close  Close_lag1
1  1.588667    1.592667
2  1.464000    1.588667
3  1.280000    1.464000
4  1.074000    1.280000
5  1.053333    1.074000

        
        # This output verifies the effective removal of NaN values resulting from the creation of lag features, 
        # with the dataset now cleaned and ready for further processing. Dropping the NaN values ensures that our dataset is clean and ready for model training.        
# Defining Features and Target Variables
# Next, we'll define the features and target variables for our model. Our features will include Close_lag1, High-Low, Price-Open, and Volume.
        # Our target variable will be the Close price.

# Defining features and the target
features = tesla_df[['Close_lag1', 'High-Low', 'Price-Open', 'Volume']].values
target = tesla_df['Close'].values

# Displaying features and target
print("Features (first 5 rows):\n", features[:5])
print("Target (first 5 rows):\n", target[:5])
#  ----The output of the above code will be:


Features (first 5 rows):
 [[ 1.592667e+00  4.746670e-01 -1.306660e-01  2.578065e+08]
 [ 1.588667e+00  3.766670e-01 -2.026670e-01  1.232820e+08]
 [ 1.464000e+00  2.926670e-01 -2.533330e-01  7.709700e+07]
 [ 1.280000e+00  2.780000e-01 -2.593330e-01  1.030035e+08]
 [ 1.074000e+00  1.100000e-01 -4.000000e-02  1.038255e+08]]
Target (first 5 rows):
 [1.588667 1.464    1.28     1.074    1.053333]

        
        # --This output demonstrates the structured array format of features selected for the machine learning model training, 
        # ---including lag features and the immediate target values for the prediction. By defining these features and targets, 
        # ----we set up our dataset for machine learning models, enabling them to learn from past data to predict future stock 

import pandas as pd
import datasets

# Loading the dataset (revision)
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])

# Creating basic features (revision)
tesla_df['High-Low'] = tesla_df['High'] - tesla_df['Low']
tesla_df['Price-Open'] = tesla_df['Close'] - tesla_df['Open']

# Creating a lag feature
tesla_df['Close_lag1'] = tesla_df['Close'].shift(1)

# Dropping NaN values
tesla_df.dropna(inplace=True)

# Defining features and the target
features = tesla_df[['Close_lag1', 'High-Low', 'Price-Open', 'Volume']].values
target = tesla_df['Close'].values

# Displaying features and target
print("Features (first 5 rows):\n", features[:5])
print("Target (first 5 rows):\n", target[:5])

import pandas as pd
import datasets

# Loading the dataset
data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(data['train'])

# Creating basic features
tesla_df['High-Low'] = tesla_df['High'] - tesla_df['Low']
tesla_df['Price-Open'] = tesla_df['Close'] - tesla_df['Open']

# TODO: Create a lag feature for the 'Close' column
tesla_df['Close_lag1'] = tesla_df['Close'].shift(1)

# TODO: Drop NaN values to clean the dataset
tesla_df.dropna(inplace=True)
# Defining features and the target
features = tesla_df[['Close_lag1', 'High-Low', 'Price-Open', 'Volume']].values
target = tesla_df['Close'].values

# Displaying features and target
print("Features (first 5 rows):\n", features[:5])
print("Target (first 5 rows):\n", target[:5])    


#############################################################################################################################
        Introduction to Machine Learning with Gradient Boosting Models
#############################################################################################################################
Quick Revision: Data Loading and Preparation
First, let's quickly revise how to load data and prepare it for machine learning:

Python
Copy to clipboard
Play
import pandas as pd
from sklearn.preprocessing import StandardScaler
import datasets

# Load dataset
tesla = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla['train'])

# Convert the column to `datetime`
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

tesla_df['SMA_5'] = tesla_df['Adj Close'].rolling(window=5).mean()
tesla_df['SMA_10'] = tesla_df['Adj Close'].rolling(window=10).mean()
tesla_df['EMA_5'] = tesla_df['Adj Close'].ewm(span=5, adjust=False).mean()
tesla_df['EMA_10'] = tesla_df['Adj Close'].ewm(span=10, adjust=False).mean()

# Drop NaN values created by moving averages
tesla_df.dropna(inplace=True)

# Features and target selection
features = tesla_df[['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_5', 'SMA_10', 'EMA_5', 'EMA_10']].values
target = tesla_df['Adj Close'].values

# Standardizing features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
In this code we:

Convert the 'Date' column to datetime format.
Calculate SMA with windows of 5 and 10 days.
Calculate EMA with spans of 5 and 10 days.
Handle missing values resulting from moving averages.
Select relevant features and the target variable.
Standardize the feature values for better model performance.


# ------------------------------------------------------------------What is a Gradient Boosting Regressor?
# -- Gradient Boosting is a powerful machine learning technique used for predictive modeling tasks. 
 # Gradient Boosting Regressor is a specific application of this technique for regression tasks, where we aim to predict a continuous target variable like stock prices.

# In simple terms, Gradient Boosting works by creating an ensemble (a group) of weak prediction models, which are typically simple models.  
# It combines these weak models in a sequential manner to build a robust predictive model. Here's a simplified explanation of how it works:
                              

Initial Prediction: Start with an initial prediction, which is often the average of the target values.
Calculate Residuals: Calculate the residuals, which are the differences between the actual target values and the current predictions.
Train Weak Learners: Train a weak learner (a simple model) on the residuals to predict these errors.
Update Predictions: Update the overall predictions by adding the predictions of the weak learner to the current predictions.
Iterate: Repeat steps 2-4 multiple times, each time using a new weak learner to correct the errors of the previous model.
Through this iterative process, the gradient boosting regressor minimizes the errors and produces a strong predictive model.

# *************Training a Gradient Boosting Model

# First, we need to split the dataset into training and testing sets. Then, we instantiate a Gradient Boosting Regressor and fit the model to the training data.

# * Here is the necessary code to accomplish this:


from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.25, random_state=42)

# Instantiate and fit the model
model = GradientBoostingRegressor(random_state=42)
model.fit(X_train, y_train)

# Evaluating Model Performance
# Evaluating the model is crucial to understand how well it performs. We will:

# Make predictions with the trained model.
# Calculate and print the Mean Squared Error (MSE) to the actual y_test values.
# Here is how you can achieve this:


from sklearn.metrics import mean_squared_error

# Predict and evaluate
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)
The output of the above code will be:

Output Text:
        
Mean Squared Error: 0.4944244179351423
# This output indicates the accuracy of our Gradient Boosting Model by providing the mean squared error between the actual 
        # and predicted stock prices. A lower MSE value suggests better predictive performance.

# -- Visualizing Predictions
# -- Finally, let's visualize the actual vs predicted values to understand the performance of our model better:

# -- We will plot the actual and predicted values using scatter plots. Here's the visualization code:


import matplotlib.pyplot as plt

# Plotting predictions vs actual values
plt.figure(figsize=(10, 6))
plt.scatter(range(len(y_test)), y_test, label='Actual', alpha=0.7)
plt.scatter(range(len(y_test)), predictions, label='Predicted', alpha=0.7)
plt.title('Actual vs Predicted Values')
plt.xlabel('Sample Index')
plt.ylabel('Value')
plt.legend()
plt.show()        

        
# Here:

plt.figure(figsize=(10, 6)): This line initializes a new figure with a specified size.
plt.scatter(range(len(y_test)), y_test, label='Actual', alpha=0.7): This command creates a scatter plot of the actual values. The range(len(y_test)) generates x-coordinates, while y_test provides actual stock prices. The label parameter is set for the legend, and alpha=0.7 sets the transparency level.
plt.scatter(range(len(y_test)), predictions, label='Predicted', alpha=0.7): This command creates a scatter plot of the predicted values, using the same x-coordinates for comparison. The label parameter is set for the legend, and alpha=0.7 sets the transparency level.
plt.title('Actual vs Predicted Values'): Sets the title of the plot.
plt.xlabel('Sample Index'): Sets the x-axis label to 'Sample Index'.
plt.ylabel('Value'): Sets the y-axis label to 'Value'.
plt.legend(): Displays the legend to differentiate between actual and predicted values.
plt.show(): Renders the plot to the screen.

      
import pandas as pd
from sklearn.preprocessing import StandardScaler
from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load dataset
tesla = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla['train'])

# Convert 'Date' column to datetime format
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

# Adding technical indicators
tesla_df['SMA_5'] = tesla_df['Adj Close'].rolling(window=5).mean()
tesla_df['SMA_10'] = tesla_df['Adj Close'].rolling(window=10).mean()
tesla_df['EMA_5'] = tesla_df['Adj Close'].ewm(span=5, adjust=False).mean()
tesla_df['EMA_10'] = tesla_df['Adj Close'].ewm(span=10, adjust=False).mean()

# Drop NaN values created by moving averages
tesla_df.dropna(inplace=True)

# Features and target selection excluding the 'Close' column
features = tesla_df[['Close','Open', 'High', 'Low', 'Volume', 'SMA_5', 'SMA_10', 'EMA_5', 'EMA_10']].values
target = tesla_df['Adj Close'].values

# Standardizing features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Splitting the dataset again
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.25, random_state=42)

# Train the model
model = GradientBoostingRegressor(random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

# Visualizing the predictions
plt.figure(figsize=(10, 6))
plt.scatter(range(len(y_test)), y_test, label='Actual', alpha=0.7)
plt.scatter(range(len(y_test)), predictions, label='Predicted', alpha=0.7)
plt.title('Actual vs Predicted Values')
plt.xlabel('Sample Index')
plt.ylabel('Value')
plt.legend()
plt.show()   

   
import pandas as pd
from sklearn.preprocessing import StandardScaler
import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load dataset
tesla = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla['train'])

# Convert 'Date' to datetime format
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

# Calculate SMAs and EMAs
tesla_df['SMA_5'] = tesla_df['Adj Close'].rolling(window=5).mean()
tesla_df['SMA_10'] = tesla_df['Adj Close'].rolling(window=10).mean()
tesla_df['EMA_5'] = tesla_df['Adj Close'].ewm(span=5, adjust=False).mean()
tesla_df['EMA_10'] = tesla_df['Adj Close'].ewm(span=10, adjust=False).mean()

# Drop NaN values
tesla_df.dropna(inplace=True)

# Features and target selection
features = tesla_df[['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_5', 'SMA_10', 'EMA_5', 'EMA_10']].values
target = tesla_df['Adj Close'].values

# Standardizing features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.25, random_state=42)

# Instantiate and fit the Gradient Boosting Regressor
model = GradientBoostingRegressor(random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate the model
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

# Visualizing the actual vs predicted values
plt.figure(figsize=(10, 6))
plt.scatter(range(len(y_test)), y_test, label='Actual', alpha=0.7)
plt.scatter(range(len(y_test)), predictions, label='Predicted', alpha=0.7)
plt.title('Actual vs Predicted Values')
plt.xlabel('Sample Index')
plt.ylabel('Value')
plt.legend()
plt.show()


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
import datasets

# Load dataset
tesla = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla['train'])

# TODO: Convert 'Date' column to datetime format
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
# TODO: Add technical indicators: 
# - Price_Diff: Difference in adjusted close price from the previous day (Adj Close - Adj Close.shift(1))
# - Volatility: Standard deviation of adjusted close price over the last 5 days (Adj Close.rolling(window=5).std())
# - Momentum: Difference in adjusted close price compared to 5 days ago (Adj Close - Adj Close.shift(5))
# - Log_Price: Logarithm of the adjusted close price (np.log(Adj Close))
tesla_df['Price_Diff'] = tesla_df['Adj Close'] - tesla_df['Adj Close'].shift(1)
tesla_df['Volatility'] = tesla_df['Adj Close'].rolling(window=5).std()
tesla_df['Momentum'] = tesla_df['Adj Close'] - tesla_df['Adj Close'].shift(5)
tesla_df['Log_Price'] = np.log(tesla_df['Adj Close']) 

# TODO: Drop rows with NaN values
tesla_df.dropna(inplace=True)
# TODO: Select features (Price_Diff, Volatility, Momentum, Log_Price) and target variable (Adj Close)
features = tesla_df[['Price_Diff', 'Volatility', 'Momentum', 'Log_Price']].values
target = tesla_df['Adj Close'].values
# TODO: Standardize the feature values
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
# TODO: Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.25, random_state=42)
# TODO: Instantiate the Gradient Boosting Regressor and fit it to the training data
model = GradientBoostingRegressor(random_state=42)
model.fit(X_train, y_train)
# TODO: Make predictions and calculate the Mean Squared Error (MSE)
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)
# TODO: Visualize actual vs predicted values using scatter plots
plt.figure(figsize=(10, 6))
plt.scatter(range(len(y_test)), y_test, label='Actual', alpha=0.7)
plt.scatter(range(len(y_test)), predictions, label = 'Predicted', alpha=0.7)
plt.title('Actual vs Predicted Values')
plt.xlabel('Sample Index')
plt.ylabel('Value')
plt.legend()
plt.show()

         ######################################################################################################################################
                                                      Evaluating Model with Cross-Validation
        #######################################################################################################################################

# Review of Data Preparation
# Before we dive into evaluating our model with cross-validation, let's quickly review the data preparation steps we performed. This will ensure that we're on the same page regarding the dataset and features we're using.

# First, we loaded the Tesla ($TSLA) historical prices dataset:


from datasets import load_dataset
import pandas as pd

# Load dataset
tesla = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla['train'])

# Convert Date column to datetime type
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
Next, we performed feature engineering to add technical indicators and the target variable:


# Feature Engineering
tesla_df['Target'] = tesla_df['Adj Close'].shift(-1) - tesla_df['Adj Close']
tesla_df['SMA_5'] = tesla_df['Adj Close'].rolling(window=5).mean()
tesla_df['SMA_10'] = tesla_df['Adj Close'].rolling(window=10).mean()
tesla_df['EMA_5'] = tesla_df['Adj Close'].ewm(span=5, adjust=False).mean()
tesla_df['EMA_10'] = tesla_df['Adj Close'].ewm(span=10, adjust=False).mean()

# Drop NaN values created by moving averages
tesla_df.dropna(inplace=True)
Finally, we selected our features and target, and standardized the features:


from sklearn.preprocessing import StandardScaler

# Select features and target
features = tesla_df[['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_5', 'SMA_10', 'EMA_5', 'EMA_10']].values
target = tesla_df['Target'].values

# Standardizing features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
# This brings us to the prepared data that we'll use for model training and evaluation.
     
# Introduction to Cross-Validation
# Cross-validation is a key technique in evaluating the performance of machine learning models. 
# It helps in assessing how well our model generalizes to an independent dataset. By using cross-validation, 
               #we minimize the risk of overfitting and ensure our model's robustness.

# In K-Fold Cross-Validation, we split our dataset into k portions (folds). The model is trained on k - 1 folds and 
               # tested on the remaining fold. This process is repeated k times, each time using a different fold as the test set. 
               # The scores from each fold are then averaged to get a more reliable performance estimate.

# Here's a quick explanation of how K-Fold Cross-Validation works:

# First, we split data into k folds
# Then we train on k - 1 folds and test on the remaining fold
# We repeat this k times, each time with a different fold as the test set
# Finally, we take the average of the results from each fold
# We will use the cross_val_score function from sklearn.model_selection to perform cross-validation efficiently.

# Implementing Cross-Validation
# Let's move on to implementing cross-validation with our Gradient Boosting model. We'll set up the model and use 5-fold cross-validation to evaluate its performance.

# Start by importing the necessary functions and setting up the model:


from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingRegressor

# Instantiate model
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
# Next, perform cross-validation and print the mean score:


# Perform cross-validation
# The scoring parameter defaults to the negative mean absolute error
# for regression models, hence the negative scores.
scores = cross_val_score(model, features_scaled, target, cv=5, scoring='neg_mean_absolute_error')

# Convert negative mean absolute error to positive for easier interpretation
mean_score = -scores.mean()
print("Mean cross-validation score (Mean Absolute Error): ", mean_score)
# Output:
# Mean cross-validation score (Mean Absolute Error):   2.306462976736652
# In this code, the cross_val_score function performs 5-fold cross-validation on the model using Mean Absolute Error (MAE) 
# as the scoring metric (scoring='neg_mean_absolute_error'). MAE measures the average absolute difference between predicted 
# and actual values, with lower MAE values indicating better model performance because fewer errors mean better predictions. 
# However, since cross_val_score is designed to maximize scores, it returns the negative of the MAE to fit this convention. 
# The mean of these negative MAE scores gives an overall measure of the model's accuracy across different data splits, 
# and taking the negative of this mean provides the actual MAE.        

        
        # -------> Visualizing Model Predictions
#  Visualizing the model's predictions against actual values is crucial for understanding how well the model is performing. 
        # Let’s fit the model to our entire dataset and visualize its predictions.
# Fit the model to the data:
# Fit model to visualize predictions
model.fit(features_scaled, target)
predictions = model.predict(features_scaled)
# Now, let's create a scatter plot comparing the actual values to the predicted values:

import matplotlib.pyplot as plt

# Plotting predictions vs actual values
plt.figure(figsize=(10, 6))
plt.scatter(range(len(target)), target, label='Actual', alpha=0.7)
plt.scatter(range(len(target)), predictions, label='Predicted', alpha=0.7)
plt.title('Actual vs Predicted Values with Cross-Validation')
plt.xlabel('Sample Index')
plt.ylabel('Value')
plt.legend()
plt.show()



from datasets import load_dataset
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt

# Load dataset
tesla = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla['train'])

# Convert Date column to datetime type
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

# Feature Engineering
tesla_df['Target'] = tesla_df['Adj Close'].shift(-1) - tesla_df['Adj Close']
tesla_df['SMA_5'] = tesla_df['Adj Close'].rolling(window=5).mean()
tesla_df['SMA_10'] = tesla_df['Adj Close'].rolling(window=10).mean()
tesla_df['EMA_5'] = tesla_df['Adj Close'].ewm(span=5, adjust=False).mean()
tesla_df['EMA_10'] = tesla_df['Adj Close'].ewm(span=10, adjust=False).mean()

# Drop NaN values created by moving averages
tesla_df.dropna(inplace=True)

# Select features and target
features = tesla_df[['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_5', 'SMA_10', 'EMA_5', 'EMA_10']].values
target = tesla_df['Target'].values

# Standardizing features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Instantiate model
model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=3, random_state=42)

# Perform cross-validation
scores = cross_val_score(model, features_scaled, target, cv=10)
mean_score = scores.mean()
print("Mean cross-validation score: ", mean_score)

# Fit model to visualize predictions
model.fit(features_scaled, target)
predictions = model.predict(features_scaled)

# Plotting predictions vs actual values
plt.figure(figsize=(10, 6))
plt.scatter(range(len(target)), target, label='Actual', alpha=0.7)
plt.scatter(range(len(target)), predictions, label='Predicted', alpha=0.7)
plt.title('Actual vs Predicted Values with Cross-Validation')
plt.xlabel('Sample Index')
plt.ylabel('Value')
plt.legend()
plt.show()




from datasets import load_dataset
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt

# Load dataset
tesla = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla['train'])

# TODO: Convert Date column to datetime type
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
# TODO: Perform feature engineering to add a shifted Adj Close column as target, and the mean and std of Adj Close over 5 and 10 days
# - Add a new column 'Target' which is the difference between the shifted 'Adj Close' and the current 'Adj Close' to use as the target variable.
# - Add columns 'Mean_5' and 'Std_5', which are the mean and standard deviation of the 'Adj Close' over the past 5 days.
# - Add columns 'Mean_10' and 'Std_10', which are the mean and standard deviation of the 'Adj Close' over the past 10 days.
tesla_df['Target'] = tesla_df['Adj Close'].shift(-1) - tesla_df['Adj Close']
tesla_df['Mean_5'] = tesla_df['Adj Close'].rolling(window=5).mean()
tesla_df['Std_5'] = tesla_df['Adj Close'].rolling(window=5).mean()
tesla_df['Mean_10'] = tesla_df['Adj Close'].rolling(window=10).mean()
tesla_df['Std_10'] = tesla_df['Adj Close'].rolling(window=10).mean()
# TODO: Drop NaN values created during feature engineering
tesla_df.dropna(inplace=True)
# TODO: Select features and target values for model
# The target is the 'Target' column, features to choose is up to you
features = tesla_df[['Open', 'Close', 'High', 'Low', 'Mean_5', 'Std_5', 'Mean_10','Std_10']].values
target = tesla_df['Target'].values
# TODO: Standardize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
# TODO: Instantiate the Gradient Boosting model with `n_estimators = 100`, `learning_rate = 0.1`, `max_depth = 3`
model = GradientBoostingRegressor(n_estimators = 100, learning_rate=0.1, max_depth = 3)
# TODO: Perform 5-fold cross-validation and print the mean cross-validation score
scores = cross_val_score(model, features_scaled, target, cv=5)
mean_score = scores.mean()
print("Mean cross-valadation score:", mean_score)

# TODO: Fit the model to the entire dataset and predict target values
model.fit(features_scaled, target)
predictions = model.predict(features_scaled)
# TODO: Plot actual vs predicted values to visualize model performance```
plt.figure(figsize=(10,6))
plt.scatter(range(len(target)), target, label='Actual', alpha=0.7)
plt.scatter(range(len(target)), predictions, label='Predicted', alpha=0.7)
plt.title('Actual vs Predicted Values with Cross-Validation')
plt.xlabel('Sample Index')
plt.ylabel('Value')
plt.legend()
plt.show()   


###########################################################################################################################
Lesson 3 Hyperparameter Tuning Using GridsearchCV

Brief Revision of Loading and Preparing the Dataset
Before diving into hyperparameter tuning, let's quickly revise how we load and prepare our dataset. We start by loading the Tesla dataset, 
adding technical indicators, and splitting the data into training and testing sets.

Here's a quick overview of the code:

Python
Copy to clipboard
Play
import pandas as pd
from datasets import load_dataset

# Load dataset
tesla = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla['train'])

# Feature Engineering
tesla_df['SMA_5'] = tesla_df['Adj Close'].rolling(window=5).mean()
tesla_df['SMA_10'] = tesla_df['Adj Close'].rolling(window=10).mean()
tesla_df['EMA_5'] = tesla_df['Adj Close'].ewm(span=5, adjust=False).mean()
tesla_df['EMA_10'] = tesla_df['Adj Close'].ewm(span=10, adjust=False).mean()

# Drop NaN values created by moving averages
tesla_df.dropna(inplace=True)

# Select features and target
features = tesla_df[['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_5', 'SMA_10', 'EMA_5', 'EMA_10']].values
target = tesla_df['Adj Close'].shift(-1).dropna().values  # Predicting next day's close price
features = features[:-1] # Align features and target arrays correctly for time series forecasting

# Splitting the dataset into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.25, random_state=42)
The code above loads the Tesla historic prices dataset, applies feature engineering to add technical indicators like Simple Moving Averages (SMA) 
and Exponential Moving Averages (EMA), and preprocesses the dataset by removing NaN values. It then selects relevant features and the target variables, 
preparing the data for training and testing by splitting it into training and testing sets. 
The line target = tesla_df['Adj Close'].shift(-1).dropna().values is used for predicting the next day's closing price. 
The line features = features[:-1] ensures that the features and target arrays are aligned correctly for a time series forecasting task where you 
want to predict the next day's closing price.


# Introduction to Hyperparameter Tuning
# Hyperparameters are configuration settings used to tune how our models learn. Examples include learning_rate, n_estimators, and max_depth in Gradient Boosting. 
# Proper hyperparameter tuning can significantly improve model performance.

# Imagine you're trying to make the perfect soup. Hyperparameter tuning is like adjusting the seasoning to get the best flavor. 
# Just like too much salt or too little pepper can ruin the dish, poor hyperparameters can underperform our model.

# The downside of this approach however is that it takes much more time, as every combination of hyperparameters is being tested.
# Setting up a Hyperparameter Grid
# To find the best hyperparameters, we'll need to test various combinations. This is where the hyperparameter grid comes in. We define a set of values to test for each hyperparameter.

# Here are the key hyperparameters we'll tune:

# learning_rate: This controls the contribution of each tree to the final prediction. A smaller learning rate means the model learns more slowly but can achieve better performance with proper tuning.
# n_estimators: This is the number of boosting stages (trees) to be used in the model. More boosting stages can improve performance but may also lead to overfitting.
# max_depth: This determines the maximum depth of the trees. Deeper trees can capture more complex patterns but may also overfit the training data.
# Here's how to set up a hyperparameter grid:


# Setting up the hyperparameter grid
param_grid = {
    'learning_rate': [0.01, 0.1],
    'n_estimators': [100, 200],
    'max_depth': [3, 4]
}
# In this grid, each combination of learning_rate, n_estimators, and max_depth will be tested. In this param_grid dictionary, the keys are hyperparameter names, 
             # and mapped lists contain their possible values.


# ------>>>>>>Implementing GridSearchCV
# GridSearchCV automates the process of hyperparameter tuning by searching for the best combination of parameters in our grid.

# Here's how to implement GridSearchCV:

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor

# Instantiate the GridSearchCV object
model = GridSearchCV(GradientBoostingRegressor(random_state=42), param_grid, cv=3)

# Fit the model to the training data
model.fit(X_train, y_train)

         
         #In the code above, we first import the necessary libraries. We then instantiate the GridSearchCV object with a GradientBoostingRegressor 
         # and our predefined param_grid. The cv=3 parameter specifies that 3-fold cross-validation should be used, meaning the data will be split 
         # into three subsets, and the model will be trained and validated three times, each time using a different subset for validation and the 
         # remaining subsets for training. This helps ensure the model's performance is robust and not dependent on a particular train-test split. 
         # Finally, we fit the GridSearchCV object to the training data, which involves training multiple models using different hyperparameter 
         # combinations and selecting the best one based on cross-validation results.
             
# Evaluating and Interpreting Results
# Once GridSearchCV has found the best parameters, we need to evaluate and interpret the results.


# Print the best parameters found
print("Best parameters found:", model.best_params_)
# Output:
# Best parameters found: {'learning_rate': 0.1, 'max_depth': 3, 'n_estimators': 100}
# Now, using the combination of hyperparameters resulted in the best model performance, let's calculate the error using these parameters:

# Predict with the best estimator
best_model = model.best_estimator_
predictions = best_model.predict(X_test)

# Calculate and print Mean Squared Error
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error with best params:", mse)
# Output:
# Mean Squared Error with best params: 22.27547097230719
# This indicates the model's accuracy using the optimized hyperparameters, with a lower MSE indicating better accuracy.

# Visualizing Predictions
# Visualizing predictions helps us understand how well our model is performing and identify any patterns or discrepancies between the 
# actual and predicted values. By plotting the actual values against the predicted values, we can visually assess the model's accuracy  
# and spot areas where the predictions may be off. This is crucial for interpreting the effectiveness of our hyperparameter tuning and understanding the model's behavior.


# Plotting predictions vs actual values
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(range(len(y_test)), y_test, label='Actual', alpha=0.7)
plt.scatter(range(len(y_test)), predictions, label='Predicted', alpha=0.7)
plt.title('Actual vs Predicted Values with Tuned Hyperparameters')
plt.xlabel('Sample Index')
plt.ylabel('Value')
plt.legend()
plt.show()


 import pandas as pd
from datasets import load_dataset
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load dataset
tesla = load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla['train'])

# Feature Engineering
tesla_df['SMA_5'] = tesla_df['Adj Close'].rolling(window=5).mean()
tesla_df['SMA_10'] = tesla_df['Adj Close'].rolling(window=10).mean()
tesla_df['EMA_5'] = tesla_df['Adj Close'].ewm(span=5, adjust=False).mean()
tesla_df['EMA_10'] = tesla_df['Adj Close'].ewm(span=10, adjust=False).mean()

# Drop NaN values created by moving averages
tesla_df.dropna(inplace=True)

# Select features and target
features = tesla_df[['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_5', 'SMA_10', 'EMA_5', 'EMA_10']].values
target = tesla_df['Adj Close'].shift(-1).dropna().values  # Predicting next day's close price
features = features[:-1]

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.25, random_state=42)

# Setting up the hyperparameter grid
param_grid = {
    'learning_rate': [0.01, 0.1],
    'n_estimators': [100, 200],
    'max_depth': [3, 4]
}

# Instantiate the GridSearchCV object
model = GridSearchCV(GradientBoostingRegressor(random_state=42), param_grid, cv=2)

# Fit the model to the training data
model.fit(X_train, y_train)

# Print the best parameters found
print("Best parameters found:", model.best_params_)

# Predict with the best estimator
best_model = model.best_estimator_
predictions = best_model.predict(X_test)

# Calculate and print Mean Squared Error
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error with best params:", mse)

# Plotting predictions vs actual values
plt.figure(figsize=(10, 6))
plt.scatter(range(len(y_test)), y_test, label='Actual', alpha=0.7)
plt.scatter(range(len(y_test)), predictions, label='Predicted', alpha=0.7)
plt.title('Actual vs Predicted Values with Tuned Hyperparameters')
plt.xlabel('Sample Index')
plt.ylabel('Value')
plt.legend()
plt.show()       

Revision of Previous Steps
Before diving into feature importance, let's quickly revise the previous steps to ensure we have a solid foundation.

Data Preparation and Feature Engineering:

Python
Copy to clipboard
Play
import pandas as pd
import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load TSLA dataset
tesla = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla['train'])

# Convert Date column to datetime type
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

# Feature Engineering: adding technical indicators as features
tesla_df['SMA_5'] = tesla_df['Adj Close'].rolling(window=5).mean()
tesla_df['SMA_10'] = tesla_df['Adj Close'].rolling(window=10).mean()
tesla_df['EMA_5'] = tesla_df['Adj Close'].ewm(span=5, adjust=False).mean()
tesla_df['EMA_10'] = tesla_df['Adj Close'].ewm(span=10, adjust=False).mean()

# Drop NaN values created by moving averages
tesla_df.dropna(inplace=True)

# Select features and target
features = tesla_df[['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_5', 'SMA_10', 'EMA_5', 'EMA_10']].values
target = tesla_df['Adj Close'].values

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.25, random_state=42)

# Standardizing features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
Model Training:


from sklearn.ensemble import GradientBoostingRegressor

# Instantiate and fit the model
model = GradientBoostingRegressor(random_state=42)
model.fit(X_train, y_train)

Understanding Feature Importance
What is Feature Importance?

Feature importance refers to techniques that assign scores to input features based on their importance in predicting the target variable. In the context of a Gradient Boosting model, feature importance indicates how valuable each feature is in constructing the boosted decision trees.

Why is Feature Importance Useful?

Understanding feature importance helps:

Identify and select the most influential features, potentially simplifying the model.
Gain insights into the factors driving your predictions.
Improve model interpretability and trustworthiness

Computing Feature Importance in Gradient Boosting
Once the Gradient Boosting model is trained, we can easily access the feature importances. Let's walk through the steps:

Python
Copy to clipboard
Play
# Compute feature importance
feature_importance = model.feature_importances_

# Create a DataFrame for better visualization of feature names alongside their importance
feature_names = ['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_5', 'SMA_10', 'EMA_5', 'EMA_10']
feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance})

# Sort features by importance
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# Print feature importances with names
print("Feature importance:\n", feature_importance_df)
# Output:
# Feature importance:
#   Feature    Importance
# 3   Close  9.447889e-01
# 1    High  3.668675e-02
# 0    Open  9.142875e-03
# 2     Low  8.464037e-03
# 6  SMA_10  4.800413e-04
# 7   EMA_5  2.992652e-04
# 8  EMA_10  1.326235e-04
# 5   SMA_5  5.195267e-06
# 4  Volume  3.363300e-07
Here's what each step is doing:

model.feature_importances_: Extracts the feature importance scores from the trained Gradient Boosting model.
feature_names = [...]: Defines a list of feature names for better readability.
feature_importance_df = pd.DataFrame(...): Creates a DataFrame that links feature names with their respective importance scores.
feature_importance_df.sort_values(...): Sorts the DataFrame by feature importance in descending order for better interpretation.

Visualizing Feature Importance
Visualizing the importance of features helps interpret the results more effectively. We'll use Matplotlib to create a bar chart:

Python
Copy to clipboard
Play
import matplotlib.pyplot as plt

feature_importance_df = feature_importance_df.iloc[::-1]

# Plotting feature importance
plt.figure(figsize=(10,6))
plt.barh(feature_importance_df['Feature'], feature_importance_df['Importance'])
plt.title('Feature Importances')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.show()

Interpreting the Results
By examining the feature importance values and plot, you can determine which features have the most impact on the model's predictions. For instance, if Adj Close heavily relies on SMA_10 and Close, we know they are critical factors in the stock's movement.

Insights and Next Steps:

Focus on Key Features: Emphasize the most important features in further analysis and model tuning.
Feature Selection: Consider removing less important features to simplify the model.
Model Interpretation: Use feature importance insights to explain model predictions to stakeholders.

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt

# Logging level setup
import logging
logging.getLogger('datasets').setLevel(logging.ERROR)

# Load TSLA dataset
tesla = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla['train'])

# Convert Date column to datetime type
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])

# Feature Engineering: adding technical indicators as features
tesla_df['SMA_5'] = tesla_df['Adj Close'].rolling(window=5).mean()
tesla_df['SMA_10'] = tesla_df['Adj Close'].rolling(window=10).mean()
tesla_df['EMA_5'] = tesla_df['Adj Close'].ewm(span=5, adjust=False).mean()
tesla_df['EMA_10'] = tesla_df['Adj Close'].ewm(span=10, adjust=False).mean()

# Drop NaN values created by moving averages
tesla_df.dropna(inplace=True)

# Select features and target
features = tesla_df[['Open', 'High', 'Low', 'Close', 'SMA_5', 'SMA_10', 'EMA_5', 'EMA_10']].values
target = tesla_df['Adj Close'].values

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.25, random_state=42)

# Standardizing features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Instantiate and fit the model
model = GradientBoostingRegressor(random_state=42)
model.fit(X_train, y_train)

# Compute feature importance
feature_importance = model.feature_importances_

# Create a DataFrame for better visualization of feature names alongside their importance
feature_names = ['Open', 'High', 'Low', 'Close', 'SMA_5', 'SMA_10', 'EMA_5', 'EMA_10']
feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance})

# Sort features by importance
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# Print feature importances with names
print("Feature Importance:\n", feature_importance_df)

# Plotting feature importance
plt.figure(figsize=(10, 6))
plt.bar(range(len(feature_importance)), feature_importance)
plt.title('Feature Importances')
plt.xlabel('Feature Index')
plt.ylabel('Importance')
plt.xticks(range(len(feature_importance)), feature_names, rotation=45)
plt.show()
