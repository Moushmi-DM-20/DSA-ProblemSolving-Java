# Angle between two sides

#Solution
import math

def angle(a,b):
    c = math.atan2(a,b)
    return math.degrees(c)

input1 = int(input("Enter an angle value : "))
input2 = int(input("Enter an angle value : "))
print(angle(input1,input2))
