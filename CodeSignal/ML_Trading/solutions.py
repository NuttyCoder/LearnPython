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
