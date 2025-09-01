#Decompress a string

#Solution
def deCompress(s):
    string = ""
    for i in range(len(s)):
        c = s[i]
        ascii = ord(c)
        if 65<=ascii<=90 or 97<=ascii<=122:
            char = c
        elif 48<=ascii<=57:
            count = ord(c)-48
            string += char*count
    return string
    
s = input("Enter : ")
print(deCompress(s))
