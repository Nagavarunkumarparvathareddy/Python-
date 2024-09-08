import math
print('''
Approach 2 : Inputs Values in Function head : NO
             Returns Values in              : No
**************************************************************************     
Input   : Function def 
Process : Function def = fun heading + fun body
Output  : Function def
''')
def circle():
    radius = float(input('Enter radius of circle: '))
    area = math.pi*(radius**2)
    circumference = 2*math.pi*radius
    print('Area: ',area)
    print("circumference: ",circumference)
circle()
