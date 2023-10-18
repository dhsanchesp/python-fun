
class AnagramFunction:

    def isAnagram(self, firstString, secondString):
        if sorted(firstString) == sorted(secondString):
            return True;
        else:
            return False;

if __name__ == '__main__':
    firstString = input('Enter first string: ')
    secondString = input('Enter second string: ')

    solution = AnagramFunction().isAnagram(firstString, secondString)

    if solution:
        print("The two String are an anagram of each other.")
    else:
        print("These strings are not an anagram of each other")