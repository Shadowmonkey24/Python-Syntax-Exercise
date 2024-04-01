
def print_upper_words(words, must_start_with):
    #  Filter the list of words one at a time
    for word in words:
        for letter in must_start_with:
            #  Check if the current word starts with the letter specified by 'must_start_with'
            if letter == word[0]:
                # If they match it will print the uppercase version of the word
                print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})