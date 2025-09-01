#Write a method to remove given character from a given string

#Solution
def charRemove(s,c):
    result = ""
    for i in s:
        if i!=c:
            result+=i
    return result

s = input("Enter a string : ")
ch = input("Enter a character to remove : ")
print(charRemove(s,ch))
