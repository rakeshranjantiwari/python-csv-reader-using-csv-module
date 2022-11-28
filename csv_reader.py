import csv
#open the csv file
#path should be full directory path ex: /home/username/directory/filename.csv
with open('full-directory-path/users.csv', mode='r') as csv_file:
    #read the CSV file
    csv_reader = csv.reader(csv_file)
    #read csv using DictReader class to show data in dictionary
    #csv_reader = csv.DictReader(csv_file)
    #display the contents of the CSV file
    for row in csv_reader:
        print(row)