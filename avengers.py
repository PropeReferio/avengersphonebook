#Using Visual Studio Code, Create an Object Oriented phone book that stores names, addresses 
# and phone numbers of of avengers. Store each avenger name as a key and their information 
# as values. Create a method that calls on a random avenger which should return their phone 
# number.

# This should be turned in on next Monday at 11:30am. Once completed, commit the finished code to GitHub and submit the link.
import random

class PhoneBook():

    def __init__(self, book = {}):
        self.book = book

    def addEntry(self, name, info): #Info is value, a list of address and phonenumber
        self.book[name] = info

    def callRandomHero(self):
        print(random.choice(list(bosbook.book.items())))

bosbook = PhoneBook()
bosbook.addEntry('Spiderman', ['123 Big Apple St.', '615-788-9366'])
bosbook.addEntry('The Flash', ['110 Blackburn Ave.', '720-538-9294'])
bosbook.addEntry('Iron Man', ['958 Sunset Cliffs Blvd.', '513-864-3421'])
bosbook.callRandomHero()