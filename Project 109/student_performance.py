import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics 
import plotly.graph_objects as go

#Reading the data
data=pd.read_csv("StudentsPerformance.csv")
math_score=data["math score"].tolist()

#Finding mean,median,mode and std dev
mean=statistics.mean(math_score)
std_dev=statistics.stdev(math_score)
median=statistics.median(math_score)
mode=statistics.mode(math_score)
print('Mean is {},Median is {}, Mode is {},Standard Deviation is {}'.format(mean,median,mode,std_dev))

#Marking the area between the 3 std devs
first_std_dev_start=mean-std_dev
first_std_dev_end=mean+std_dev

second_std_dev_start=mean-(2*std_dev)
second_std_dev_end=mean+(2*std_dev)

third_std_dev_start=mean-(3*std_dev)
third_std_dev_end=mean+(3*std_dev)

figure=ff.create_distplot([math_score],["Student performance in Maths"],show_hist=False)
figure.add_trace(go.Scatter(x=[first_std_dev_start,first_std_dev_start],y=[0,0.05],name="First std dev start"))
figure.add_trace(go.Scatter(x=[first_std_dev_end,first_std_dev_end],y=[0,0.05],name="First std dev end"))
figure.add_trace(go.Scatter(x=[second_std_dev_start,second_std_dev_start],y=[0,0.05],name="Second std dev start"))
figure.add_trace(go.Scatter(x=[second_std_dev_end,second_std_dev_end],y=[0,0.05],name="Second std dev end"))
figure.add_trace(go.Scatter(x=[third_std_dev_start,third_std_dev_start],y=[0,0.05],name="Third std dev start"))
figure.add_trace(go.Scatter(x=[third_std_dev_start,third_std_dev_start],y=[0,0.05],name="Third std dev end"))
figure.add_trace(go.Scatter(x=[mean,mean],y=[0,0.05],name="Mean"))
figure.show()

list_stdev_first=[i for i in math_score if i>first_std_dev_start and i<first_std_dev_end]
list_stdev_second=[i for i in math_score if i>second_std_dev_start and i<second_std_dev_end]
list_stdev_third=[i for i in math_score if i>third_std_dev_start and i<third_std_dev_end]

perct_stdev1=len(list_stdev_first)*100.0/len(math_score)
perct_stdev2=len(list_stdev_second)*100.0/len(math_score)
perct_stdev3=len(list_stdev_third)*100.0/len(math_score)

print("List dev1={},List dev2={},List dev3={}".format(perct_stdev1,perct_stdev2,perct_stdev3))
