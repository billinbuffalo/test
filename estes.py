# Another test  Following Dr. Estes

import csv
import numpy as np
import matplotlib.pyplot as plt

myFile = open('/Users/bill/School/MSIT/Data/201630-CIS512-4600/testFile.csv','rt')

reader = csv.reader(myFile)

myList = []

for row in reader:
    myList.append(row)

myFile.close()

# print(myList)

myArray = np.asarray(myList)

bugsInd = np.flatnonzero(myArray[0,:]=='bugs')
bugs = myArray[1:,bugsInd].astype(np.float)

pointsInd = np.flatnonzero(myArray[0,:]=='points')
points = myArray[1:,pointsInd].astype(np.float)

# print (bugs)
# print (points)

myFit = np.polyfit(bugs.squeeze(),points.squeeze(),1,None,True,None,True)

frogPred = myFit[0][0]*bugs+myFit[0][1]

fig_myFit = plt.figure()
ax_myFit = fig_myFit.add_subplot(111)
bugsvspoints = ax_myFit.plot(bugs,points,'o',color = 'r',label = 'Original Data')
linearFit = ax_myFit.plot(bugs,frogPred,color = 'k',label = 'Linear Fit')
ax_myFit.grid(True)
ax_myFit.set_xlabel('bug units')
ax_myFit.set_ylabel('point units')
ax_myFit.set_title('bugs vs. point')
ax_myFit.legend()




# print(len(bugs))


