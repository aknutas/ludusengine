############
# IMPORTS
import random
import pickle
import Orange

############
# GLOBALS

# Start off by loading the classifier from binary file:
print("Loading the classifier..")
c = pickle.load(open("..\\algorithm\\modelfile_orangev341.pkcls", "rb"))

print("Classifier loaded.")
print()

# Load metadata for the classifier (also provided in a binary file): 
data_domain = pickle.load(open("..\\algorithm\\ludusdomain.pkl", "rb"))

#############
# Short names and descriptions for the variables (to ease reading):

challenge_short_names = ["", "Advise low skill user","Advise low skill user","Bob the Builder","Bob the Builder","Chat helper","Chat helper","Completionist","Conversationalist","Create a task","Deeper-Socialize-talk","Discovery","Doraemon","Doraemon","Doraemon","Doraemon++","Doraemon++","Fast helper","Fast helper","Fast helper","Get advice from high skill user","Get all from other team to help","Get discussion started","Get help","Get help","Involve all in discussion","Master explorer","Master reader","Master reader","Master student","Master student","Master student","Mutual help","Mutual help","Mutual help","Neil Armstrong","Night owl","Offer help","Offer help","Offer help","Offer help","Offer help","Point hoarder","Point Out","Publish solution","Publish solution","Publish solution","Publish solution","Read the Fine Manual","Remind for help","Sidekick","Sidekick","Sidekick","Socialize-act","Socialize-act","Socialize-talk","Solver","Star Trek; \"Go Where No Man Has Gone Before\"","Status Check","Status Check","Tactical Team-Up","Tactical Team-Up","Tactical Team-Up","Ultimate Achiever","Up to Date","Updator, the Master of Updates","Wikiperson","Wikiperson","You Know It","You Know It All" ]
challenge_descriptions = ["","Write in chat","Write in chat","Report a bug to chat","Report a bug to chat","Offer to help with other team task","Offer to help with other team task","Fill all fields in profile page","Carry out chat activity for at least 15 minutes","Task created","Check all other team members","Paste a web link to chat","Reply within 5 minutes of question","Reply within 5 minutes of question","Reply within 5 minutes of question","Reply within 5 minutes of question","Reply within 5 minutes of question","Offer help to other team under N minutes","Offer help to other team under N minutes","Offer help to other team under N minutes","Write in chat","Get all members from other team to help","Write something in chat","Get other team member to help","Get other team member to offer help","Write something in chat","Look each page available in the framework","Read all the tasks in all the teams","Read all the tasks in all the teams","Get other team member to offer help for High number questions","Get other team member to offer help for High number questions","Get other team member to offer help for High number questions","Help other team with task","Help other team with task","Help other team with task","See the hidden pages","Complete a task / submit an assignment at 3:30 am.","Offer help to other team","Offer help to other team","Offer help to other team","Offer help to other team","Offer help to other team","Raise your team to the top of the scoreboard","Paste this task to chat","Write to chat","Write to chat","Write to chat","Write to chat","Read the FAQ","Link the task to chat","Help other team to become highest ranked in your own team","Help other team to become highest ranked in your own team","Help other team to become highest ranked in your own team","Check all other team pages","Check all other team pages","Check all other team pages","Solve one own team task","Visit a page that has not been visited before","Read all your team member's tasks","Read all your team member's tasks","Work with other team to raise them up to second position","Work with other team to raise them up to second position","Work with other team to raise them up to second position","Complete all the metabadges first","Check the scoreboard x10","Check the scoreboard x100","Paste wikilinks within 10 minutes of new tasks","Paste wikilinks within 10 minutes of new tasks","Reply within 5 minutes of question","Reply within 5 minutes of question"]


#############
# Helper function that asks questions in our text based adventure:

def ask(variables, question="", question_shortname="", choices=[]):
    """docstring """

    # append a question mark to the question, if it has none
    q = question if "?" in question else question + "?"

    # append the question shortname to the prompt
    q = q + " ('" + question_shortname + "')"

    # append the selectable choices to the prompt
    q = q + " (" + "/".join(choices) + "): "

    # ask questions untill a valid answer is given
    while True:
        inp = input(q)
        if inp in choices:
            break
        else:
            print("Please answer with:", "/".join(choices) )

    # add the answer to the 'user data' array
    variables.append(inp)    

###############
# Main program
print()
print("Welcome! This is the text based adaptive gamification challenge challenge!")
print()

# Array for our user data. 
answers = []

# Questions for the user
questions = [
    "What is the player type?",
    "What was the difficulty level",
    "How high was user skill level",
    "How high was other skill level",
    "How many own team open tasks were completed"
    ]

# Traverse through two lists:
# - the questions above
# - short names and valid answers to questions from metadata (data_domain.attributes)
# 
for question, metadata in zip(questions, data_domain.attributes):
    ask(answers, question, metadata.name, metadata.values)


# Create a Data Table from our user information
# (data.Table expects a two-dimensional list):
data_table = Orange.data.Table(data_domain, [answers])

# classify:
result = c(data_table)

# the classifier usually classifies an entire array at once
# but now we only have the one user to classify, so from our list of one
# select the first (and only) result. The result is zero-indexed, so +1
# to get the challenge number:
challenge_number = result[0] + 1

print()
print("Give the user gamification challenge number", str(challenge_number) + ":", end=" " )
print(challenge_short_names[challenge_number], end=" ")
print("(" + challenge_descriptions[challenge_number] + ")")
print()











