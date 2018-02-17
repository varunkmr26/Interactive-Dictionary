import json
from difflib import get_close_matches

# We could use either of the two sources below
data = json.load(open('data.json'))
#data = json.load(open('dictionary.json'))

def dictionary(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word,data.keys()))>0:
		alternate = get_close_matches(word,data.keys())[0]
		yn = raw_input("We couldn't find a \'%s\'.Did you mean \'%s\' instead? Enter Y if yes, or N if no: " % (word,alternate))
		yn = yn.upper()
		if yn == "Y":
			return data[alternate]
		elif yn == "N":
			return "I'm sorry! The word doen't exist in our dictionary. Please double check it"
		else:
			return "We didn't understand your response."
	else:
		return "We couldn't find a match for your entry. Please double check the word."

word = raw_input("Please enter the word: ")
output = dictionary(word)
if type(output) == list:
	for response in output:
		print(response)
else:
	print(output)
