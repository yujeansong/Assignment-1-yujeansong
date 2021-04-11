import pandas as pd
import argparse
import matplotlib.pyplot as plt
import sys
import numpy as np

covid = pd.read_csv("owid-covid-data.csv", encoding = "UTF8")

covid = covid[["location", "date", "total_cases", "new_cases", "total_deaths", "new_deaths"]]

covid[covid["date"].str[:4] == "2020"]

#change datetime to integer month  
covid["date"] = covid["date"].map(lambda x: int(x[5:7]))


covid.insert(2, "month", covid["date"])

#delete the date column
del covid["date"]

covid["case_fatality_rate"] = (covid["total_deaths"])/(covid["total_cases"])

#print the DataFrame sorted by location & month
covid = covid[["location", "month", "case_fatality_rate", "total_cases", "new_cases", "total_deaths", "new_deaths"]].sort_values(by = ["location", "month"])

phi = np.linspace(0, 2*np.pi, covid["location"].drop_duplicates().size)
rgb_cycle = np.vstack((            # Three sinusoids
    .5*(1.+np.cos(phi          )), # scaled to [0,1]
    .5*(1.+np.cos(phi+2*np.pi/3)), # 120° phase shifted.
    .5*(1.+np.cos(phi-2*np.pi/3)))).T # Shape = (60,3)

uniq_locations = list(covid["location"].drop_duplicates())
locations = list(covid["location"])
colours = list(map(lambda loc: rgb_cycle[uniq_locations.index(loc)], locations))

#x-axis for new_cases & y-axis for case_fatality_rate
plt.scatter(covid["new_cases"], covid["case_fatality_rate"], c = colours)
plt.ylabel("case_fatality_rate")
plt.xlabel("new_cases")
plt.grid(True)

#scatter-a.png
plt.savefig(sys.argv[1])

#scatter-b.png, logscale
plt.xscale("log")
plt.savefig(sys.argv[2])
