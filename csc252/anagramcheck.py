"""
09/22/2023 in-class exercise
Check if two strings are anagrams of each other

Input: 2 strings
Goal: Are they anagrams?
Output: Boolean

"bear", rabe" -> T
"goop", "pool" -> F
"", "" -> T
"mom123", "omm321" -> T

Assume alphanumeric characters (no spaces or special chars)
"""

def anagramcheck(str1, str2):
    a1 = [0] * 255
    a2 = [0] * 255
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        numlet1 = ord(str1[i])        # get ASCII for the character
        a1[numlet1] += 1         # iterate the # of that letter

        numlet2 = ord(str2[i])
        a2[numlet2] += 1
    if a1 == a2:                # element-wise comparison not addr-comparison (thanks Python!)
        return True
    return False

def main():
    print(anagramcheck("bear", "rabe"))         # T
    print(anagramcheck("goop", "pool"))         # F
    print(anagramcheck("mom123", "omm321"))     # T
    print(anagramcheck("", ""))                 # T
    print(anagramcheck("abc", "abcd"))          # F

if __name__ == "__main__":
    main()