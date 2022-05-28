# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

wordstr=str(input('Enter First Word: '))
anagramstr=str(input('Enter Second Word: '))

words=wordstr.lower()
anagrams=anagramstr.lower()


def find_anagram(word,anagram):
    # [assignment] Add your code here

    if sorted(word)== sorted(anagram):
        return True
    else:
        return False


print(find_anagram(words,anagrams))
