import math
print('''
Approach 4: Inputs Values in Function head : NO
            Returns Values in              : YES
**************************************************************************     
Input   : Function def 
Process : Function def = fun heading + fun body
Output  : Function call
''')
def circle():
    r = float(input('Enter radius of circle: '))
    area = math.pi*(r**2)
    circum = 2*math.pi*r
    return area,circum
result = circle()
print(f'area : {result[0]}')
print(f'circum : {result[1]}')
