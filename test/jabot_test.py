import random

random.seed(12)

length_of_file = 6
index_array = []

quote_file_name = "test_responses.txt"
# open file
qfile = open(quote_file_name, "r")

for i in range(length_of_file):
	index_array.append(0)	# 0 for unused quote
qfile.close()
cont = input("press enter to continue. press q to quit\n> ")
while cont != 'q':
    qfile = open(quote_file_name, "r")
    quote_index = random.randint(0,length_of_file-1)
    while index_array[quote_index] == 1:
    	quote_index = random.randint(0,length_of_file-1)
    print("QI =", quote_index)
    quote = qfile.readline()
    i = 1
    while i <= quote_index:
        quote = qfile.readline()
        i += 1
    print(quote)
    # mark index as used
    index_array[quote_index] = 1
    print("IA =", index_array)
    # reset if all quotes used up
    reset = True
    for item in index_array:
    	if item == 0:
    		reset = False
    print("reset =", reset)
    if reset:
    	for i in range(len(index_array)):
    		index_array[i] = 0
    cont = input("press enter to continue. press q to quit\n> ")
    qfile.close()
