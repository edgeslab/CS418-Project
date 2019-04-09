import csv

# 0, 5, 7, 8, 11, 13, 17


counter = 0
with open("filtered.csv") as WebData:
    reader = csv.reader(WebData)
    # skip the first line of csv file, which is the header only
    next(reader)
    with open('dataFiltered.csv', mode='w') as finalData:
        finalCsv = csv.writer(finalData, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if int(row[17]) >= 2008 and int(row[17]) <= 2012:
                temp = [row[0], row[5], row[7], row[8], row[11], row[13], row[17]]
                finalCsv.writerow(temp)
                # print (row[0], row[5], row[7], row[8], row[11], row[13], row[17])
                counter = counter + 1
msg = "hello world"
print (counter)

