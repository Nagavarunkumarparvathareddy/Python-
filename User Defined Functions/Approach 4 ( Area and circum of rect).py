print('''
Approach 4: Inputs Values in Function head : NO
            Returns Values in              : YES
**************************************************************************     
Input   : Function def 
Process : Function def = fun heading + fun body
Output  : Function call
''')
def rect():
    l = float(input('Enter length of rectangle: '))
    w = float(input('Enter  width of rectangel: '))
    area = l * w
    circum = 2*(l+w)
    return area,circum
result = rect()
print(f'area : {result[0]}')
print(f'circum : {result[1]}')
