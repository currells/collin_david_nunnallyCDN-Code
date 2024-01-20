import random

word = ['bird', 'dog', 'cat', 'mouse', 'man', 'fox']
words = ['birds', 'dogs', 'cats', 'mouses', 'men', 'foxes']
verbs = ['ran', 'fought', 'biked', 'swam', 'climbed']
article = ['a', 'the', 'one']
articles = ['many', 'some', 'few']

def get_determiner():
    number = random.choice(range(0,2,1))
    if number == 1:
        determiner = random.choice(article)
        x = 1
    else:
        determiner = random.choice(articles)
        x = 2
    return determiner, x

def get_noun(x):
  noun = random.choice(word) if x == 1 else random.choice(words)
  return noun

def get_verb():    
    verb = random.choice(verbs)
    return verb 

def make_sentence(determiner, noun, verb):
    sentence = f'{determiner.capitalize()} {noun} {verb}.'
    return sentence

def main():
    determiner, x = get_determiner()
    noun = get_noun(x)
    verb = get_verb()
    sentence = make_sentence(determiner, noun, verb)
    print(sentence)
main()