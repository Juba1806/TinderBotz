'''
Created by Frederikme (TeetiFM)
Examples of usage are demonstrated in this template.py file
'''

from bot import *
import constants

email = constants.email
password = constants.password
import string
import random
def name_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == "__main__":

    # creates instance of bot
    bot = TinderBot()

    # login using your google account
    bot.loginUsingGoogle(email=email, password=password)

    # alternatively you can use
    bot.loginUsingFacebook(email=email, password=password)

    # spam likes
    bot.like(amount=0)
    # spam dislikes
    bot.dislike(amount=0)
    # spam superlikes
    bot.superlike(amount=0)

    # There are 2 types of matches:
    #  - new matches with whom you haven't interacted yet
    #bot.getNewMatches()
    #  - matches with whom you've already chatted
    #bot.getChattedMatches()
    # - or simply get all matches (new+chatted)
    matches = bot.getAllMatches()

    # print all matches name + their corresponding id
    for match in matches:
        break
        #print("{:>20}   {:>50}".format(match.getName(), match.getID()))

    # opening a chat can be done by their id
    # bot.openChat(id=matches[1].getID())

    # send chats to the user
    #bot.sendMessage(toID=matches[1].getID(), message="hey")

    # possibilty to unmatch your match
    #bot.unMatch(id="kzifzuofy")

    # get a url to image
    bot.getImage(matches[1].getID())
