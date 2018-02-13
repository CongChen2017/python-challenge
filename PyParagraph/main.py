# # get a paragraph from input and store as sting
	
# paragraph = input("please input your paragraph here: ")


# read text files from a folder

import os

# specify folder name

folderName = 'raw_data'

# Loop through files in target folder

fileNames = os.listdir(folderName)

for filename in fileNames:

	# set file path

	textpath = os.path.join(folderName, filename)

	# read text files

	with open(textpath, newline='') as textfile:

		paragraph = ''.join(textfile.readlines())

	# print title of the count result

	print("")
	print("Paragraph Analysis")
	print("-------------------")

	# split paragraph as words

	import re
	word = re.split("\s|(?<!\d)[.,][,.](?!\d)", paragraph)


	# print out word count
	print("Approximate Word Count: " + str(len(word)))

	# split paragraph as sentence

	sentence = re.split(r'[.!?]+', paragraph)

	# print out sentence count
	print("Approximate Sentence Count: " + str(len(sentence)-1))


	# initiate a list of letters

	letter = []

	# loop paragraph, find letters and add to list

	for char in list(paragraph):

		if char.isalpha():

			letter.append(char)

	# print out average letter count / word
	print("Average Letter Count: " + str("{0:.2f}".format(len(letter)/len(word))))

	# print out Average sentence length
	print("Average Sentence Length: " + str("{0:.1f}".format(len(word)/(len(sentence)-1))))
	print("")


