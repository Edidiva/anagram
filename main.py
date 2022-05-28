# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
def find_anagram(word, anagram):
    x = sorted(word)
    y = sorted(anagram)
    if x == y :
         print(word, "and", anagram, "are anagrams.")
         return True
    else:
        print(word, "and", anagram, "are not anagrams." )
        return False
print(find_anagram("ate", "eat"))

    # [assignment] Add your code here


