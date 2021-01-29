#
# 1)
# Create a new file called 'tweet_data.py'
# and create a function called "load_tweets".
# The function should have one parameter:
# a string which is the relative path of a
# file in "json lines" format.
#
# The function should open that file and
# parse each line as JSON, returning a
# list of dictionaries.



#
# 2)
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
