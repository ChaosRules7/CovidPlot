import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv')  # load the data into a DataFrame
df['Date_reported'] = pd.to_datetime(df['Date_reported'], format="%Y-%m-%d")  # transform dates into timestamps

start = pd.to_datetime("2020-09-01", format="%Y-%m-%d")  # set the start date for the plot


# setting the filter for country and date:
df_germany = df.loc[df['Country'] == 'Germany']  # Filter to specific Country
df_filter = df_germany.loc[df_germany['Date_reported'] > start]  # setting start point within the DataFrame


# calculating and setting the 7d Indicator:
# calculating the sum of 7 consecutive days:
df_filter['7d Indicator'] = df_filter['New_cases'].rolling(7).sum().shift(7)
# divide the sum by Population(integer)/100.000 to get final 7d Indicator:
df_filter['7d Indicator'] = df_filter['7d Indicator'] / 830
df_filter['7d Indicator'] = round(df_filter['7d Indicator'], 0)  # round the float to make it neat


# calculating and setting the average for the daily deaths:
# calculating the sum of 7 consecutive days:
df_filter['Death 7d avg'] = df_filter['New_deaths'].rolling(7).sum().shift(7)
df_filter['Death 7d avg'] = df_filter['Death 7d avg'] / 7  # calculate the 7d average
df_filter['Death 7d avg'] = round(df_filter['Death 7d avg'], 2)  # round the float to make it neat


# setting the first subplot (New Cases):
plt.subplot(2, 2, 1)
plt.plot(df_filter['Date_reported'], df_filter['New_cases'], 'bx-')
plt.xlabel('Date Reported')
plt.ylabel('New Cases')
plt.ylim(0,)
plt.title('New Cases')
plt.grid(b=True, axis='both')


# setting second subplot (7d Indicator):
plt.subplot(2, 2, 2)
plt.plot(df_filter['Date_reported'], df_filter['7d Indicator'])
plt.xlabel('Date Reported')
plt.ylabel('Weekly new Cases per 100.000')
plt.ylim(0,)
plt.title('7d Indicator')
plt.grid(b=True, axis='both')


# setting third subplot (deaths and 7d avg):
plt.subplot(2, 2, 3)
plt.plot(df_filter['Date_reported'], df_filter['New_deaths'], 'x-', label='Death')
plt.plot(df_filter['Date_reported'], df_filter['Death 7d avg'], 'r-',  label='7d Avg')
plt.xlabel('Date Reported')
plt.ylabel('Death')
plt.ylim(0,)
plt.title('Death')
plt.legend()
plt.grid(b=True, axis='both')


plt.suptitle('WHO Covid Data for Germany')  # setting the overall plot title

plt.show()  # show the final plot
