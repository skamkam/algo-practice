# Name: Sarah Kam
# Peers: None
# References: https://en.wikipedia.org/wiki/List_of_knapsack_problems

def lumberSelection(prices:list, n:int) -> float:
    """
    Given a length of lumber and a list of prices for each cut-down plank by size,
    returns the best price you can get for that amount of lumber

    :param prices: (list) List of prices per each size of plank
    :param n: (int) Size of initial plank to be cut down
    :return : (float) Maximum price you can get for n amount of lumber

    >>> lumberSelection([0.25, 1.45, 0, 3.58, 0, 4.4, 0, 5.18, 0, 6.58, 0, 8.28], 12)
    10.74
    """
    # n by 1 array, each entry represents 1 foot dif
    # the previous best for each number is already in there
    # so each time we increase by 1 to k for example
    # only check the combos of 1 and k-1, 2 and k-2, etc
    matrix = [0] * n
    for i in range(n):
        current_max = prices[i] # the ith item
        for j in range(i):
            if (matrix[j] + matrix[i-j-1]) > current_max:
                current_max = matrix[j] + matrix[i-j-1]
        matrix[i] = current_max
    return matrix[n-1]

def getNumberOfWays(change_amount:int, bill_list:list) -> int:
    """
    Given some amount of cash to change into change, figure out the number of possible
    bill combinations that the cash can be changed into
    
    :param change_amount: (int) The amount of cash to change
    :param bill_list: (lst) A list of the bills that can be used in the change combinations
    :return : (int) A number representing the # of combos of bills that make up the change_amount

    >>> getNumberOfWays(3, [1, 2, 5, 10, 20, 50, 100])
    2
    >>> getNumberOfWays(6, [1, 2, 5, 10, 20, 50, 100])
    5
    """
    # Note: I could not get getNumberOfWays() to work properly. I did my best

    if change_amount <= 0:
        return 0     # make sure good input
    matrix = [0] * (change_amount + 1)
    matrix[0] = 1   # we want to intialize 0 -> 1 combo for easy calculation

    # fill in matrix
    for i in range(1, change_amount+1):
        #print("\ni is {} and represents the amount of change we have right now".format(i))
        # find biggest bill that applies
        biggest_bill_loc = 0
        for j in range(len(bill_list)):
            if i < bill_list[j]:
                biggest_bill_loc = j-1
                break
        #print("for round {}, biggest_bill_loc is {} and biggest bill is {}".format(i,biggest_bill_loc, bill_list[biggest_bill_loc]))    

        # calculate count for that entry
        count = 0
        for bill in bill_list[1:biggest_bill_loc+1]:
            dif = i - bill      # 7 - 5 = 2            
            #print("starting bill list loop, bill is {}, dif is {}".format(bill,dif))

            if dif in bill_list and dif > bill:     # if dif is 2, bill is 5
                count += matrix[dif]
                #print("no double counties, added {}, subtract 1".format(matrix[dif]))
                count -= 1      # subtract 1 for double count
            else:
                #print("dif is not in bill_list or dif < bill, adding {}".format(matrix[dif]))
                count += matrix[dif]
        count += 1  # for the all-ones combo
        matrix[i] = count
    return matrix[change_amount]
        

def main():
    lumber_prices = [0.25, 1.45, 0, 3.58, 0, 4.4, 0, 5.18, 0, 6.58, 0, 8.28]
    print(lumberSelection(lumber_prices, 12))

    bill_list = [1, 2, 5, 10, 20, 50, 100]
    print(getNumberOfWays(8, bill_list))

if __name__ == "__main__":
    main()