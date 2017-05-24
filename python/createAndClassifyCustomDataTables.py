import Orange

import pickle

## # Load the classifier object from file using pickle
print("Loading the classifier..")
c = pickle.load(open("..\\algorithm\\modelfile_orangev341.pkcls", "rb"))
print("Classifier loaded.")
print()

#################################
## creating data table from scratch

print("Example: Classifying data from scratch (creating own data table):")

# Data domain = stores a list of features, class(es) and
# meta attribute descriptors.
#
# While the domain description is stored within the packed classifier
# we can alternatively load the domain only from 
data_domain = pickle.load(open("..\\algorithm\\ludusdomain.pkl", "rb")) #

## Let us make some example user data:
# person a should be a philantropist who gets challenge #1 (index 0)
person_a = ['Philantropist', 'Low', 'high', 'low', '', '', '', '', 1, '', '', '', '', '', '', '', '']
# person b is a free spirit who gets challenge #2 (index 1)
person_b  =["Free Spirit"] + [i for i in range(16)]

# Create a Data Table from our user information:
user_data = [
        person_a,
        person_b
        ]
## alternatively, we could also use Orange.data.Table.from_list()
data_table = Orange.data.Table(data_domain, user_data)

# classify using CN2 classifier

result = c(data_table)

for user, challenge_index in zip(user_data, result):
        print("Person who is a", user[0], "get's challenge number", challenge_index+1)

