'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #base case
    #if the word is less than 2 characters, it cannot contain th, therefore will return 0 
    if len(word) < 2:
      return 0
    #run again, starting from the next char, and add 1 to document the 'th' found
    if word[:2] == 'th':
        return count_th(word[1:]) +1
    #basically keeps the recursion going even when a 'th' isnt found, until there are less than 2 chars left to check
    return count_th(word[1:])

print(count_th('abcdefthyz'))
