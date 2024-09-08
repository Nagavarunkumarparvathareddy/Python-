print('''
Approach 2: Inputs Values in Function head : NO
            Returns Values in              : No
**************************************************************************     
Input   : Function def 
Process : Function def = fun heading + fun body
Output  : Function def
''')
def rectangle():
    l = float(input('Enter length of rectangle: '))
    w = float(input('Enter  width of rectangel: '))
    area = l*w
    print(area)
    circum = 2*(l+w)
    print(circum)
rectangle()
