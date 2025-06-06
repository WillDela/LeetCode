'''
Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed. The sentence will contain only alphabetic characters and spaces to separate the words. If there is only one word in the sentence, the function should return the original string.

def reverse_sentence(sentence):
    pass
Example Usage:

sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)
Example Output:

"fluff with stuffed all cubby little tubby"
"Pooh"

split method


'''

def reverse(sentence):
  words = sentence.split()
  reversed_sentence = ""
  for i in range(len(words) - 1, -1, -1):
    reversed_sentence += words[i] + ' '
  return reversed_sentence

sentence = input("Enter a sentence: ")
print(reverse(sentence))

"""
def reverse_function(sentence):
  return ' '.join(sentence.split()[::-1]) #built in function in Python
  #print(split.reverse())
  


sentence = input("Enter a sentence: ")
print(reverse(sentence))

#sentence = "
#print(reverse_function(sentence))
"""
