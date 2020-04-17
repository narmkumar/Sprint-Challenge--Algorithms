'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


# def count_th(word): PSEUDOCODE:

# if word length is < 2:
#   return 0

# if the word is == "th"
#   return 1

# If the word has "th" inside of it:
# increase the return value by 1
# run the initial function once again recursively
# return the total number of times "th" is in a string!
# return 0 once no more


def count_th(word):
    # Base Case
    if len(word) < 2:
        return 0
    elif word == "th":
        return 1

    elif "th" in word:
        new_word = word.find("th") # Find goes through the indicies in order to find the first occurence of the substring!
        return 1 + count_th(word[new_word + 2:]) ## recursively call function
    else:
        return 0

print(count_th("askdlfjadsftheweather"))
