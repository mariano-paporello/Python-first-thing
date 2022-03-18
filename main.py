"""
This program generates passages that are generated in mad-lib format
Author: Katherin
"""

# The template for the story
print ("The madlib has started")

name = input("Enter a name: ")
adjetive1 = input("Enter a crazy adjetive: ")
adjetive2 = input("Enter another crazy adjetive: ")
adjetive3 = input("Enter other crazy adjetive: ")
verb = input("Enter a crazy verb: ")
noun1 = input("Enter a crazy noun: ")
noun2 = input("Enter another crazy noun: ")
animal = input("Enter a animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
hero = input("Enter a Superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")

STORY = "This morning %s woke up feeling %s . 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world." % ( name, adjetive1, adjetive2, animal, food, verb, noun1, fruit, adjetive3, name, hero, name, country, name, dessert, name, year, noun2)

print (STORY)
