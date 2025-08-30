#Anagrams

#Solution

#With sorting
str1 = input("Enter a string : ").lower()
str2 = input("Enter string : ").lower()
sortS1 = ''.join(sorted(str1))
sortS2 = ''.join(sorted(str2))
if sortS1 == sortS2:
    print("Anagram")
else:
    print("Not an Anagram")

#Without Sorting
def getAnagram(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1)!=len(s2):
        return False
    count = {}
    for c in s1:
        if c!=" ":
            count[c] = count.get(c,0)+1
    for c in s2:
        if c not in count:
            return False
        count[c] -= 1
        if count[c]<0:
            return False
    return True
            
str1 = input("Enter a string : ")
str2 = input("Enter a string : ")
if getAnagram(str1,str2):
    print("Anagram")
else:
    print("Not an Anagram")
