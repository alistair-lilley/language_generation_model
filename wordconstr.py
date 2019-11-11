'''                 WORD CONSTRUCTOR                    '''

import random

# Generates a given number of words given syllables and number of syllables per word
def genWords(syls, sylnum, numwords):
    # Sets up a set for the words (set for faster lookup)
    words = set()
    # Sets up a maximum number of words possible, based on possible combination count of syllables
    max = len(syls)**sylnum
    for i in range(numwords):
        # Breaks if all possible words have been generated
        if i == max:
            break
        # Create word and keep recreating as long as the word does not exist in the set
        word = ''.join([random.choice(syls) for syl in range(sylnum)])
        while word in words:
            word = ''.join([random.choice(syls) for syl in range(sylnum)])
        # add word to set
        words.add(word)
    return words

# Makes words given a number of syllables and a number of words to make
def makeWords(dir, numSyls, numwords):
    words = []
    syls = [line.strip() for line in open(dir+"/outputs/syllables.txt")]
    # Defines syllable level weights
    if numSyls == 1:
        sylstats = [1]
    elif numSyls == 2:
        sylstats = [0.22, 0.78]
    elif numSyls == 3:
        sylstats = [0.15, 0.51, 0.34]
    else:
        sylstats = [1/numSyls for i in range(numSyls)]
    # Sets up exact wordcount for each syllable level based on syllable level weights and total word count
    # This will not necessarily yield total word count exactly
    wordnums = sylstats
    for i in range(len(sylstats)):
        wordnums[i] = int(numwords//(1/sylstats[i]))
    # Generate words for each syllable level
    for sylnum in range(numSyls):
        words += genWords(syls, sylnum+1, wordnums[sylnum])
    wordfile = open(dir+"/outputs/words0.txt",'w')
    wordfile.write('\n'.join(words))
    wordfile.close()


if __name__ == "__main__":
    makeWords('L2',2,100)
    print(100)
    makeWords('L2',2,500)
    print(500)
    makeWords('L2',2,1000)
    print(1000)
    makeWords('L2',3,10000)
    print("three syllables")