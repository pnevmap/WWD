import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('arstotzkan.csv')
print(df.head())
missing_values = df.isnull().sum()
print(missing_values)
print(df.describe())



# Convert 'Date_Time_Record' to datetime
df['Date_Time_Record'] = pd.to_datetime(df['Date_Time_Record'])

# Set 'Date_Time_Record' as the index
df = df.set_index('Date_Time_Record')
print (df.index.min())
print (df.index.max())

# Count records by year

# Resample by year and count records
records_by_year = df.resample('YE').size()
print(records_by_year)

# Create the time series plot
plt.figure(figsize=(10, 6))

# Plot the original data
plt.plot(records_by_year.index, records_by_year.values, marker='o', label='Original Data')

# Plot the moving average
color_map = ['','red', 'green', 'blue', 'yellow']
for i in range(1,5):
    print (i*2)
    moving_average = records_by_year.rolling(window=i*2).mean()
    plt.plot(moving_average.index, moving_average.values, color=color_map[i], label=f'{i*2}-Year Moving Average')


moving_average = records_by_year.rolling(window=3).mean()
plt.plot(moving_average.index, moving_average.values, color=color_map[3], label=f'{3}-Year Moving Average')

plt.title('Number of Emigration Records by Year')
plt.xlabel('Year')
plt.ylabel('Number of Records')
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.ticker as ticker
# Find the distinct values of the `profession` column
distinct_professions = df['Profession'].unique()

# Print the distinct values of the `profession` column
print(distinct_professions)
# Create a figure and axes for the plot
plt.figure(figsize=(12, 5))

#Iterate over age groups and plot the data
for profession in distinct_professions:
    # Filter data for the current age group
    df_by_profession = df[(df['Profession'] == profession)]

    # Resample by year and count records
    records_by_year = df_by_profession.resample('YE').size()

    # Plot the data for the current age group
    plt.plot(records_by_year.index, records_by_year.values, label=f'{profession}')

# Set plot labels and title
plt.title('Number of Records by Profession Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Records')
plt.legend()
plt.grid(True)

plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# Show the plot
plt.show()

distinct_civil_status = df['Civil_Status'].unique()
print(distinct_civil_status)

for group in distinct_civil_status:
    # Filter data for the current age group
    df_by_group = df[(df['Civil_Status'] == group)]
    # Resample by year and count records
    records_by_year = df_by_group.resample('YE').size()
    # Plot the data for the current age group
    plt.plot(records_by_year.index, records_by_year.values, label=f'{group}')

# Set plot labels and title
plt.title('Number of Records by Civil Status Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Records')
plt.legend()
plt.grid(True)

plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# Show the plot
plt.show()


distinct_civil_status = df['Annual_Income'].unique()
print(distinct_civil_status)

import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

def plot_income_histogram(df):
  """
  Plots a histogram of the 'Annual_Income' column in a DataFrame and adds a mean line.

  Args:
    df: pandas DataFrame with an "Annual_Income" column.
  """

  plt.figure(figsize=(10, 6))  # Set figure size

  # Plot the histogram
  plt.hist(df["Annual_Income"], bins=20, color='skyblue', edgecolor='black')

  # Calculate and plot the mean line
  mean_income = df["Annual_Income"].mean()
  plt.axvline(mean_income, color='red', linestyle='dashed', linewidth=2, label=f"Mean Income: {mean_income:.2f}")

  # Add labels and title
  plt.xlabel("Annual Income")
  plt.ylabel("Frequency")
  plt.title("Histogram of Annual Income")
  plt.legend()

  plt.show()

# Example usage:
# Assuming your DataFrame is named 'df'
plot_income_histogram(df)

import pandas as pd
import matplotlib.pyplot as plt

def plot_income_histogram_boxplot(df):
  """
  Plots a histogram and boxplot of the 'Annual_Income' column in a DataFrame.

  Args:
    df: pandas DataFrame with an "Annual_Income" column.
  """

  fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)  # Create 2 subplots

  # Histogram
  ax1.hist(df["Annual_Income"], bins=20, color='skyblue', edgecolor='black')
  mean_income = df["Annual_Income"].mean()
  ax1.axvline(mean_income, color='red', linestyle='dashed', linewidth=2, label=f"Mean Income: {mean_income:.2f}")
  ax1.set_ylabel("Frequency")
  ax1.set_title("Histogram and Boxplot of Annual Income")
  ax1.legend()

  # Boxplot
  ax2.boxplot(df["Annual_Income"], vert=False)  # Horizontal boxplot
  ax2.set_xlabel("Annual Income")

  plt.tight_layout()  # Adjust layout for better spacing
  plt.show()

# Example usage:
# Assuming your DataFrame is named 'df'
plot_income_histogram_boxplot(df)

import pandas as pd
import matplotlib.pyplot as plt
# Calculate value counts and store in a new DataFrame
income_counts = df['Annual_Income'].value_counts().reset_index()
income_counts.columns = ['Annual_Income', 'Count']

print(income_counts)


