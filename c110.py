import random 
import statistics
import plotly.figure_factory as ff 
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()

def random_set_of_mean(counter):
  
  dataset=[]
  for i in range(0,100):
    random_index = random.randint(0,len(data)-1)
    value=data[random_index]
    dataset.append(value)
  mean=statistics.mean(dataset)
  return mean
def show_fig(mean_list):
  df=mean_list 
  fig=ff.create_distplot([df],["reading_time"],show_hist=False)
  fig.show()

def setup():
  mean_list=[]
  for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)
  show_fig(mean_list)
setup()
mean_of_sample1=statistics.mean(data)
mean=statistics.mean(data)
sd=statistics.stdev(data)
z_score=(mean_of_sample1-mean)/sd
print("z score is",z_score)