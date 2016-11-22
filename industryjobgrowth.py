import csv, sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE projections (SOC, Change, Industry);") # use your column names here
cur.execute("CREATE TABLE codelookup (Code, Occupation);") # use your column names here

OccupationCodesFile = open('/Users/bill/School/MSIT/Data/occupationcodes.csv')
codelookup = csv.DictReader(OccupationCodesFile, delimiter=',')

ProjectionsFile = open('/Users/bill/School/MSIT/Data/Long_Term_Occupational_Projections.csv')
projections = csv.DictReader(ProjectionsFile, delimiter=',')

    # csv.DictReader uses first line in file for column headings by default
    #dr = csv.DictReader(fin) # In DictReader the comma is default delimiter

for row in codelookup:
    temp = [(i['Code'], i['Occupation']) for i in codelookup]
    cur.executemany("INSERT INTO codelookup (Code, Occupation) VALUES (?, ?);", temp)
    con.commit()

for row in projections:
    temp2 = [(i['SOC'], i['Change']) for i in projections]
    cur.executemany("INSERT INTO projections (SOC, Change) VALUES (?, ?);", temp2)
    con.commit()


for row in cur.execute('Select SOC from projections'):
    cur.executescript("UPDATE projections set Industry = SUBSTR(SOC,3,2)")
    con.commit

cur.executescript("DELETE from projections WHERE Industry = '00'")
con.commit


IndustryAndTotalChange = []

for row in cur.execute('SELECT codelookup.Occupation as Code, SUM(projections.Change) as Total FROM projections '
                      'INNER JOIN codelookup ON codelookup.Code=projections.Industry GROUP BY codelookup.Occupation '
                      'ORDER BY SUM(projections.Change) DESC'):
    IndustryAndTotalChange.append(row)

for row in cur.execute('SELECT SUM(Change) FROM projections'):
    TenYearTotalGrowth = int(row[0])

for row in IndustryAndTotalChange:
    print(row)

print("Ten Year Projected Job Growth")
print('Total Job Growth: ',TenYearTotalGrowth)
TopFiveTotalChange = IndustryAndTotalChange[0][1] + IndustryAndTotalChange[1][1] + IndustryAndTotalChange[2][1] + IndustryAndTotalChange[3][1] + IndustryAndTotalChange[4][1]
print('Top Five Industries Total Job Growth: ',TopFiveTotalChange)
TenYearMinusTopFive = TenYearTotalGrowth - TopFiveTotalChange
print('Remainder: ',TenYearMinusTopFive)

import matplotlib.pyplot as plt

labels = [IndustryAndTotalChange[0][0], IndustryAndTotalChange[1][0], IndustryAndTotalChange[2][0], IndustryAndTotalChange[3][0], IndustryAndTotalChange[4][0], 'All Others']
sizes = [IndustryAndTotalChange[0][1], IndustryAndTotalChange[1][1], IndustryAndTotalChange[2][1], IndustryAndTotalChange[3][1], IndustryAndTotalChange[4][1], TenYearMinusTopFive]
patches, texts = plt.pie(sizes, shadow=True, radius=.5)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.title('10 Year Job Growth By Industry in NYS')
#plt.tight_layout()
plt.show()



con.close()
ProjectionsFile.close()
OccupationCodesFile.close()

