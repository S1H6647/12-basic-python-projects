# String concatentation 

# Few ways to do this:

# Youtuber = "Mr.beast"
# print("Subscribe to"+Youtuber)
# print("Subscribe to {}".format(Youtuber))
# print(f"Subscribe to {Youtuber}") # "F string"

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Programming is so {adj}! It makes me so excited all the time because I love to {verb1}.\
Stay hydrated and {verb2} like you are {famous_person}."

print(madlib)
