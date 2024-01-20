"""
Name: Collin Nunnally
Class: CSE-111
Comments:

"""
import random

noun = ["bird", "dog", "cat", "mouse", "man", "fox"]
plural_nouns = ["birds", "dogs", "cats", "mouses", "men", "foxes"]
past = ["ran", "fought", "biked", "swam", "climbed"]
present = ["running", "fighting", "biking", "swimming", "climbing"]
future = ["will run", "will fight", "will bike", "will swim", "will climb"]
article = ["a", "the", "one"]
articles = ["many", "some", "few"]
preposition = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

ran_number = random.choice(range(0,3,1))

def get_determiner(ran_number):
    if ran_number == 1:
        p_determiner = random.choice(article)
    else:
        p_determiner = random.choice(articles)
    return p_determiner

def get_noun(p_x):
    if ran_number == 1:
        p_noun = random.choice(noun) 
    else:
        p_noun = random.choice(plural_nouns)
    return p_noun

def get_verb():
    if ran_number == 0:
        p_verb = random.choice(past)
    if ran_number == 1:
        p_verb = random.choice(present)
    if ran_number == 2:
        p_verb = random.choice(future)
    return p_verb 

def get_preposition():
    p_preposition = random.choice(preposition)
    return p_preposition

def get_prepositional_phrase(ran_number):
    p_preposition_2 = get_preposition()
    p_determiner_2 = get_determiner(ran_number)
    p_noun_2 = get_noun(ran_number)
    p_prep_phrase = f"{p_preposition_2} {p_determiner_2} {p_noun_2}"
    return p_prep_phrase

def make_sentence(p_determiner, p_noun, p_verb, p_prep_phrase):
    p_sentence = f"{p_determiner.capitalize()} {p_noun} {p_verb} {p_prep_phrase}."
    return p_sentence

def main():
    p_determiner = get_determiner(ran_number)
    p_noun = get_noun(ran_number)
    p_verb = get_verb()
    p_prep_phrase = get_prepositional_phrase(ran_number)
    p_sentence = make_sentence(p_determiner, p_noun, p_verb, p_prep_phrase)
    print(p_sentence)
main()