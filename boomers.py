# Initial import and scrubbing of population/age group data

import csv

# SOC vaiable.  For example, Health Care would be "29-." Change as appropriate for other industries
# Link to SOC codes:
# http://www.bls.gov/oes/current/oes_stru.htm
agegroupcode = 5

# CSV used for analysis
# https://pad.human.cornell.edu/counties/projections.cfm
# I'm using the 2025 worksheet exported as csv
myFile = open('/Users/bill/School/MSIT/Data/Projections2011.csv')
reader = csv.reader(myFile, delimiter=',')
# Skip the first line
next(reader, None)

# Arrays used to hold scrubbed data
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

# Print occupations and their net change in jobs
for a,b in zip(agegroup,pop2025):
    print (a,b)

# Total the population
Total = sum(pop2025)
allTotal = sum(totalpop)
print("Total population for age group code ", agegroupcode,"and above: ",Total," Out of: ", allTotal)
