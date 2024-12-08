# 1.CheckIfTwoStringsAreAnagrams
#  Task:
#  Writeafunctionthatdeterminesif twostringsareanagramsofeachother.
#  TestCases:
#  1. Input:("listen","silent")→Output:True
#  2. Input:("triangle","integral")→Output:True
#  3. Input:("apple","pale")→Output:False
#  4. Input:("a","a")→Output:True
#  5. Input:("rat","car")→Output:False


def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

print(are_anagrams("rat", "car"))