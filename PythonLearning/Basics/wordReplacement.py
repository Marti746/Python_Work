# Word Replacement Program
# to help with the replace() method
def replaceWord():
    str = "Hello World, I am robo-man wow wow wow"
    words_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter word replacement: ")
    print(str.replace(words_to_replace, word_replacement))

replaceWord()