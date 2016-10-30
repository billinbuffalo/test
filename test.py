# testing

# print('hello world')

f = open("/Users/bill/School/MSIT/Data/data/SFHFCLData.csv")

# arrays
town = []
state = []
zipcode = []

for line in f:
    if "***" not in line:
        splitline = line.split(',')
        if len(splitline[0]) < 20:
            town.append(splitline[0])
            state.append(splitline[1])
            zipcode.append(splitline[2])

    # print (splitline)


#    print(line)

print(town,zipcode)