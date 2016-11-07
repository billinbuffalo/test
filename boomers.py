# Initial import and scrubbing of population/age group data

import csv

# The age group code representing the target analysis
#1	0-4
#2	5-9
#3	10-14
#4	15-19
#5	20-24
#6	25-29
#7	30-34
#8	35-39
#9	40-44
#10	45-49
#11	50-54
#12	55-59
#13	60-64
#14	65-69
#15	70-74
#16	75-79
#17	80-84
#18	85+
agegroupcode = 9

# CSV used for analysis
# https://pad.human.cornell.edu/counties/projections.cfm
# I'm using the 2025 worksheet exported as csv
myFile = open('/Users/bill/School/MSIT/Data/Projections2011.csv')
reader = csv.reader(myFile, delimiter=',')
# Skip the first line
next(reader, None)

# Arrays used to hold data
agegroup = []
pop2025 = []
totalpop = []

# Get the data for age group codes greater than or equal to AGEGROUPCODE
for row in reader:
    totalpop.append(row[14])
    if int(row[5]) >= agegroupcode:
        agegroup.append(row[6])
        pop2025.append(row[14])

myFile.close()

# Convert population values to Int
pop2025 = list(map(int, pop2025))
totalpop = list(map(int, totalpop))

# Print the age groups and their population
for a,b in zip(agegroup,pop2025):
    print (a,b)

# Total the sampled population and overall
Total = sum(pop2025)
allTotal = sum(totalpop)
print("Total population for age group code", agegroupcode,"and above: ",Total," Out of:", allTotal)
