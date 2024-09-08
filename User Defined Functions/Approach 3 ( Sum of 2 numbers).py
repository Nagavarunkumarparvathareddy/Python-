print('''
Approach 2: Inputs Values in Function head : YES
            Returns Values in              : No
**************************************************************************     
Input   : Function call 
Process : Function def = fun heading + fun body
Output  : Function def
''')
def rect(l,w):
    area = l*w
    circum = 2*(l+w)
    print(area)
    print(circum)
l = float(input('l: '))
w = float(input('w: '))
rect(l,w)
