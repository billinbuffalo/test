# Initial import and scrubbing of long-term job projections in New York State

import csv

# SOC vaiable.  For example, Health Care would be "29-." Change as appropriate for other industries
# Link to SOC codes:
# http://www.bls.gov/oes/current/oes_stru.htm
SOC = "29-"

# CSV used for analysis
# https://data.ny.gov/Economic-Development/Long-Term-Occupational-Projections/pqm4-9qqb
myFile = open('/Users/bill/School/MSIT/Data/Long_Term_Occupational_Projections.csv')
reader = csv.reader(myFile, delimiter=',')

# Arrays used to hold scrubbed data
Occupation = []
Change = []

# Get only specific SOCs and their change projections for jobs
for row in reader:
    if SOC in row[2]:
        Occupation.append(row[3])
        Change.append(row[6])

myFile.close()

# Convert change values to Int
Change = list(map(int, Change))

# Print occupations and their net change in jobs
for a,b in zip(Occupation,Change):
    print (a,b)

# Total the net change
Total = sum(Change)
print("Total projected SOC:",SOC," job additions for New York State in the next ten years: ",Total)
