"""
09/22/2023 in-class exercise
Check if all the characters in a string are unique characters

In: String
Goal: String Unique Char.
Out: T/F

"hello" -> F
"hi mom" -> F
"abcd" -> T
"this day go" -> F (spaces)
"""

def unique(in_str):
    """
    Time: O(n^2)    Space: O(n) because it's just the original string size
    """
    for i in range(len(in_str)):
        for j in range(i+1, len(in_str)):
            if in_str[i] == in_str[j]:
                return False
    return True

def unique_fast(in_str):
    """
    Time: O(n),     Space: O(n) because the list size is bounded and we can ignore it!
    """
    # to go faster, aim for just one loop
    # take advantage of the fact that this is ASCII
    # loop over each letter in in_str and see if it's in there already
    # if there are repeat letters return False else return True
    my_char = [0] * 256
    for letter in in_str:
        num_let = ord(letter)   # returns ASCII of that letter
        if my_char[num_let] == 1:
            return False
        else:
            my_char[num_let] = 1
    return True

def main():
    tests = ["hello", "abcd", "this day go", "hi mom"]  # expect F T F F
    for test in tests:
        print("test: " + test)
        print("unique:      " + str(unique(test)))
        print("unique fast: "+ str(unique_fast(test)))
        print()
    
    string = "test"
    string[0] = "a"
    print(string)

if __name__ == "__main__":
    main()


"""
INTERVIEW NOTES:
Talk out loud the whole time
Ask lots of clarifying questions to make sure we understand the problem
Come up with a bunch of test cases beforehand to help with understanding questions
iterate over basic solution and then optimized solution
"""