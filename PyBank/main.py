
import os
import csv

# specify folder name

folderName = 'raw_data'

# Loop through files in target folder

fileNames = os.listdir(folderName)

for filename in fileNames:


	# set file path

	csvpath = os.path.join(folderName, filename)

	# initiate lists & variables

	date = []
	revenue = []
	change = [0]
	changesum = 0
	mostincr = 0
	mostdecr = 0
	totalrev = 0


	# read csv file

	with open(csvpath, newline='') as csvfile:

		csvreader = csv.reader(csvfile, delimiter=',')

		# skip the header row

		next(csvreader, None)

		# loop remaining rows and write data into lists

		for row in csvreader:

			date.append(row[0])
			revenue.append(row[1])

	# calcuate revenue change and write results to list change

	for i in range(0, len(revenue)-1):

		change.append(int(revenue[i+1]) - int(revenue[i]))

	# calculate total absolute monthly change, then average change
	# find the most increase and most decrease number as well
	# at last calculate total revenue

	for j in range(0, len(change)):

		if change[j] > mostincr:

			mostincr = change[j]

		if change[j] < mostdecr:

			mostdecr = change[j]

		changesum = changesum + abs(change[j])

		totalrev = totalrev + int(revenue[j])

	AveChange = int(changesum/(len(change)-1))

	# print out results in terminal

	print("")
	print("Financial Analysis")
	print("----------------------------")
	print("Total Months: " + str(len(date)))
	print("Total Revenue: $" + str(totalrev))
	print("Average Revenue Change: $" + str(AveChange))
	print("Greatest Increase in Revenue: " + date[change.index(mostincr)] + " ($" + str(mostincr) + ")")
	print("Greatest Decrease in Revenue: " + date[change.index(mostdecr)] + " ($" + str(mostdecr) + ")")

	# generate txt file for the report

	with open('Report_' + filename.split('.')[0] + '.txt', 'w', newline='') as textfile:

		textfile.write("Financial Analysis" + "\n")
		textfile.write("----------------------------" + "\n")
		textfile.write("Total Months: " + str(len(date)) + "\n")
		textfile.write("Total Revenue: $" + str(totalrev) + "\n")
		textfile.write("Average Revenue Change: $" + str(AveChange) + "\n")
		textfile.write("Greatest Increase in Revenue: " + date[change.index(mostincr)] + " ($" + str(mostincr) + ")" + "\n")
		textfile.write("Greatest Decrease in Revenue: " + date[change.index(mostdecr)] + " ($" + str(mostdecr) + ")")


