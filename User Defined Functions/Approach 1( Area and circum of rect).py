print('''
Approach 1 : Inputs Values in Function call : Yes
             Returns Values in              : Yes
**************************************************************************     
Input   : Function call 
Process : Function def = fun heading + fun body
Output  : Function call
''')
def rectangle(l,w):
    area = l*w
    circum = 2*(l+w)
    return area,circum
l = float(input('Enter length of rectangle: '))
w = float(input('Enter width of rectangle: '))
result = rectangle(l,w)
print(f'Area of Rectangle = {result[0]}')
print(f'circumference of Rectangle = {result[1]}')
