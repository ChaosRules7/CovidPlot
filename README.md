# CovidPlot
Analyze and Plot WHO Covid Data

This program si meant to automatically analyze the WHO Covid Data, by adding the new data sets '7d Indicator' and
'Deaths 7d avg'. At the end 'New Cases', '7d Indicator', 'Deaths' and 'Deaths 7d avg' are plotted.

The program is at the moment hard-coded to analyze the data for Germany since 2020-09-01

Requirements:
- Pandas Libary (https://pandas.pydata.org/)
- MatPlotLib Libary (https://matplotlib.org/)
- WHO Covid Data as csv file (https://covid19.who.int/; button bottom right corner)


Definition '7d Indicator':
The sum of all reported cases of the last seven days per 100.000 citizens of the country.
Number of citizens is currently hard coded.

Definition of 'Deaths 7d avg':
The sum of all reported covid deaths within the last seven days divided by seven to get
the daily average for that periode.


Planned Features:
- Choice of Country and time periode
- GUI
- Optical plot improvements
