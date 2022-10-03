import random


def sentence_generator():
    theString = "structure" # what it is trying to aim for
    options = "a b c d e f g h i j k l m n o p q r s t u v w x y z " # the options that it has
    options = options.split()# splits the options up
    options.append(' ')
    random_string = [random.choice(options) for i in range(len(theString))] # len returns the number of characters in the string. Random.choice() chooses a random letter from the alphabet.
    return random_string

def sentence_scorer(sentence):

#takes as input a sentence from sentence_generator
#and then evaluates how close to "to be or not to be that is the question" it is.

    score = 0
    theString = "structure"

# turns every character from the String into an element of a list
    theString2 = list(theString) 
    for i in range(len(theString)):
        if sentence[i] == theString2[i]:
            score += 1
            if score % 10 == 0:
                print(score)
        return score

def generator():
    high_score = 0
    while high_score != 9:
        x = sentence_generator()
        y = sentence_scorer(x)
        if high_score < y:
            high_score = y
            print("The new high score is %d" % (high_score))
            print(" The string is " + ' '.join(x))
    print ("Done!")
    
generator()
