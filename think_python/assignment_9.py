
# Write a program that reads words.txt and prints only the words with more than 20
# characters (not counting whitespace)

fin = open('words.txt') 

for line in fin:
    word = line.strip() 
    if len(word) > 20:
        print(word[0:20])
        
# Exercise 9.2. In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that
# does not contain the letter “e.” Since “e” is the most common letter in English, that’s not easy to
# do.
# In fact, it is difficult to construct a solitary thought without using that most common symbol. It is
# slow going at first, but with caution and hours of training you can gradually gain facility.
# All right, I’ll stop now.
# Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in
# it.
# Modify your program from the previous section to print only the words that have no “e” and compute the
# percentage of the words in the list have no “e.”


    
def has_no_e(word):
    for letter in word:
        if letter == 'e': 
            return False
    return True


def find():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if has_no_e(word):
            print(word)
find()

# Give me a word with three consecutive double letters. I’ll give you a couple of words
# that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
# would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-ip-p-i. 
# If you could take out those i’s it would work. But there is a word that has three
# consecutive pairs of letters and to the best of my knowledge this may be the only word.
# Of course there are probably 500 more but I can only think of one. What is the word?
       
    
from __future__ import print_function, division


def is_triple_double(word):
  
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            i = i + 1 - 2*count
            count = 0
    return False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')





            


     
              
               