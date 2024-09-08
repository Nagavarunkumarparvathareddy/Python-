print('''
Approach 2: Inputs Values in Function head : YES
            Returns Values in              : No
**************************************************************************     
Input   : Function call 
Process : Function def = fun heading + fun body
Output  : Function def
''')
def si(p,t,r):
    simple_int = p*t*r/100
    amount = simple_int+p
    print(simple_int)
    print(amount)
p = float(input('p: '))
t = float(input('t: '))
r = float(input('r: '))
si(p,t,r)
