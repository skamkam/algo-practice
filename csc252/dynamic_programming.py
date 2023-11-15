def longest_common_substr(word_a:str, word_b:str) -> str:
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

def longest_common_subseq(word_a:str, word_b:str) -> str:
    """
    Finds the longest common subsequence between two words
    """
    word_a = word_a.lower()
    word_b = word_b.lower()
    
    matrix = []
    for i in range(len(word_a)):        # create the matrix
        b = [0] * len(word_b)
        matrix.append(b)

    for i in range(len(word_a)):        # fill in values for matching letters in matrix
        for j in range(len(word_b)):    # propagate any matches down/right along matrix
            if word_a[i] == word_b[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                prev_row = matrix[i-1][j] if i > 0 else 0
                prev_col = matrix[i][j-1] if j > 0 else 0
                matrix[i][j] = max(prev_row, prev_col)

    longest_subseq_len = matrix[len(word_a)-1][len(word_b)-1]
    subseq = ""
    curr_r = len(word_a)-1
    curr_c = len(word_b)-1
    for i in range(longest_subseq_len):     # unpack the matrix to find the subsequence
        # scoot up along rows and left along cols to find where the next match is
        while curr_r > 0 and matrix[curr_r][curr_c] == matrix[curr_r-1][curr_c]:
            curr_r -= 1
        while curr_c > 0 and matrix[curr_r][curr_c] == matrix[curr_r][curr_c-1]:
            curr_c -= 1
        subseq = word_a[curr_r] + subseq
        curr_r -= 1
        curr_c -= 1
    return subseq

def calculate_knapsack(items, values, weights, max_weight):
    """
    Find the best items to put in a knapsack: each item has value, weight; knapsack has a given max_weight
    """
    def knapsack(i: int, j: int):
        """
        Recursive helper function to return the knapsack/what's currently in it
        """
        if i == 0:
            return {}
        if cell[i][j] > cell[i-1][j]:
            return {items[i-1]}.union(knapsack(i-1,j-weights[i-1]))
        else:
            return knapsack(i-1,j) 
        
    # Start of calculate_knapsack code:    
    # We are going to add a zero items (row) and zero weights (column)
    #   because Python lists allow for negative indexing.
    #   It also makes the problem slightly easier to solve.
    row_len = len(items) + 1
    col_len = max_weight + 1
    cell = []
    for i in range(row_len):
        row = [0] * col_len
        cell.append(row)
    
    #Note: The zero row/column already has zeros in it.
    for i in range(1, row_len):
        item_num = i - 1
        for w in range(1, col_len):
            # if current item is too heavy for the max weight we have right now,
            # take the value for the prev row and same max weight
            if weights[item_num] > w:
                cell[i][w] = cell[i-1][w]
            # else the cell is the max of the prev row/same max weight
            # or we update this cell and add this item: add value of current item,
            # and find the max value of the leftover space
            else:
                cell[i][w] = max(cell[i-1][w], cell[i - 1][w - weights[item_num]] + values[item_num])
    
    # #This is the maximum value you can store in the knapsack.
    # print(cell[row_len-1][col_len-1])
    # #Let's check our answer.
    # for i in range(len(cell)):
    #     print(cell[i])

    return knapsack(row_len-1, col_len-1)


def main():
    str1 = "monkeys"
    str2 = "dumkey is sus????"
    print(longest_common_substr(str1, str2))
    print(longest_common_subseq(str1, str2))    #xaybzci, yabqrcv

    items   = ['Guitar','Stereo','Laptop','iPhone']
    values  = [1500,3000,2000,2000]
    weights = [1,4,3,1]
    capacity = 4
    print(calculate_knapsack(items,values,weights,capacity))

main()