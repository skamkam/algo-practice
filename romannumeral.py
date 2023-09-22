"""
Convert a roman numeral string to a number
"""

def romanToInt(s: str) -> int:
        ans = 0
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        addedLastInt = False
        i = 0
        while i < (len(s)-1):
            if roman[ s[i] ] < roman [ s[i+1] ]:
                if i == len(s)-2:
                    addedLastInt = True
                ans = ans + roman[ s[i+1] ] - roman[ s[i] ]
                i = i + 1   # skip ahead bc we compared the next one
            else:
                ans = ans + roman[ s[i] ]
            i = i + 1
        if addedLastInt != True:
            return ans + roman[ s[-1] ]
        return ans

def romanToIntBetter(s: str):
    ans = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(s)-1):
        if roman[s[i]] < roman[s[i+1]]:
            ans -= roman[s[i]]
        else:
            ans += roman[s[i]]
    ans += roman[s[-1]]
    return ans

print(romanToInt("XIV"))
print(romanToIntBetter("XIV"))