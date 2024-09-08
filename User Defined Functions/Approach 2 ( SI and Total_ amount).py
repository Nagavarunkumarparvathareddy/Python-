print('''
Approach 2: Inputs Values in Function head : NO
            Returns Values in              : No
**************************************************************************     
Input   : Function def 
Process : Function def = fun heading + fun body
Output  : Function def
''')
def si():
    p = float(input('Enter Principle amount: '))
    t = float(input('Enter time in years: '))
    r = float(input('Enter rate of Interest: '))
    simple_int = p*t*r / 100
    amount = simple_int+p
    print(f'Simple Interest: {simple_int}')
    print(f'Amount to be paid: {amount}')
si()
