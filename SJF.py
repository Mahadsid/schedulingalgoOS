from numpy import *
import numpy as np
print("Shortest Job First scheduling")
n= int(input("Enter The Number of Processes: "))
d=dict()
for i in range(n):
    key = "P"+str(i+1)
    a = int(input("Enter arrival time of process"+str(i+1)+": "))
    b = int(input("Enter burst time of process"+str(i+1)+": "))
    l=[]
    l.append(a)
    l.append(b)
    d[key] = l

d=sorted(d.items(),key=lambda item: item[1][1])
#print(d)
#print(d[0][1][1])

ct = []
for i in range(int(len(d))):
    if i == 0: 
    # for first task ct is null so ct = at + bt of that process
        ct.append(d[i][1][1] + d[i][1][0])
    else:
        ct.append(d[i][1][1] + ct[i-1])

# printing Compltion time
for i in range(len(ct)):
    print ("Compltion time for P{} is: {}".format(d[i][0],ct[i]))


tat = []
for i in range(int(len(d))):
    tat.append(ct[i] - d[i][1][0])
    
# printing Turn Around Time
for i in range(len(tat)):
    print ("Turn Around Time for P{} is: {}".format(d[i][0],tat[i]))

avarage_TAT = round(np.mean(tat),2)
print ("Average Turn Around Time for all process is: ",avarage_TAT)


wt = []
for i in range(int(len(d))):
    wt.append(tat[i] - d[i][1][1])
    
# printing Waiting time
for i in range(len(wt)):
    print ("Waiting time for P{} is: {}".format(d[i][0],wt[i]))

avarage_WT = round(np.mean(wt),2)
print ("Average Turn Around Time for all process is: ",avarage_WT)

print("Process | Arrival | Burst | Exit | Turn Around | Wait |")
for i in range(n):
      print("   ",d[i][0],"   |   ",d[i][1][0]," |    ",d[i][1][1]," |    ",ct[i],"  |    ",tat[i],"  |   ",wt[i],"   |  ")
print("Average Waiting Time: ",avarage_WT)
print("Average Turnaround Time: ",avarage_TAT)
