print("First Come First Serve scheduling")
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

d=sorted(d.items(),key=lambda item: item[1][0])
print(d)

#print(d[0][1][0])


ET = [] # completition = burst + arrival
for i in range(len(d)):
    # first process
    if(i==0):
        ET.append(d[i][1][1] + d[i][1][0])
 
    # get prevET + newBT
    else:
        ET.append(d[i][1][1] + ct[i-1])
print(ET)

 
TAT = [] # tat = burst - arrival
for i in range(len(d)):
    TAT.append(ET[i] - d[i][1][0])
print(TAT)

WT = [] # waitingtime = TAT - burst time
for i in range(len(d)):
    WT.append(TAT[i] - d[i][1][1])
print(WT)

avg_WT = 0
for i in WT:
    avg_WT +=i
avg_WT = (avg_WT/n)
print(avg_WT)

avg_TAT = 0
for i in TAT:
    avg_TAT +=i
avg_TAT = (avg_TAT/n)
print(avg_TAT)

print("Process | Arrival | Burst | Exit | Turn Around | Wait |")
for i in range(n):
      print("   ",d[i][0],"   |   ",d[i][1][0]," |    ",d[i][1][1]," |    ",ET[i],"  |    ",TAT[i],"  |   ",WT[i],"   |  ")
print("Average Waiting Time: ",avg_WT)
print("Average Turnaround Time: ",avg_TAT)





