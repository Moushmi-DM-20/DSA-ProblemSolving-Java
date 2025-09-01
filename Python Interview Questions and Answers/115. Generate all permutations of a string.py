#Generate all permutations of a string

#Solution
def permute(s,step = 0):
    if len(s)==step:
        print(''.join(s))
        return 
    for i in range(step,len(s)):
        scopy = [c for c in s]
        scopy[step],scopy[i]=scopy[i],scopy[step]
        permute(scopy,step+1)
    
s = input("Enter : ")
permute(list(s))
