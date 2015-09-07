"""settings.sample.py - Module for storing settings for destroyer"""


#######################
# Twitter Integration #
#######################

# Put your Twitter API keys and secrets here
# Make a Twitter app at dev.twitter.com and add the API keys here.
# Be sure to give your app both read and write access.
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

########################
# Facebook Integration #
########################

facebook_access_token = ''

########################
# General              #
########################

question_prompts = [
        'Would you like to cleanse {name} from your existence?',
        'Are you ready to abolish ({name}) from your life?',
        'Would you like to unfollow the name that must not be mentioned ({name})?',
        'Are you not entertained?! Will {name} go?',
        'Does {name} irk you? Would you like rid them of your online life?',
]

insult_prompts = [
        "May the flies of a thousand camels infest the social feed of {name}",
        'Be gone {name}, foul demon spawn!',
        'Banish thyself to the fiery depths of hades, {name}!',
        'How does it feel to be worth absolutely nothing? It feels like a typical day for {name}.',
        'In life and death, {name} was worthless. Let it stay that way.',
]

