#Calculate number of vowels and consonants in a string

#Solution
def conVow(s):
    vowCount,conCount = 0,0
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for c in s:
        if c in vowels:
            vowCount +=1
        else:
            conCount +=1
    print("Vowel Count : ",vowCount)
    print("Consonant Count : ",conCount)

s = input("Enter a string : ")
conVow(s)
