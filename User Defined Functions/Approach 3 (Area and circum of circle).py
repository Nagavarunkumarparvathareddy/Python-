import math
print('''
Approach 3: Inputs Values in Function head : YES
            Returns Values in              : No
**************************************************************************     
Input   : Function call 
Process : Function def = fun heading + fun body
Output  : Function def
''')
def circle(r):
    area = math.pi*(r**2)
    circum = 2*math.pi*r
    print(area)
    print(circum)
r = float(input('Enter radius of circle: '))
circle(r)
