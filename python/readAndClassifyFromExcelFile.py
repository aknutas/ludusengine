import os.path # this is only for folder paths
import pickle
import Orange


## # Load the classifier object from file using pickle
print("Loading the classifier..")
c = pickle.load(open("..\\algorithm\\modelfile_orangev341.pkcls", "rb"))
print("Classifier loaded.")
print()


##
################################
#####the list of all rules in the classifier can be printed
####for r in c.rule_list:
####	print(r)
##
###################################
# Load the test (training) data from xlsx-file
data = Orange.data.Table.from_file("..\\algorithm\\training_set.xlsx")
# Classify the test data using the CN2 classifier
result = c(data)

# Print out the resulting classification for the test set
for item in zip(data, result):
        print("User type:", item[0][0], "gets challengee number", item[1])

