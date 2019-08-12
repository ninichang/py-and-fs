import csv

def function1(filename, filename2):

    # f1 records the number of articles for each year
    f1 = open(filename, 'r', encoding = 'big5')
    txtLst = f1.readlines()
    f1.close()
    txtLst.pop(0) # remove the column names
    num_of_articles = []

    for i in range(len(txtLst)):
        txtLst[i] = txtLst[i].strip().split(',')
        num_of_articles.append(txtLst[i][1])
    
    # f2 lists all the urls into txtLst2
    f2 = open(filename2, 'r', encoding = 'big5')
    txtLst2 = f2.readlines()
    f2.close()
    txtLst2.pop(0) # remove the column names
    for i in range(len(txtLst2)):
        txtLst2[i] = txtLst2[i].strip().split('\n')

    # convert num_of_articles to integer and count the remainders
    # for i in range(len(num_of_articles)):
    #     num_of_articles[i] = int(num_of_articles[i])

    num_of_articles = [int(i) for i in num_of_articles]
    # divide the number of articles by 10 and loop print the numbers

    num_by_10 = [int(i) // 10 for i in num_of_articles]
    num_remaining = [int(i) % 10  for i in num_of_articles]

    newLst = []
    for i in range(len(num_by_10)):
        newLst.append([num_by_10[i], num_remaining[i]])

    numLst = []
    for i in newLst:
        for j in range(i[0]):
            numLst.append(10)
        if i[1] == 0:
            continue
        else:
            numLst.append(i[1])
    
    # use csvData(list) to store all the values
    csvData = []

    for index in range(len(txtLst2)):
        for times in range(1, numLst[index]+1):
            csvData.append([txtLst2[index], times])


    print(csvData[0:30])
    with open('FSurls.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvData)
    csvFile.close()

function1('FSsheet.csv', 'FSsheet_urls.csv')

