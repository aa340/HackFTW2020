import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
landData = pd.read_csv('land.csv', usecols = ['Year', 'Month','MonthlyAnomally'])
#print(landData) #print

def getMonthAverageAnomaly(start, end):
  monthAverageAnomaly = []
  counter = 1
  tempMonthAnomaly = 0.0
  with open("land.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
      tempMonthAnomaly = 0
      if line[0].split(",")[2] != "MonthlyAnomally":
        if counter != 12:
          tempMonthAnomaly+=float(line[0].split(",")[2])
          counter+=1
        else:
          tempMonthAnomaly+=float(line[0].split(",")[2])
          counter = 1
          roundedValue = round(tempMonthAnomaly/12.0, 4)
          if roundedValue:
            monthAverageAnomaly.append(roundedValue)
          else:
            monthAverageAnomaly.append(0.0000)
  year = 1750
  values = []
  for i in monthAverageAnomaly:
    values.append([year,i])
    print(str(year)+" "+str(i))
    year+=1
  valuesEdited = []
  for i in values:
    if i[0] >= int(start) and i[0] < int(end):
      valuesEdited.append([i[0],i[1]])
  return valuesEdited       
       
def sortList(list):
  for i in list:
    i = float(i)
  list.sort(key = float)
  for i in list:
    i = str(i)
  return list  


def selectYearRange(start,stop):
  x=[]
  y=[]
  years = []
  averageAnomalys = []
  with open("land.csv", "r") as f:
    with open('selectYearRangeLand.csv','w') as fd:
      reader = csv.reader(f, delimiter="\t")
      temp = getMonthAverageAnomaly(start,stop)
      print(temp)
      for i in temp:
        years.append(i[0])
        averageAnomalys.append(i[1])
      fig = plt.figure(figsize=(10, 8))
      axis = fig.add_subplot(111)
      axis.plot(years, averageAnomalys)
      axis.set_title("Average anomally of year " + str(start) + " to year " + str(stop))
      axis.set_xlabel("Years")
      axis.set_ylabel("Average Anomally")
      fig.savefig('static/images/selectYearRange.png')


def selectIndividualYear(year):
  x=[]
  y=[]
  with open("land.csv", "r") as f:
    with open('selectIndividualYearLand.csv','w') as fd:
      reader = csv.reader(f, delimiter="\t")
      for i, line in enumerate(reader):
        if line[0].split(",")[0] == year:
          print('line[{}] = {}'.format(i, line))
          string = ",".join(line)
          fd.write(string)
          fd.write("\n")
          x.append(line[0].split(',')[1])
          y.append(line[0].split(",")[2])
      fig = plt.figure(figsize=(10, 8))
      axis = fig.add_subplot(111)
      axis.plot(x, y)
      axis.set_title("Monthly Anomally of Year " + str(year))
      axis.set_xlabel("Month")
      axis.set_ylabel("Monthly Anomally")
      fig.savefig('static/images/individualYear.png')
