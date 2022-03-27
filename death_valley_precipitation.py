import csv
import matplotlib.pyplot as plt
from datetime import datetime

#Opening the file
file_name = 'data\death_valley_2018_simple.csv'

with open(file_name) as f:
    reader = csv.reader(f)
    headers = next(reader)
    rains = []
    dates = []

#saving the data in two lists in order to plot
    for row in reader:
        rain = float(row[3])
        date = datetime.strptime(row[2], '%Y-%m-%d')
        rains.append(rain)
        dates.append(date)

#Setting the plot
x_values = dates
y_values = rains

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(x_values, y_values, color='blue')

#setting the configs
ax.set_title('Precipitation in Sikta, Alaska', fontsize=24)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Precipitation', fontsize=14)

#tick params
ax.tick_params(axis='both', labelsize=14)

#formating the date
fig.autofmt_xdate()
plt.show()
