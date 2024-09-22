import math
print('''
Approach 1 : Inputs Values in Function call : Yes
             Returns Values in              : Yes
**************************************************************************     
Input   : Function call 
Process : Function def = fun heading + fun body
Output  : Function call
''')
def si(p,t,r):
    simple_int = p*t*r / 100
    Tot_amount = p+simple_int
    return simple_int,Tot_amount
p = float(input('Enter Principle Amount: '))
t = float(input('Enter time: '))
r = float(input('Enter rate of charge: '))
result = si(p,t,r)
print(f'SI : {result[0]}')
print(f'Amount to pay : {result[1]}')
