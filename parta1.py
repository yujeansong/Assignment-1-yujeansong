import pandas as pd
import argparse
import sys

covid = pd.read_csv("owid-covid-data.csv", encoding = "UTF8")

covid = covid[["location", "date", "total_cases", "new_cases", "total_deaths", "new_deaths"]]

#parse it out with 2020 data
covid = covid[covid["date"].str[:4] == "2020"]

#add month column into order of second column
covid["date"] = covid["date"].map(lambda x: int(x[5:7]))
covid.insert(2, "month", covid["date"])
del covid["date"]

covid["case_fatality_rate"] = (covid["total_deaths"])/(covid["total_cases"])

#print the DataFrame sorted by location & month
covid = covid[["location", "month", "case_fatality_rate", "total_cases", "new_cases", "total_deaths", "new_deaths"]].sort_values(by = ["location", "month"])

print(covid.head(5))

covid.to_csv(sys.argv[1])
