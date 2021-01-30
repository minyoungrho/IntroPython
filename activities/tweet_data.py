import json

# Create a new file called 'tweet_data.py'
# and create a function called "load_tweets".
# The function should have one parameter:
# a string which is the relative path of a
# file in "json lines" format.
#
# The function should open that file and
# parse each line as JSON, returning a
# list of dictionaries.

def load_tweets(x_str):
    y = json.loads(x_str)
    return y

# Twitter records the language of each tweet in
# a key called "lang". The language is represented
# by a 2-character code recorded as a string,
# i.e.: "en" or "ca" or "es"
#
# Create a function called "get_language_counts"
# which takes a list of "tweets" (dictionaries)
# and returns a dictionary where the keys are
# language codes ("es", "ca", "en") and the
# values are integers representing the number
# of tweets in that language.
#
# For example: { 'es': 5, 'ca': 3 }



def get_language_counts(x_dict):
    langlist = []
    for elem in D:
        langlist.append(elem['lang'])
    return {x:langlist.count(x) for x in langlist}



D = [{'lang': 'es', 'content': 'hello' },
     {'lang':'en'},
     {'lang':'es'}]

get_language_counts(D)
