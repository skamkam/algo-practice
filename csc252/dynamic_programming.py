def longest_common_substr(word_a, word_b):
    """
    Finds the longest common substring 
    """
    word_a = word_a.lower()
    word_b = word_b.lower()
    
    matrix = []
    for i in range(len(word_a)):
        b = [0] * len(word_b)
        matrix.append(b)
    # matrix = [[0] * len(word_b)] * len(word_a) -> doesn't work, all the inside lists are the same object and python updates them all at the same time
    for i in range(len(word_a)):
        for j in range(len(word_b)):
            if word_a[i] == word_b[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j-1] + 1

    longest_substr_len = 0
    longest_substr_location = (0,0)
    for i in range(len(word_a)):
        for j in range(len(word_b)):
            if matrix[i][j] > longest_substr_len:
                longest_substr_len = matrix[i][j]
                longest_substr_location = (i,j)
    
    r = longest_substr_location[0]
    c = longest_substr_location[1]
    substr = ""
    while matrix[r][c] > 0:
        substr = word_a[r] + substr
        r -= 1
        c -= 1
    return substr

def longest_subsequence(word_a, word_b):
    # check all diagonals until hit a number or one of the indices is 0
    word_a = word_a.lower()
    word_b = word_b.lower()
    
    matrix = []
    for i in range(len(word_a)):
        b = [0] * len(word_b)
        matrix.append(b)
    # matrix = [[0] * len(word_b)] * len(word_a) -> doesn't work, all the inside lists are the same object and python updates them all at the same time
    for i in range(len(word_a)):
        for j in range(len(word_b)):
            if word_a[i] == word_b[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    # go diagonal up left until reach a non-zero number, or indices 0
                    matrix[i][j] = matrix[i-1][j-1] + 1

    longest_substr_len = 0
    longest_substr_location = (0,0)
    for i in range(len(word_a)):
        for j in range(len(word_b)):
            if matrix[i][j] > longest_substr_len:
                longest_substr_len = matrix[i][j]
                longest_substr_location = (i,j)
    
    r = longest_substr_location[0]
    c = longest_substr_location[1]
    subseq = ""
    while matrix[r][c] > 0:
        subseq = word_a[r] + substr
        r -= 1
        c -= 1
    return subseq


print(longest_common_substr("monkey", "dumkey is sus?????"))

"""
longest subsequence: in order and can have letters between them
xaybzci, yabqrcv -> abc is the longest subsequence
how to change code so that we have the longest subsequence
"""