import math
print('''
Approach 1 : Inputs Values in Function call : Yes
             Returns Values in              : Yes
**************************************************************************     
Input   : Function call 
Process : Function def = fun heading + fun body
Output  : Function call
''')
def circle(radius):
    area = math.pi*(radius**2)
    circumference = 2*math.pi*radius
    return area,circumference
radius = float(input('Enter radius of circle: '))
result = circle(radius)
print(f'Area of circle :{result[0]}')
print(f'Circumference of circle : {result[1]}')
