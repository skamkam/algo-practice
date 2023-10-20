
def stringpermutation(s, letters):   # n is place in so_far
    """
    linked list
    base case 1 elt, insert it every poss spot in the existing word
    recursively call on each of those inserted versions with the letters
    """
    
    if len(letters) == 0:       # base case
        print(s)
    else:
        if len(s) == 0:
            stringpermutation(letters[0], letters[1:])
        else:
            for i in range(len(s)+1): # at every spot in s, insert letters[0]
                word = s[:i] + letters[0] + s[i:]
                stringpermutation(word, letters[1:])

stringpermutation("", "abc")    # abc acb bac bca cab cba