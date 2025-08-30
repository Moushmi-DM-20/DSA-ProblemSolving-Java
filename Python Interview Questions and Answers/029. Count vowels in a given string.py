#Count vowels in a given string

#Solution
def countVowels(s):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count 
    
S = input("Enter a sentence : ")
print("Count",countVowels(S))
